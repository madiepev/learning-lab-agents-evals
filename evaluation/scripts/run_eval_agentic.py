"""
Agentic evaluation harness for .agent.md agents.

Runs agents realistically by:
1. Parsing .agent.md frontmatter to extract system prompt, model, and tools
2. Connecting to MCP servers (Microsoft Learn, Microsoft Docs) via HTTP
3. Implementing a tool-calling loop with the declared model via Azure AI Foundry
4. Capturing the final response for scoring

Environment variables:
    FOUNDRY_PROJECT_ENDPOINT – Azure AI Foundry project endpoint
    AGENT_FILE               – path to the agent .agent.md file
    TEST_FILE                – path to the test JSONL file
    RESULTS_FILE             – path to write the results JSONL
    MODEL_OVERRIDE           – (optional) override model from agent frontmatter
    MCP_ENDPOINT             – (optional) MCP server URL, default: https://learn.microsoft.com/api/mcp
    MAX_TOOL_ROUNDS          – (optional) max tool-call rounds per query, default: 10

Authentication uses DefaultAzureCredential (managed identity in CI,
az login / VS Code locally).
"""

import asyncio
import json
import os
import sys
from pathlib import Path

import yaml
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from mcp import ClientSession

# Handle MCP SDK version differences for streamable HTTP client
try:
    from mcp.client.streamable_http import streamable_http_client as _mcp_client_factory
except ImportError:
    from mcp.client.streamable_http import streamablehttp_client as _mcp_client_factory

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ENDPOINT = os.environ.get("FOUNDRY_PROJECT_ENDPOINT")
AGENT_FILE = os.environ.get("AGENT_FILE")
TEST_FILE = os.environ.get("TEST_FILE")
RESULTS_FILE = os.environ.get("RESULTS_FILE")
MODEL_OVERRIDE = os.environ.get("MODEL_OVERRIDE")
MCP_ENDPOINT = os.environ.get("MCP_ENDPOINT", "https://learn.microsoft.com/api/mcp")
MAX_TOOL_ROUNDS = int(os.environ.get("MAX_TOOL_ROUNDS", "10"))

if not ENDPOINT:
    print("ERROR: FOUNDRY_PROJECT_ENDPOINT is not set.")
    sys.exit(1)

for var_name, var_val in [("AGENT_FILE", AGENT_FILE), ("TEST_FILE", TEST_FILE), ("RESULTS_FILE", RESULTS_FILE)]:
    if not var_val:
        print(f"ERROR: {var_name} is not set.")
        sys.exit(1)

# Model name mapping from .agent.md declarations to Azure AI Foundry deployment names
MODEL_MAP = {
    "claude sonnet 4.6 (copilot)": "claude-sonnet-4-6",
    "claude sonnet 4.6": "claude-sonnet-4-6",
}

# Tools that are VS Code-specific and cannot be replicated outside the IDE
STUB_TOOLS = {"vscode/askQuestions", "edit", "execute", "execute/createAndRunTask",
              "todo", "agent", "read", "search", "web", "web/fetch",
              "github/*", "github.vscode-pull-request-github/issue_fetch"}


# ---------------------------------------------------------------------------
# Agent file parsing
# ---------------------------------------------------------------------------


def parse_agent_file(agent_path: str) -> dict:
    """Parse an .agent.md file and return frontmatter + system prompt."""
    text = Path(agent_path).read_text(encoding="utf-8")

    frontmatter = {}
    system_prompt = text

    if text.startswith("---"):
        end_index = text.index("---", 3)
        frontmatter_text = text[3:end_index].strip()
        frontmatter = yaml.safe_load(frontmatter_text) or {}
        system_prompt = text[end_index + 3:].strip()

    return {
        "name": frontmatter.get("name", Path(agent_path).stem),
        "model": frontmatter.get("model", ""),
        "tools": frontmatter.get("tools", []),
        "system_prompt": system_prompt,
    }


def resolve_model(agent_model: str) -> str:
    """Resolve agent model declaration to a Foundry deployment name."""
    if MODEL_OVERRIDE:
        return MODEL_OVERRIDE
    if not agent_model:
        return "claude-sonnet-4-6"
    return MODEL_MAP.get(agent_model.lower().strip(), "claude-sonnet-4-6")


def needs_mcp(tools: list) -> bool:
    """Check if the agent declares MCP-backed tools."""
    mcp_prefixes = ("microsoft_docs_mcp/", "microsoft-learn/")
    for tool in tools:
        if isinstance(tool, str) and any(tool.startswith(p) or tool == p.rstrip("/") + "/*" for p in mcp_prefixes):
            return True
    return False


# ---------------------------------------------------------------------------
# MCP client
# ---------------------------------------------------------------------------


async def call_mcp_tool(session: ClientSession, tool_name: str, arguments: dict) -> str:
    """Call a specific tool on an existing MCP session and return the result."""
    try:
        result = await session.call_tool(tool_name, arguments)
        if result.content:
            parts = []
            for block in result.content:
                if hasattr(block, "text"):
                    parts.append(block.text)
            return "\n".join(parts) if parts else str(result.content)
        return ""
    except Exception as e:
        return f"[Tool error: {e}]"


# ---------------------------------------------------------------------------
# Agentic loop
# ---------------------------------------------------------------------------


async def run_agent_query(
    client,
    model: str,
    system_prompt: str,
    query: str,
    openai_tools: list[dict],
    mcp_session: ClientSession | None,
) -> str:
    """
    Run a single query through the agent with a tool-calling loop.

    The loop continues until the model produces a final text response
    or MAX_TOOL_ROUNDS is reached.
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": query},
    ]

    for round_num in range(MAX_TOOL_ROUNDS):
        kwargs = {
            "model": model,
            "messages": messages,
            "temperature": 0.2,
            "max_tokens": 2048,
        }
        if openai_tools:
            kwargs["tools"] = openai_tools

        response = client.chat.completions.create(**kwargs)
        choice = response.choices[0]

        # If the model is done (no tool calls), return the text
        if choice.finish_reason != "tool_calls" or not choice.message.tool_calls:
            return choice.message.content.strip() if choice.message.content else ""

        # Convert assistant message to dict for serialization
        assistant_msg = {"role": "assistant", "content": choice.message.content or ""}
        assistant_msg["tool_calls"] = [
            {
                "id": tc.id,
                "type": "function",
                "function": {
                    "name": tc.function.name,
                    "arguments": tc.function.arguments,
                },
            }
            for tc in choice.message.tool_calls
        ]
        messages.append(assistant_msg)

        for tool_call in choice.message.tool_calls:
            fn_name = tool_call.function.name
            try:
                fn_args = json.loads(tool_call.function.arguments)
            except json.JSONDecodeError:
                # Return parse error to model rather than calling with bad args
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": f"[Error: Invalid JSON arguments: {tool_call.function.arguments[:200]}]",
                })
                continue

            print(f"    [Round {round_num + 1}] Tool call: {fn_name}({json.dumps(fn_args)[:100]})")

            if mcp_session:
                result = await call_mcp_tool(mcp_session, fn_name, fn_args)
            else:
                result = f"[Tool '{fn_name}' not available — no MCP session]"

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result[:4000],  # Truncate large results
            })

    # Max rounds reached — return whatever we have
    last_response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.2,
        max_tokens=2048,
    )
    return last_response.choices[0].message.content.strip() if last_response.choices[0].message.content else ""


# ---------------------------------------------------------------------------
# Test data
# ---------------------------------------------------------------------------


def load_test_items(test_path: str) -> list[dict]:
    """Load JSONL test file into a list of dicts."""
    items = []
    with open(test_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


async def main() -> None:
    print(f"Agent file:   {AGENT_FILE}")
    print(f"Test file:    {TEST_FILE}")
    print(f"Results file: {RESULTS_FILE}")
    print(f"MCP endpoint: {MCP_ENDPOINT}")
    print()

    # Parse agent
    agent = parse_agent_file(AGENT_FILE)
    model = resolve_model(agent["model"])
    print(f"Agent name:   {agent['name']}")
    print(f"Agent model:  {agent['model']} -> {model}")
    print(f"Agent tools:  {agent['tools']}")
    print(f"System prompt: {len(agent['system_prompt'])} chars")
    print()

    # Load test data
    test_items = load_test_items(TEST_FILE)
    print(f"Test items: {len(test_items)}")
    print()

    # Set up Azure AI Foundry client
    project_client = AIProjectClient(
        endpoint=ENDPOINT,
        credential=DefaultAzureCredential(),
    )
    client = project_client.get_openai_client()

    # Determine if we need MCP
    use_mcp = needs_mcp(agent["tools"])

    if use_mcp:
        # Run all evaluations within a single MCP session
        async with _mcp_client_factory(MCP_ENDPOINT) as streams:
            if len(streams) == 3:
                read_stream, write_stream, _ = streams
            else:
                read_stream, write_stream = streams
            async with ClientSession(read_stream, write_stream) as mcp_session:
                await mcp_session.initialize()

                # List tools
                tools_result = await mcp_session.list_tools()
                openai_tools = []
                for tool in tools_result.tools:
                    tool_def = {
                        "type": "function",
                        "function": {
                            "name": tool.name,
                            "description": tool.description or "",
                        }
                    }
                    if tool.inputSchema:
                        tool_def["function"]["parameters"] = tool.inputSchema
                    else:
                        tool_def["function"]["parameters"] = {"type": "object", "properties": {}}
                    openai_tools.append(tool_def)
                print(f"  Connected to MCP. Found {len(openai_tools)} tools.")
                print()

                results = await _run_all_queries(client, model, agent, test_items, openai_tools, mcp_session)
    else:
        print("  Agent does not use MCP tools, skipping MCP connection")
        print()
        results = await _run_all_queries(client, model, agent, test_items, [], None)

    # Write results
    results_path = Path(RESULTS_FILE)
    results_path.parent.mkdir(parents=True, exist_ok=True)

    with open(results_path, "w", encoding="utf-8") as f:
        for item in results:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"\nWrote {len(results)} results to {RESULTS_FILE}")


async def _run_all_queries(
    client,
    model: str,
    agent: dict,
    test_items: list[dict],
    openai_tools: list[dict],
    mcp_session: ClientSession | None,
) -> list[dict]:
    """Run all test queries through the agent and return results."""
    results = []
    for i, item in enumerate(test_items, 1):
        query = item["query"]
        ground_truth = item.get("ground_truth", "")

        print(f"  [{i}/{len(test_items)}] {query[:80]}...")

        answer = await run_agent_query(
            client=client,
            model=model,
            system_prompt=agent["system_prompt"],
            query=query,
            openai_tools=openai_tools,
            mcp_session=mcp_session,
        )

        result_item = {
            "query": query,
            "response": answer,
        }
        if ground_truth:
            result_item["ground_truth"] = ground_truth
        if "id" in item:
            result_item["id"] = item["id"]
        if "scenario" in item:
            result_item["scenario"] = item["scenario"]

        results.append(result_item)
        print(f"    -> {len(answer)} chars response")

    return results


if __name__ == "__main__":
    asyncio.run(main())
