# Evaluation dimensions

Four dimensions are used to assess the quality of agent-generated learning content. The first two dimensions are active. Dimensions three and four are planned for a later phase.

## 1. Instructional design

This dimension evaluates whether the content follows sound learning principles: appropriate level, logical progression of ideas, and genuine helpfulness for the learner. Each metric is rated on a 1-3 scale.

### Metrics

#### Appropriate level for learner

| Score | Meaning |
| --- | --- |
| 1 | Too basic or too advanced |
| 2 | Mostly on level |
| 3 | Perfectly pitched |

#### Logical progression of ideas

| Score | Meaning |
| --- | --- |
| 1 | Disjointed or jumps around |
| 2 | Mostly logical flow |
| 3 | Clear, coherent structure |

#### Helpfulness for learning

| Score | Meaning |
| --- | --- |
| 1 | Unhelpful or confusing |
| 2 | Somewhat helpful |
| 3 | Clearly aids understanding |

Concrete examples for each score level will be added per metric. Those examples should be validated with instructional design experts to improve scoring consistency across evaluators.

## 2. Technical accuracy

This dimension checks the response against a curated list of known errors, including incorrect product names, deprecated terms, and commonly confused references. Each item is scored as pass or fail.

### Metric

| Result | Meaning |
| --- | --- |
| Pass | No known errors. The response uses correct terms and references. |
| Fail | A known error is present. Example: "Azure AI Foundry" instead of "Microsoft Foundry". |

### Examples from the error list

- Use `Microsoft Foundry`, not `Azure AI Foundry`.
- Add more errors to the list as they are identified.

Content developers can submit new errors to the list by opening a GitHub issue in this repository.

## 3. Acrolinx and writing style

This planned dimension will measure alignment with Microsoft writing guidance and Acrolinx targets, including clear and concise language, consistent terminology, inclusive wording, and an appropriate tone for learning content.

Metrics and implementation for this dimension are still to be defined.

## 4. File scaffolding

This planned dimension will check whether generated files and folder structure match expected Learn module conventions, including file types, naming, metadata, and required sections.

Metrics and implementation for this dimension are still to be defined.