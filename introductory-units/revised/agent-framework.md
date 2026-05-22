## Describe the core pieces of Microsoft Agent Framework

Microsoft Agent Framework gives you a consistent way to build AI agents that can reason, call tools, and work with other agents. Instead of wiring every capability yourself, you use a set of common building blocks that let the agent focus on the task and the platform handle the coordination.

That matters because most agent apps need the same basic pieces. You need a model connection, a place to manage conversation state, and a way to let the agent use tools. With Microsoft Agent Framework, those pieces fit together under one design so you can move from a simple chat experience to a more capable agent without changing the overall pattern.

That means you should define the agent's job first, then choose the tools and orchestration that support that job.

## Start with the agent

The agent is the central interface. It receives the user request, keeps the conversation moving, and decides when to call tools or hand work to another component. That makes it the right place to define the job you want the agent to do.

A useful way to think about the agent is to ask one question: what should this agent be responsible for? If the answer is clear, the rest of the design becomes easier. You can then decide whether the agent needs a chat provider, custom functions, built-in tools, or a workflow that coordinates multiple steps.

## Add the capabilities the agent needs

Chat providers connect the agent to a model service such as Azure OpenAI, OpenAI, Anthropic, or Copilot-backed services. They give the agent the language model it uses to interpret prompts and generate responses.

The other core pieces usually fall into three groups:

- Function tools extend the model with code you control.
- Built-in tools cover common needs such as code execution, file search, and web search.
- Conversation management keeps track of roles and message history so the agent stays grounded in context.

That mix gives you a practical way to add capability without turning the agent into a bundle of one-off integrations.

## Scale from one agent to many

Once a single agent works, you can use workflow orchestration to connect more than one agent. The framework supports sequential steps, parallel work, group chat patterns, and handoffs between specialized agents. That is useful when one agent should gather information, another should analyze it, and a third should produce the final response.

Microsoft Foundry agents fit into this pattern when you need enterprise features such as secure tool invocation, persistent threads, and broader Azure integration. In practice, that means you can keep the same agent design while choosing a deployment model that matches the workload.

> [!TIP]
> Start with one agent and one task. Add orchestration only when the single-agent design is no longer enough.

Now that you understand the core building blocks, you can decide whether your next step is a simple single-agent app or a larger workflow with multiple agents working together.
