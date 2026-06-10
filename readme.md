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

---

## Cognitive Load Rubric Evaluation

A specialized evaluation workflow using LLM-as-judge to score Microsoft Learn units against a Cognitive Load Theory-based rubric.

### Rubric overview

The cognitive load rubric evaluates units on 6 criteria (0-2 scale, max 12 points):

1. **Task-first opening** - Does it start with a scenario/task before introducing concepts?
2. **Prior knowledge bridge** - Does it connect new concepts to existing knowledge?
3. **Sequential complexity** - Are concepts introduced one at a time?
4. **Specificity over coverage** - Does it use concrete examples vs. feature lists? Includes visual integration assessment.
5. **Reasoning transparency** - Do examples show *why* choices are made?
6. **Schema-building activation** - Does it include in-body reflection prompts AND application-oriented assessment?

### Score bands

- **10-12**: Strong (minor improvements only)
- **7-9**: Acceptable (targeted revision needed)
- **4-6**: Needs revision (significant rewrite)
- **0-3**: Failing (full rewrite)

### Running evaluations

#### Local execution

```bash
# Set required environment variables
export GITHUB_TOKEN=your_token_here
export INPUT_FILE=evaluation/data/instructional-design-results/smoke-test-results-learn-unit-writer.jsonl

# Optional: override model (defaults to openai/gpt-4o)
export MODEL_NAME=openai/gpt-4o

# Optional: specify output directory (defaults to reports)
export OUTPUT_DIR=reports

# Run evaluation
python evaluation/scripts/cognitive-load-rubric.py
```

**Examples:**

```bash
# Evaluate smoke test results for a specific agent
export INPUT_FILE=evaluation/data/instructional-design-results/smoke-test-results-learn-unit-writer.jsonl
python evaluation/scripts/cognitive-load-rubric.py

# Evaluate all introductory units
export INPUT_FILE=introductory-units
python evaluation/scripts/cognitive-load-rubric.py

# Evaluate revised units only
export INPUT_FILE=introductory-units/revised
python evaluation/scripts/cognitive-load-rubric.py
```

#### GitHub Actions

Use the "Run Cognitive Load Evaluation" workflow:

1. Go to Actions → Run Cognitive Load Evaluation
2. Select input source:
   - **smoke-test-results**: Evaluate smoke test results (specify agent name)
   - **introductory-units**: Evaluate all introductory units
   - **revised-units**: Evaluate revised units only
   - **custom-path**: Provide custom file/directory path
3. Optionally check "Evaluate ALL agent smoke test results" to batch process all agents
4. Reports are uploaded as artifacts and optionally committed to the repo

### Output

Reports are saved to `reports/` with format: `rubric-evaluation-{source}-{timestamp}.md`

Each report includes:
- Quality band distribution
- Average scores per criterion
- Detailed per-unit breakdown with justifications
- Flagged items requiring human review (e.g., visual integration)

---

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
