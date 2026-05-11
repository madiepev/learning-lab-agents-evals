# Evaluation dimensions

Four dimensions are used to assess the quality of agent-generated learning content. The first two dimensions are active. Dimensions three and four are planned for a later phase.

## 1. Instructional design

This dimension evaluates whether the content follows sound learning principles: appropriate level, logical progression of ideas, and genuine helpfulness for the learner. Each metric is rated on a 1-5 scale.

### Metrics

#### Appropriate level for learner

| Score | Meaning |
| --- | --- |
| 1 | Too basic or too advanced |
| 2 | Often mismatched to learner level, with frequent over- or under-explanation |
| 3 | Mostly on level, with occasional mismatch in depth or assumed prior knowledge |
| 4 | Well matched to learner level, with only minor gaps in depth or scaffolding |
| 5 | Perfectly pitched to learner level throughout |

#### Logical progression of ideas

| Score | Meaning |
| --- | --- |
| 1 | Disjointed or jumps around |
| 2 | Some order is present, but flow is inconsistent and transitions are abrupt |
| 3 | Mostly logical flow; structure is understandable with minor clarity issues |
| 4 | Clear and coherent structure with helpful sequencing and transitions |
| 5 | Exceptionally clear progression where each idea naturally builds on the previous one |

#### Helpfulness for learning

| Score | Meaning |
| --- | --- |
| 1 | Unhelpful or confusing |
| 2 | Limited learning help; explanations are thin or not actionable |
| 3 | Somewhat helpful and supports baseline understanding |
| 4 | Helpful and actionable for most learners |
| 5 | Highly helpful; clearly accelerates understanding and application |

Concrete examples for each score level will be added per metric. Those examples should be validated with instructional design experts to improve scoring consistency across evaluators. The same score definitions should be reused in human evaluation and in LLM-as-judge prompts.

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
