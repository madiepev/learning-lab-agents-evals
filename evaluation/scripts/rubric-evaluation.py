"""
Compare agent responses to ground truth using an LLM-as-judge.

Reads a results JSONL (query + response + ground_truth), scores each item
on instructional design quality and writes a markdown report.

Environment variables:
    GITHUB_TOKEN  – GitHub token with models:read permission
    RESULTS_FILE  – path to the results JSONL to score
    MODEL_NAME    – (optional) GitHub Models model name, default: openai/gpt-4.1
"""

import json
import os
import re
import sys
from pathlib import Path
from openai import OpenAI

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
RESULTS_FILE = os.environ.get("RESULTS_FILE")
MODEL_NAME = os.environ.get("MODEL_NAME", "openai/gpt-4.1")

if not GITHUB_TOKEN:
    print("ERROR: GITHUB_TOKEN is not set.")
    sys.exit(1)

if not RESULTS_FILE:
    print("ERROR: RESULTS_FILE is not set.")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

RUBRIC_DEFINITIONS = {
    "appropriate_level": {
        1: "Too basic or too advanced for the intended learner.",
        2: "Often mismatched to learner level, with frequent over- or under-explanation.",
        3: "Mostly on level, with occasional mismatch in depth or assumed prior knowledge.",
        4: "Well matched to learner level, with only minor gaps in depth or scaffolding.",
        5: "Perfectly pitched to learner level throughout the response.",
    },
    "logical_progression": {
        1: "Disjointed or jumps around; ideas are hard to follow.",
        2: "Some order is present, but flow is inconsistent and transitions are abrupt.",
        3: "Mostly logical flow; structure is understandable with minor clarity issues.",
        4: "Clear and coherent structure with helpful sequencing and transitions.",
        5: "Exceptionally clear progression where each idea naturally builds on the previous one.",
    },
    "helpfulness": {
        1: "Unhelpful or confusing for learning.",
        2: "Limited learning help; explanations are thin or not actionable.",
        3: "Somewhat helpful and supports baseline understanding.",
        4: "Helpful and actionable for most learners.",
        5: "Highly helpful; clearly accelerates understanding and application.",
    },
}


def build_judge_system_prompt() -> str:
    """Create the system prompt from the repository's evaluation-dimension definitions."""
    def format_scale(metric: str, title: str) -> str:
        scale = RUBRIC_DEFINITIONS[metric]
        return (
            f"**{title}**\\n"
            f"- 1: {scale[1]}\\n"
            f"- 2: {scale[2]}\\n"
            f"- 3: {scale[3]}\\n"
            f"- 4: {scale[4]}\\n"
            f"- 5: {scale[5]}"
        )

    rubric_text = "\\n\\n".join([
        format_scale("appropriate_level", "Appropriate level for learner"),
        format_scale("logical_progression", "Logical progression of ideas"),
        format_scale("helpfulness", "Helpfulness for learning"),
    ])

    return (
        "You are an instructional-design judge for Microsoft Learn training content.\\n\\n"
        "Score only the RESPONSE while using QUERY and GROUND TRUTH as context for learner intent. "
        "Use the rubric exactly as defined below, assigning one integer score (1-5) per metric.\\n\\n"
        f"{rubric_text}\\n\\n"
        "Scoring rules:\\n"
        "- Return only integer scores from 1 to 5.\\n"
        "- Do not use half scores.\\n"
        "- Favor the lower score when evidence is mixed.\\n"
        "- Keep notes concise and evidence-based.\\n\\n"
        "Reply with ONLY a JSON object (no markdown fences):\\n"
        "{\"appropriate_level\": <int>, \"logical_progression\": <int>, \"helpfulness\": <int>, \"notes\": \"<brief explanation>\"}"
    )

JUDGE_SYSTEM_PROMPT = build_judge_system_prompt()


def load_results(path: str) -> list[dict]:
    """Load JSONL results file."""
    items = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items


def extract_agent_name(results_path: str) -> str:
    """Derive agent name from results filename like smoke-test-results-learn-module-writer.jsonl."""
    stem = Path(results_path).stem  # smoke-test-results-learn-module-writer
    prefix = "smoke-test-results-"
    if stem.startswith(prefix):
        return stem[len(prefix):]
    return stem


def parse_judge_response(text: str) -> dict:
    """Parse the judge LLM's JSON response, handling markdown fences if present."""
    # Strip markdown code fences if the model wraps its response
    cleaned = re.sub(r"^```(?:json)?\s*", "", text.strip())
    cleaned = re.sub(r"\s*```$", "", cleaned)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {
            "appropriate_level": 1,
            "logical_progression": 1,
            "helpfulness": 1,
            "notes": f"Failed to parse judge response: {text[:200]}",
        }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    print(f"Results file: {RESULTS_FILE}")
    print(f"Judge model:  {MODEL_NAME}")

    results = load_results(RESULTS_FILE)
    print(f"Items to score: {len(results)}")

    agent_name = extract_agent_name(RESULTS_FILE)
    print(f"Agent name: {agent_name}")

    # Set up GitHub Models client (OpenAI-compatible)
    client = OpenAI(
        base_url="https://models.github.ai/inference",
        api_key=GITHUB_TOKEN,
    )

    scores = []
    for i, item in enumerate(results, 1):
        query = item["query"]
        response = item["response"]
        ground_truth = item["ground_truth"]

        print(f"  [{i}/{len(results)}] Scoring: {query[:70]}...")

        user_prompt = (
            f"QUERY: {query}\n\n"
            f"GROUND TRUTH: {ground_truth}\n\n"
            f"RESPONSE: {response}"
        )

        judge_response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": JUDGE_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.0,
            max_tokens=256,
        )

        judge_text = judge_response.choices[0].message.content.strip()
        score = parse_judge_response(judge_text)
        score["query"] = query
        score["response"] = response
        score["ground_truth"] = ground_truth
        score["verdict"] = (
            "PASS"
            if score.get("appropriate_level", 0) >= 3
            and score.get("logical_progression", 0) >= 3
            and score.get("helpfulness", 0) >= 3
            else "FAIL"
        )
        scores.append(score)

    # Aggregate metrics
    total = len(scores)
    pass_count = sum(1 for s in scores if s["verdict"] == "PASS")
    pass_rate = (pass_count / total * 100) if total else 0

    level_scores = [s["appropriate_level"] for s in scores]
    progression_scores = [s["logical_progression"] for s in scores]
    helpfulness_scores = [s["helpfulness"] for s in scores]

    def avg(lst):
        return sum(lst) / len(lst) if lst else 0

    # Write report
    report_dir = Path("reports")
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / f"{agent_name}-smoke-test-report.md"

    lines = [
        f"# Smoke Test Report: {agent_name}",
        "",
        f"**Date:** {os.popen('date +%Y-%m-%d 2>/dev/null || echo unknown').read().strip()}",
        f"**Test file:** smoke-test.jsonl",
        f"**Total questions:** {total}",
        f"**Pass rate:** {pass_count}/{total} ({pass_rate:.0f}%)",
        "",
        "## Summary",
        "",
        "| Criterion | Average | Min | Max |",
        "|-----------|---------|-----|-----|",
        f"| Appropriate level | {avg(level_scores):.1f} | {min(level_scores)} | {max(level_scores)} |",
        f"| Logical progression | {avg(progression_scores):.1f} | {min(progression_scores)} | {max(progression_scores)} |",
        f"| Helpfulness | {avg(helpfulness_scores):.1f} | {min(helpfulness_scores)} | {max(helpfulness_scores)} |",
        "",
        "## Details",
        "",
    ]

    for i, s in enumerate(scores, 1):
        lines.extend([
            f"### Q{i}: {s['query']}",
            "",
            f"- **Ground truth:** {s['ground_truth']}",
            f"- **Response:** {s['response']}",
            f"- **Scores:** Appropriate level: {s['appropriate_level']} | Logical progression: {s['logical_progression']} | Helpfulness: {s['helpfulness']}",
            f"- **Verdict:** {s['verdict']}",
            f"- **Notes:** {s.get('notes', '')}",
            "",
        ])

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nReport written to {report_path}")

    # Print summary to stdout for CI
    print(f"\n{'=' * 60}")
    print(f"  {agent_name} — Pass rate: {pass_count}/{total} ({pass_rate:.0f}%)")
    print(
        "  Appropriate level: "
        f"{avg(level_scores):.1f}  Logical progression: {avg(progression_scores):.1f}  "
        f"Helpfulness: {avg(helpfulness_scores):.1f}"
    )
    print(f"{'=' * 60}")

    # Exit with failure if pass rate < 80%
    if pass_rate < 80:
        print(f"\nFAILED: Pass rate {pass_rate:.0f}% is below 80% threshold.")
        sys.exit(1)


if __name__ == "__main__":
    main()
