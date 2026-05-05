# End-to-End Smoke Test: Plan Module → Plan Unit → Write Unit

This smoke test covers the full authoring pipeline across three prompts: module planning, unit planning, and unit writing. Each prompt is standalone and can be run independently. The written unit uses a constrained output length (max ~300 words of body content) to keep evaluation fast and consistent. **The length constraint is for test purposes only and should not be used in production.**

Each prompt is run against all agents under test.

---

## Prompt 1 — Plan the module

---

> **Target audience:** AI Engineer
>
> **Level:** Beginner
>
> Plan a module titled **"Get started with Azure AI Services"**. The module should have three units. For each unit, provide the unit title and a one-sentence learning objective.

---

## Prompt 2 — Plan the unit

---

> **Target audience:** AI Engineer
>
> **Level:** Beginner
>
> Plan the first unit of a module titled **"Get started with Azure AI Services"** in detail. Define the unit title, role, ms.service, learning objectives, and key concepts to cover.

---

## Prompt 3 — Write the unit

---

> **Target audience:** AI Engineer
>
> **Level:** Beginner
>
> Write a unit titled **"What is Azure AI Services?"** for a beginner-level module on getting started with Azure AI Services.
>
> **Output constraint (test only):** Limit the unit body to a maximum of 300 words. Do not truncate mid-sentence — stay within the limit while producing a coherent, complete unit. This constraint exists to speed up evaluation and will not apply in real use.

---

## Additional role-based prompt sets

The following prompt sets use the same structure but vary the role and topic. Each prompt remains standalone.

### Prompt set B — Data Analyst / Microsoft Fabric

#### Prompt 1 — Plan the module

> **Target audience:** Data Analyst
>
> **Level:** Beginner
>
> Plan a module titled **"Get started with Microsoft Fabric"**. The module should have three units. For each unit, provide the unit title and a one-sentence learning objective.

#### Prompt 2 — Plan the unit

> **Target audience:** Data Analyst
>
> **Level:** Beginner
>
> Plan the first unit of a module titled **"Get started with Microsoft Fabric"** in detail. Define the unit title, role, ms.service, learning objectives, and key concepts to cover.

#### Prompt 3 — Write the unit

> **Target audience:** Data Analyst
>
> **Level:** Beginner
>
> Write a unit titled **"What is Microsoft Fabric?"** for a beginner-level module on getting started with Microsoft Fabric.
>
> **Output constraint (test only):** Limit the unit body to a maximum of 300 words. Do not truncate mid-sentence — stay within the limit while producing a coherent, complete unit. This constraint exists to speed up evaluation and will not apply in real use.

### Prompt set C — Security Engineer / Microsoft Sentinel

#### Prompt 1 — Plan the module

> **Target audience:** Security Engineer
>
> **Level:** Beginner
>
> Plan a module titled **"Get started with Microsoft Sentinel"**. The module should have three units. For each unit, provide the unit title and a one-sentence learning objective.

#### Prompt 2 — Plan the unit

> **Target audience:** Security Engineer
>
> **Level:** Beginner
>
> Plan the first unit of a module titled **"Get started with Microsoft Sentinel"** in detail. Define the unit title, role, ms.service, learning objectives, and key concepts to cover.

#### Prompt 3 — Write the unit

> **Target audience:** Security Engineer
>
> **Level:** Beginner
>
> Write a unit titled **"What is Microsoft Sentinel?"** for a beginner-level module on getting started with Microsoft Sentinel.
>
> **Output constraint (test only):** Limit the unit body to a maximum of 300 words. Do not truncate mid-sentence — stay within the limit while producing a coherent, complete unit. This constraint exists to speed up evaluation and will not apply in real use.

### Prompt set D — Administrator / Azure Virtual Networks

#### Prompt 1 — Plan the module

> **Target audience:** Administrator
>
> **Level:** Beginner
>
> Plan a module titled **"Get started with Azure virtual networks"**. The module should have three units. For each unit, provide the unit title and a one-sentence learning objective.

#### Prompt 2 — Plan the unit

> **Target audience:** Administrator
>
> **Level:** Beginner
>
> Plan the first unit of a module titled **"Get started with Azure virtual networks"** in detail. Define the unit title, role, ms.service, learning objectives, and key concepts to cover.

#### Prompt 3 — Write the unit

> **Target audience:** Administrator
>
> **Level:** Beginner
>
> Write a unit titled **"What are Azure virtual networks?"** for a beginner-level module on getting started with Azure virtual networks.
>
> **Output constraint (test only):** Limit the unit body to a maximum of 300 words. Do not truncate mid-sentence — stay within the limit while producing a coherent, complete unit. This constraint exists to speed up evaluation and will not apply in real use.

---

## What to evaluate

All three stages are scored using the instructional design dimension. Each metric is rated 1–3.

### Metric: Appropriate level for learner

| Score | Meaning |
|---|---|
| 1 | Too basic or too advanced for the stated audience |
| 2 | Mostly on level |
| 3 | Perfectly pitched for the stated audience and level |

Apply this metric to each stage:
- **Module plan** — Are the three unit topics appropriately scoped for the stated audience and level? No unnecessary prerequisites assumed.
- **Unit plan** — Do the selected unit's learning objectives match the stated audience and level?
- **Written unit** — Is the content free of unexplained jargon? Does it assume only the background knowledge implied by the prompt?

### Metric: Logical progression of ideas

| Score | Meaning |
|---|---|
| 1 | Disjointed or jumps around |
| 2 | Mostly logical flow |
| 3 | Clear, coherent structure |

Apply this metric to each stage:
- **Module plan** — Do the three units build on each other in a sensible sequence?
- **Unit plan** — Are the key concepts ordered from simple to complex for the stated audience and level?
- **Written unit** — Does the content flow from introduction → concept explanation → closing thought without abrupt jumps?

### Metric: Helpfulness for learning

| Score | Meaning |
|---|---|
| 1 | Unhelpful or confusing |
| 2 | Somewhat helpful |
| 3 | Clearly aids understanding |

Apply this metric to each stage:
- **Module plan** — Does the plan give the learner a clear picture of what they will be able to do after completing the module?
- **Unit plan** — Are the learning objectives measurable and actionable (Bloom's verb + observable outcome)?
- **Written unit** — Does the content give the learner a clear mental model? Does the 300-word constraint result in a coherent unit or a truncated one?

---

## Notes

- The 300-word constraint deliberately creates tension between completeness and concision. A good output stays within the limit without feeling truncated — this is itself a signal for the helpfulness metric.
