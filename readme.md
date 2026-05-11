# Learning lab agents evals

Playground for experimenting with automated and manual evaluations for Learning Lab agents.

## Evaluation workflow

This workflow describes the end-to-end loop for improving smoke tests, collecting agent responses, running human and automated scoring, and comparing agreement per agent.

### 1. Define better smoke test inputs

MJ updates the smoke-test dataset so each query is explicit, scoped, and easy to score. Prompts should make expected product naming clear and cover representative agent behaviors.

- Clear query intent
- Expected product naming
- Source file: `evaluation/data/technical-accuracy-tests/smoke-test.jsonl`

### 2. Generate agent answers for the defined inputs

Each agent responds to the updated smoke-test prompts. Outputs are stored as agent-specific result files and become the single source used by both human and automated evaluation.

- One results file per agent
- Query and response pairs
- Ready for scoring

### 3. Create a rubric with examples

Define clear scoring guidance with positive and negative examples so humans score consistently. The rubric includes one binary metric and three instructional design metrics from the app.

- Product name accuracy: correct or incorrect
- Appropriate level: 1-5
- Logical progression: 1-5
- Helpfulness: 1-5

### 4. Rate outputs one by one per agent

Evaluators use the human evaluation app to score each response for one agent at a time. This keeps context stable and improves consistency across ratings.

- Single-agent review sessions
- One response at a time
- Structured rubric inputs

### 5. Run parallel analysis after responses are available

#### Automated output: evaluate product name accuracy

A dedicated script checks whether required product names are correct for each response. It outputs binary scores and per-agent aggregates.

#### Agreement analysis: compare human vs auto ratings

Human product-name scores are compared with automated scores to measure inter-rater reliability and identify mismatches in the scoring logic or rubric interpretation.

Primary reliability metric: Cohen's Kappa on product name accuracy, reported per agent and overall.

### 6. Visualize the outcome per agent

Publish comparable views for each agent: product-name accuracy, instructional design scores, and human-vs-auto agreement. Use these views to iterate on prompts, rubric examples, and agent instructions.

- Per-agent dashboards
- Human and auto comparison
- Rubric refinement loop

## Repository structure

```text
learning-lab-agents-evals/
├── readme.md
├── evaluation-dimensions.md
├── sprint-tasks.md
├── agents/
├── evaluation/
│   ├── data/
│   │   ├── technical-accuracy-tests/
│   │   └── technical-accuracy-results/
│   ├── reports/
│   └── scripts/
└── reports/
```

## Key paths

### `agents/`

Agent definition files under evaluation. Each `.agent.md` file defines the behavior being tested.

### `evaluation/data/technical-accuracy-tests/`

Input JSONL files for evaluation. Each line represents a test case.

### `evaluation/data/technical-accuracy-results/`

Agent-specific output JSONL files used as the basis for human and automated scoring.

### `evaluation/scripts/`

Scripts for running evaluations, comparing results, and supporting the human evaluation workflow.

### `evaluation/reports/` and `reports/`

Generated outputs and summary artifacts for comparing agent performance.

## Related files

- `evaluation-dimensions.md`: scoring dimensions and planned evaluation areas
- `sprint-tasks.md`: current sprint task board in Markdown
