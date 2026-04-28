# Sprint tasks

Week of April 28, 2026.

Execute the full evaluation workflow: improve smoke test inputs, define a rubric with examples, run agents, then flow through human and automated scoring with comparison.

## Status

- Done: Human rating UI (Ivor), workflow defined, dimensions defined, v0 test dataset
- This sprint: 5 tasks

## 1. Update smoke test dataset

Status: In progress  
Owner: MJ

Improve `smoke-test.jsonl` so each query is explicit and scoped. Include expected product names to make evaluation scoring objective. This becomes the single source for both agent responses and human and automated scoring.

- Initial dataset v0 exists
- Rewrite queries for clarity and scope so each query has one clear intent
- Add expected product names for each query, for example `Microsoft Foundry` and `Azure Functions`
- Update `smoke-test.jsonl` and commit

Related context: README workflow

## 2. Create rubric with antwoordmodel

Status: To do  
Owner: MJ plus instructional design expert

Write concrete positive and negative examples for each score level across the active evaluation dimensions: product name accuracy, appropriate level, logical progression, and helpfulness.

- Write two examples per score for each instructional design metric
- Define product name accuracy as binary, with correct and incorrect examples
- Validate the examples with an instructional design expert
- Add the examples to `evaluation-dimensions.md` and the human evaluation app as guidance

Related context: `evaluation-dimensions.md`

## 3. Generate agent responses

Status: To do  
Owner: Ivor plus team

Run each agent against the updated smoke-test queries. Store results as per-agent JSONL files. This output becomes the single source for both human and automated evaluation.

- Ensure each agent definition is finalized and committed
- Run query-response generation for each agent
- Store results in `evaluation/data/technical-accuracy-results/`, one file per agent
- Verify all agents have complete response sets

Related context: README workflow

## 4. Set up automated product-name check

Status: To do  
Owner: J

Build a script that checks each agent response for correct product names. Output binary pass or fail per query and per-agent aggregates. This is the automated scoring baseline for human comparison.

- Define the product-name reference list, for example `Microsoft Foundry` and `Azure Functions`
- Write the script to scan responses and flag incorrect names
- Output structured results for per-query and per-agent summaries
- Run the script against all agent result files

Related context: `evaluation-dimensions.md`

## 5. Prepare per-agent dashboard and visualization

Status: To do  
Owner: Juliane plus team

Create a dashboard or report layout that displays metrics for each agent: product-name accuracy, instructional design scores, and human-versus-automated agreement using Cohen's Kappa. This enables iterative refinement based on results.

### Dashboard layout

1. Product name accuracy: percentage correct and incorrect for human and automated scoring.
2. Instructional design metrics: mean scores for appropriate level, logical progression, and helpfulness.
3. Human-versus-automated agreement: Cohen's Kappa on product-name accuracy.
4. Query-level details: drill-down view showing human score, automated score, and agreement for each item.

- Design the dashboard template
- Write a script to aggregate human evaluation CSVs and automated scores by agent
- Generate Cohen's Kappa per agent for product-name accuracy
- Populate and publish initial dashboards in `reports/`

Related context: README workflow and `evaluation-dimensions.md`