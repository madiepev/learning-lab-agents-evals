"""
Evaluate Microsoft Learn units using LLM-as-judge with the Unit Quality Rubric.

Reads unit content (from JSONL or individual files), scores each on 6 instructional
design criteria (0-2 scale), and writes a detailed markdown report.

Environment variables:
    GITHUB_TOKEN  – GitHub token with models:read permission
    INPUT_FILE    – path to JSONL file with units OR directory with .md files
    MODEL_NAME    – (optional) GitHub Models model name, default: openai/gpt-4o
    OUTPUT_DIR    – (optional) directory for reports, default: reports/
"""

import json
import os
import re
import sys
from pathlib import Path
from openai import OpenAI
from datetime import datetime

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
INPUT_FILE = os.environ.get("INPUT_FILE")
MODEL_NAME = os.environ.get("MODEL_NAME", "openai/gpt-4o")
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "reports")

if not GITHUB_TOKEN:
    print("ERROR: GITHUB_TOKEN is not set.")
    sys.exit(1)

if not INPUT_FILE:
    print("ERROR: INPUT_FILE is not set.")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Rubric Definition
# ---------------------------------------------------------------------------

RUBRIC_PROMPT = """# Microsoft Learn Unit Quality Rubric

## LLM-as-Judge Evaluation Prompt

---

## Framework: Why This Rubric Exists

This rubric is grounded in **Cognitive Load Theory**, which describes how working memory — the mental space where active learning happens — can be spent in three ways:

- **Intrinsic load**: the inherent complexity of the subject matter (the actual concepts being taught). This is managed by scoping what the unit covers and how it sequences complexity.

- **Extraneous load**: unnecessary cognitive work imposed by *how content is presented* — searching for relevant information, decoding abstract language, or mapping between separated text and visuals. This should be minimised. It is the primary difference between documentation and learning material.

- **Germane load**: productive cognitive effort that builds lasting understanding — constructing mental models, making connections, reasoning through decisions. This should be maximised.

A unit that reads like documentation tends to be high in extraneous load and low in germane load. This rubric operationalises what "good" looks like in each dimension as observable, scoreable writing behaviours.

---

## Instructions

You are evaluating a Microsoft Learn training unit for instructional quality.

**Apply this rubric only to conceptual/instructional units.** Do not evaluate introduction units, exercise units, knowledge check units, or summary units — these serve structural roles and are not assessed here.

Score the unit on 6 criteria, each on a **0–2 scale**. For each criterion, provide:

- A score (0, 1, or 2)
- A one-sentence justification citing specific evidence from the text

Then return a total score out of 12 and a brief overall assessment.

---

## Criteria

### 1. Task-first opening

*Does the unit open with a concrete scenario or task context that establishes **why** the learner needs this capability — before introducing the tool or concept?*

Opening with a task rather than a definition reduces the cognitive work of figuring out why the content is relevant. It also increases learner motivation to invest effort in understanding — higher motivation has been shown to increase the depth of cognitive processing during learning.

| Score | Description |
|-------|-------------|
| **2** | Unit opens with a specific scenario or task that grounds the content in a real use case. The learner knows why they are reading this before any concept is introduced. |
| **1** | A scenario or context is present but generic, vague ("In this unit you will learn..."), or appears after conceptual content has already started. |
| **0** | No scenario or task context. Unit opens directly with definitions, feature descriptions, or tool names. |

---

### 2. Prior knowledge bridge

*Does the unit explicitly connect the new concept to something the learner is assumed to already know?*

When a new concept is connected to existing knowledge, learners can extend an existing mental model rather than build one from scratch. This reduces the complexity load on working memory by letting learners treat familiar elements as a single chunk rather than multiple separate pieces.

| Score | Description |
|-------|-------------|
| **2** | At least one explicit connection is made to a prerequisite concept, analogous tool, or familiar pattern (e.g., "If you've used X, this works similarly because..."). |
| **1** | An implicit connection exists but is not stated. The learner must infer the relationship. |
| **0** | No connection to prior knowledge. New concepts are introduced in isolation. |

---

### 3. Sequential complexity

*Does the unit introduce concepts one at a time, resolving each before introducing the next?*

The complexity of a subject comes from the number of interacting elements a learner must hold in mind simultaneously. Presenting all interacting elements at once — as documentation typically does — exceeds working memory capacity. Sequencing them so each is understood before the next is introduced keeps the load manageable.

| Score | Description |
|-------|-------------|
| **2** | Content is clearly sequenced. Each concept is explained and contextualised before the next is introduced. No paragraph requires the reader to hold multiple unresolved concepts simultaneously. |
| **1** | Mostly sequential but with at least one section that introduces multiple new concepts together without resolution. |
| **0** | Multiple new concepts introduced simultaneously. Reader must hold several unresolved ideas to follow the content. |

---

### 4. Specificity over coverage — including visual integration

*Does the unit use concrete, specific examples rather than comprehensive feature lists or abstract descriptions? When visuals are present, are they integrated with the text rather than spatially separated?*

This criterion covers two sources of unnecessary cognitive load — load imposed by how the content is presented rather than by the content itself:

**(a) Abstract or comprehensive prose** forces the learner to do extra interpretive work: translating vague language into meaning, deciding which features are relevant, or inferring how a capability applies to their situation. Good learning material does this work for the learner by anchoring explanations to a specific, concrete example.

**(b) The split-attention effect** occurs when text and visuals are placed in separate blocks, requiring the learner to search back and forth between them to construct a complete picture. Presenting explanatory text immediately adjacent to or within the visual eliminates this search cost. (Validated in Klepsch & Seufert, 2020.)

> **Note for automated evaluation**: Sub-criterion (b) requires the evaluator to inspect visual placement. If visuals cannot be read, score only sub-criterion (a) and set `visual_integration_flagged: true` to indicate that human review of visual layout is needed.

| Score | Description |
|-------|-------------|
| **2** | Explanations are anchored to specific, concrete examples tied to the scenario. Abstract descriptions are absent or minimal. Content links to Docs for completeness rather than reproducing it. Where visuals are present, explanatory text is placed immediately adjacent to or within the visual (callouts, captions, or inline annotation) — not in a separate block requiring search. |
| **1** | Mix of concrete examples and abstract or comprehensive descriptions, OR prose is specific but visuals are separated from their explanatory text with only a vague reference (e.g., "See the diagram above"). |
| **0** | Content reads like documentation: comprehensive feature coverage, abstract language ("wide range of options," "various sources"), or bullet lists of capabilities without contextualisation. Visuals, if present, are fully separated from explanatory text with no integration. |

---

### 5. Reasoning transparency

*Do worked examples show **why** a choice is made, not just **what** to do?*

A purely procedural example (step 1, step 2, step 3) tells the learner what happened but not why. Without understanding the reasoning, the learner cannot apply the approach in a different situation. Exposing the decision process — why this tool over an alternative, what tradeoff is being made, what would break this approach — is what turns a procedure into a transferable mental model. Research on worked examples consistently shows this reduces the cognitive effort of problem-solving and improves task performance. (Validated in Klepsch & Seufert, 2020.)

| Score | Description |
|-------|-------------|
| **2** | At least one example explicitly surfaces the decision process: why this approach over an alternative, what tradeoff is involved, or what would fail in a different context. |
| **1** | Examples show what to do but without explicit reasoning. A reader could follow the steps but not explain the choice. |
| **0** | No worked examples, or examples are purely procedural (step 1, step 2...) with no rationale. |

---

### 6. Schema-building activation

*Does the unit actively promote understanding — both within the body and at the assessment?*

Productive cognitive effort — the kind that builds lasting mental models — can be fostered at two points in a unit:

**(a) In-body prompts**: explicit moments that ask the learner to construct meaning before or while receiving it. Examples include reflection questions ("Before reading on, consider why you might choose X over Y"), self-explanation invitations ("How would this apply to your scenario?"), or prediction prompts. These direct cognitive effort toward schema construction rather than passive reading. (Validated in Klepsch & Seufert, 2020.)

**(b) Application-oriented assessment**: a knowledge check that places the concept in a new context — requiring the learner to reason rather than recall. Questions that can be answered by searching the text do not activate schema use.

> **Note**: Score (a) and (b) together. A unit with strong in-body prompts but a weak knowledge check scores 1. A unit with both scores 2. A unit with neither scores 0.

| Score | Description |
|-------|-------------|
| **2** | Unit contains at least one explicit in-body prompt that asks the learner to reflect, predict, or self-explain (e.g., "Before reading on, consider...", "Why might you choose X over Y here?") AND the knowledge check presents a new scenario requiring a decision or diagnosis rather than recall. |
| **1** | Either the unit body contains reflection or self-explanation prompts but the knowledge check is recall-based, OR the knowledge check tests application but the body contains no prompts — only one mechanism is present. |
| **0** | No reflection or self-explanation prompts in the unit body, and the knowledge check is purely recall-based (e.g., "What does X do?" "Which of the following is true about Y?") or absent. |

---

## Output Format

Return a JSON object in the following structure:

```json
{
  "unit_title": "",
  "scores": {
    "task_first_opening": {
      "score": 0,
      "justification": "One sentence citing specific evidence from the text."
    },
    "prior_knowledge_bridge": {
      "score": 0,
      "justification": "One sentence citing specific evidence from the text."
    },
    "sequential_complexity": {
      "score": 0,
      "justification": "One sentence citing specific evidence from the text."
    },
    "specificity_over_coverage": {
      "score": 0,
      "justification": "One sentence citing specific evidence from the text.",
      "visual_integration_flagged": false
    },
    "reasoning_transparency": {
      "score": 0,
      "justification": "One sentence citing specific evidence from the text."
    },
    "schema_building_activation": {
      "score": 0,
      "justification": "One sentence citing specific evidence from the text."
    }
  },
  "total": 0,
  "band": "",
  "overall": "2–3 sentences naming the unit's strongest and weakest criteria and the single highest-priority revision."
}
```

---

## Score Bands

| Total | Band | Interpretation |
|-------|------|----------------|
| 10–12 | **Strong** | Meets instructional quality standards. Minor improvements only. |
| 7–9 | **Acceptable** | Specific criteria need targeted revision before publication. |
| 4–6 | **Needs revision** | Content likely reads like documentation or marketing. Significant rewrite required. |
| 0–3 | **Failing** | Does not function as learning material. Full rewrite recommended. |

---

## Common Failure Patterns (Reference for Justifications)

Use these to calibrate your scoring and write precise justifications:

- **Documentation drift** — Unit covers all features of a tool rather than the task in scope. Often signals score of 0 on criteria 1 and 4.
- **Marketing language** — Phrases like "powerful," "seamless," "enables you to unlock" with no concrete example. Signals score of 0 on criterion 4.
- **Abstract feature lists** — Bullet lists of capabilities ("You can filter, aggregate, join, reshape...") without showing any one of them applied to the scenario. Signals score of 0–1 on criteria 4 and 5.
- **Cold opening** — Unit begins with "In this unit, you will learn about X" or a definition of X. Signals score of 0–1 on criterion 1.
- **Passive delivery** — Unit delivers information page after page without ever pausing to ask the learner to reflect, predict, or explain back. No schema construction happens until the knowledge check (if at all). Signals score of 0–1 on criterion 6.
- **Recall-only knowledge check** — Questions of the form "What is X?" or "Which of the following is true about Y?" that can be answered by searching the unit text. Signals score of 0–1 on criterion 6.
- **Split-attention layout** — Diagram or screenshot placed in a separate block from the text that explains it, with only a vague reference ("as shown above"). Learner must search between text and visual to construct meaning. Signals score of 0–1 on criterion 4. Set `visual_integration_flagged: true`.

---

Scoring rules:
- Return only integer scores of 0, 1, or 2 for each criterion.
- Do not use half scores or scores outside the 0–2 range.
- Favor the lower score when evidence is mixed.
- Keep justifications concise and evidence-based.
- Reply with ONLY a JSON object (no markdown fences).
"""

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_units(path: str) -> list[dict]:
    """Load units from JSONL file or directory of markdown files."""
    input_path = Path(path)
    units = []
    
    if input_path.is_file() and input_path.suffix == '.jsonl':
        # Load from JSONL
        with open(input_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    item = json.loads(line)
                    units.append({
                        "title": item.get("title", item.get("query", "Untitled")),
                        "content": item.get("content", item.get("response", "")),
                    })
    elif input_path.is_dir():
        # Load all .md files from directory
        for md_file in input_path.glob("**/*.md"):
            if md_file.name.lower() in ["readme.md", "index.md"]:
                continue
            content = md_file.read_text(encoding="utf-8")
            units.append({
                "title": md_file.stem,
                "content": content,
                "file_path": str(md_file),
            })
    elif input_path.is_file() and input_path.suffix == '.md':
        # Single markdown file
        content = input_path.read_text(encoding="utf-8")
        units.append({
            "title": input_path.stem,
            "content": content,
            "file_path": str(input_path),
        })
    else:
        print(f"ERROR: INPUT_FILE must be a .jsonl file, .md file, or directory")
        sys.exit(1)
    
    return units


def parse_judge_response(text: str) -> dict:
    """Parse the judge LLM's JSON response, handling markdown fences if present."""
    # Strip markdown code fences if the model wraps its response
    cleaned = re.sub(r"^```(?:json)?\s*", "", text.strip())
    cleaned = re.sub(r"\s*```$", "", cleaned)
    
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        print(f"WARNING: Failed to parse judge response: {e}")
        print(f"Response: {text[:500]}")
        return {
            "unit_title": "Parse Error",
            "scores": {
                "task_first_opening": {"score": 0, "justification": "Failed to parse response"},
                "prior_knowledge_bridge": {"score": 0, "justification": "Failed to parse response"},
                "sequential_complexity": {"score": 0, "justification": "Failed to parse response"},
                "specificity_over_coverage": {"score": 0, "justification": "Failed to parse response"},
                "reasoning_transparency": {"score": 0, "justification": "Failed to parse response"},
                "schema_building_activation": {"score": 0, "justification": "Failed to parse response"},
            },
            "total": 0,
            "band": "Failing",
            "overall": f"Failed to parse judge response: {str(e)}",
        }


def calculate_band(total: int) -> str:
    """Determine quality band from total score."""
    if total >= 10:
        return "Strong"
    elif total >= 7:
        return "Acceptable"
    elif total >= 4:
        return "Needs revision"
    else:
        return "Failing"


def score_unit(client: OpenAI, unit: dict) -> dict:
    """Score a single unit using the LLM judge."""
    title = unit.get("title", "Untitled")
    content = unit.get("content", "")
    
    user_prompt = f"UNIT TITLE: {title}\n\nUNIT CONTENT:\n{content}"
    
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": RUBRIC_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.0,
        max_tokens=1024,
    )
    
    judge_text = response.choices[0].message.content.strip()
    result = parse_judge_response(judge_text)
    
    # Add unit metadata to result
    result["input_title"] = title
    if "file_path" in unit:
        result["file_path"] = unit["file_path"]
    
    # Ensure total and band are present
    if "total" not in result or result["total"] == 0:
        # Calculate total from scores if missing
        scores = result.get("scores", {})
        total = sum(
            s.get("score", 0) for s in scores.values()
        )
        result["total"] = total
    
    if "band" not in result:
        result["band"] = calculate_band(result["total"])
    
    return result


def write_report(results: list[dict], output_path: Path) -> None:
    """Write evaluation results to a markdown report."""
    total_units = len(results)
    
    # Calculate aggregate statistics
    total_scores = [r["total"] for r in results]
    avg_total = sum(total_scores) / total_units if total_units else 0
    
    criteria_names = [
        "task_first_opening",
        "prior_knowledge_bridge",
        "sequential_complexity",
        "specificity_over_coverage",
        "reasoning_transparency",
        "schema_building_activation",
    ]
    
    criteria_stats = {}
    for criterion in criteria_names:
        scores = [
            r.get("scores", {}).get(criterion, {}).get("score", 0)
            for r in results
        ]
        criteria_stats[criterion] = {
            "avg": sum(scores) / len(scores) if scores else 0,
            "min": min(scores) if scores else 0,
            "max": max(scores) if scores else 0,
        }
    
    # Count by band
    band_counts = {}
    for r in results:
        band = r.get("band", "Unknown")
        band_counts[band] = band_counts.get(band, 0) + 1
    
    # Build report
    lines = [
        "# Microsoft Learn Unit Quality Evaluation Report",
        "",
        f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Model:** {MODEL_NAME}",
        f"**Total units evaluated:** {total_units}",
        f"**Average total score:** {avg_total:.1f} / 12",
        "",
        "## Quality Band Distribution",
        "",
        "| Band | Count | Percentage |",
        "|------|-------|------------|",
    ]
    
    for band in ["Strong", "Acceptable", "Needs revision", "Failing"]:
        count = band_counts.get(band, 0)
        pct = (count / total_units * 100) if total_units else 0
        lines.append(f"| {band} | {count} | {pct:.1f}% |")
    
    lines.extend([
        "",
        "## Criteria Summary",
        "",
        "Average scores by criterion (0–2 scale):",
        "",
        "| Criterion | Average | Min | Max |",
        "|-----------|---------|-----|-----|",
    ])
    
    criterion_labels = {
        "task_first_opening": "Task-first opening",
        "prior_knowledge_bridge": "Prior knowledge bridge",
        "sequential_complexity": "Sequential complexity",
        "specificity_over_coverage": "Specificity over coverage",
        "reasoning_transparency": "Reasoning transparency",
        "schema_building_activation": "Schema-building activation",
    }
    
    for criterion in criteria_names:
        stats = criteria_stats[criterion]
        label = criterion_labels.get(criterion, criterion)
        lines.append(
            f"| {label} | {stats['avg']:.2f} | {stats['min']} | {stats['max']} |"
        )
    
    lines.extend([
        "",
        "---",
        "",
        "## Individual Unit Results",
        "",
    ])
    
    # Detail each unit
    for i, result in enumerate(results, 1):
        title = result.get("unit_title", result.get("input_title", f"Unit {i}"))
        total = result.get("total", 0)
        band = result.get("band", "Unknown")
        overall = result.get("overall", "No overall assessment provided.")
        scores = result.get("scores", {})
        
        lines.extend([
            f"### {i}. {title}",
            "",
            f"**Total Score:** {total}/12 — **{band}**",
            "",
            f"**Overall Assessment:** {overall}",
            "",
            "**Detailed Scores:**",
            "",
        ])
        
        for criterion in criteria_names:
            criterion_data = scores.get(criterion, {})
            score = criterion_data.get("score", 0)
            justification = criterion_data.get("justification", "No justification provided.")
            label = criterion_labels.get(criterion, criterion)
            lines.append(f"- **{label}:** {score}/2")
            lines.append(f"  - {justification}")
            lines.append("")
        
        if "file_path" in result:
            lines.append(f"**Source:** `{result['file_path']}`")
            lines.append("")
        
        lines.append("---")
        lines.append("")
    
    # Write report
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print(f"Input file: {INPUT_FILE}")
    print(f"Judge model: {MODEL_NAME}")
    print(f"Output directory: {OUTPUT_DIR}")
    print()
    
    # Load units
    units = load_units(INPUT_FILE)
    print(f"Loaded {len(units)} unit(s) for evaluation")
    print()
    
    # Set up GitHub Models client (OpenAI-compatible)
    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=GITHUB_TOKEN,
    )
    
    # Score each unit
    results = []
    for i, unit in enumerate(units, 1):
        title = unit.get("title", f"Unit {i}")
        print(f"[{i}/{len(units)}] Scoring: {title}")
        
        result = score_unit(client, unit)
        results.append(result)
        
        print(f"  → Score: {result['total']}/12 ({result['band']})")
        print()
    
    # Write report
    input_name = Path(INPUT_FILE).stem
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    report_path = Path(OUTPUT_DIR) / f"rubric-evaluation-{input_name}-{timestamp}.md"
    
    write_report(results, report_path)
    
    print(f"{'=' * 70}")
    print(f"Evaluation complete!")
    print(f"Report written to: {report_path}")
    print(f"{'=' * 70}")
    
    # Summary statistics
    avg_score = sum(r["total"] for r in results) / len(results) if results else 0
    print(f"\nAverage score: {avg_score:.1f}/12")
    
    band_counts = {}
    for r in results:
        band = r.get("band", "Unknown")
        band_counts[band] = band_counts.get(band, 0) + 1
    
    print("\nDistribution:")
    for band in ["Strong", "Acceptable", "Needs revision", "Failing"]:
        count = band_counts.get(band, 0)
        print(f"  {band}: {count}")


if __name__ == "__main__":
    main()
