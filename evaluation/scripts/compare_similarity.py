"""
Compare agent responses to ground truth using multiple similarity methods.

Reads a results JSONL file (query + response + ground_truth) and scores each
item using three independent methods:

    1. Cosine Similarity   – sentence-transformers embeddings
    2. Token F1 Score      – word-level precision/recall/F1
    3. BERTScore           – contextual token-level soft alignment

Each method produces a percentage (0–100%). A summary report is printed to
the console and saved as a JSONL file alongside the input.

Usage:
    python compare_similarity.py <results.jsonl> [--methods 1,2,3]
"""

import argparse
import json
import re
from pathlib import Path
from collections import Counter

# ---------------------------------------------------------------------------
# 1. Cosine Similarity (Sentence-Transformers)
# ---------------------------------------------------------------------------

def cosine_similarity_score(response: str, ground_truth: str, model=None) -> float:
    """
    Encode both texts with a sentence-transformer model and return
    cosine similarity as a percentage (0–100).

    Uses the 'all-MiniLM-L6-v2' model (~80 MB) for a good speed/quality
    trade-off.  The model object is passed in to avoid reloading per row.
    """
    from sentence_transformers import SentenceTransformer, util

    if model is None:
        model = SentenceTransformer("all-MiniLM-L6-v2")

    emb_response = model.encode(response, convert_to_tensor=True)
    emb_truth = model.encode(ground_truth, convert_to_tensor=True)
    similarity = util.cos_sim(emb_response, emb_truth).item()

    # Clamp to [0, 1] then convert to percentage
    return round(max(0.0, min(1.0, similarity)) * 100, 2)


def load_sentence_transformer_model():
    """Load the sentence-transformer model once for reuse across rows."""
    from sentence_transformers import SentenceTransformer

    print("  Loading sentence-transformer model (all-MiniLM-L6-v2)...")
    return SentenceTransformer("all-MiniLM-L6-v2")


# ---------------------------------------------------------------------------
# 2. Token-Level F1 Score
# ---------------------------------------------------------------------------

def _tokenize(text: str) -> list[str]:
    """Lowercase and split into alpha-numeric tokens."""
    return re.findall(r"\w+", text.lower())


def token_f1_score(response: str, ground_truth: str) -> float:
    """
    Compute word-level F1 between response and ground_truth.

    Returns a percentage (0–100).  Pure Python, no external dependencies.
    """
    response_tokens = _tokenize(response)
    truth_tokens = _tokenize(ground_truth)

    if not truth_tokens and not response_tokens:
        return 100.0
    if not truth_tokens or not response_tokens:
        return 0.0

    response_counts = Counter(response_tokens)
    truth_counts = Counter(truth_tokens)

    # Number of shared tokens (capped by min count for each word)
    common = sum((response_counts & truth_counts).values())

    precision = common / len(response_tokens) if response_tokens else 0.0
    recall = common / len(truth_tokens) if truth_tokens else 0.0

    if precision + recall == 0:
        return 0.0

    f1 = 2 * precision * recall / (precision + recall)
    return round(f1 * 100, 2)


# ---------------------------------------------------------------------------
# 3. BERTScore
# ---------------------------------------------------------------------------

def bert_score_f1(response: str, ground_truth: str, scorer=None) -> float:
    """
    Compute BERTScore F1 between response and ground_truth.

    Returns a percentage (0–100).
    The scorer object is passed in to avoid reloading the model per row.
    """
    if scorer is None:
        scorer = load_bert_scorer()

    P, R, F1 = scorer.score([response], [ground_truth])
    return round(F1.item() * 100, 2)


def load_bert_scorer():
    """Load the BERTScore scorer once for reuse across rows."""
    from bert_score import BERTScorer

    print("  Loading BERTScore model (roberta-large)...")
    return BERTScorer(model_type="roberta-large", lang="en", rescale_with_baseline=True)

# ---------------------------------------------------------------------------
# Data I/O
# ---------------------------------------------------------------------------

def load_results(path: str) -> list[dict]:
    """Load a JSONL file into a list of dicts."""
    items = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items


def save_results(records: list[dict], output_path: str) -> None:
    """Write a list of dicts as JSONL."""
    with open(output_path, "w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"\nDetailed results saved to: {output_path}")


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def print_summary(records: list[dict], methods: list[int]) -> None:
    """Print a formatted summary table to the console."""
    method_labels = {
        1: "Cosine Sim",
        2: "Token F1",
        3: "BERTScore",
    }
    method_keys = {
        1: "cosine_similarity",
        2: "token_f1",
        3: "bert_score_f1",
    }

    # ---- Per-row table ----
    header_parts = ["#", "Query (first 60 chars)"]
    for m in methods:
        header_parts.append(method_labels[m])
    header = " | ".join(header_parts)
    separator = " | ".join(["-" * len(p) for p in header_parts])

    print("\n" + "=" * 80)
    print("SIMILARITY SCORES  (0–100 %)")
    print("=" * 80)
    print(header)
    print(separator)

    for i, rec in enumerate(records, 1):
        row_parts = [str(i).rjust(2), rec["query"][:60].ljust(60)]
        for m in methods:
            val = rec.get(method_keys[m], "N/A")
            if isinstance(val, (int, float)):
                row_parts.append(f"{val:6.1f}%")
            else:
                row_parts.append(str(val)[:8])
        print(" | ".join(row_parts))

    # ---- Averages ----
    print("-" * 80)
    avg_parts = ["  ", "AVERAGE".ljust(60)]
    for m in methods:
        values = [r[method_keys[m]] for r in records if isinstance(r.get(method_keys[m]), (int, float))]
        if values:
            avg_parts.append(f"{sum(values) / len(values):6.1f}%")
        else:
            avg_parts.append("  N/A ")
    print(" | ".join(avg_parts))
    print("=" * 80)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare response vs ground_truth with multiple similarity methods.",
    )
    parser.add_argument(
        "results_file",
        help="Path to the JSONL file with 'response' and 'ground_truth' fields.",
    )
    parser.add_argument(
        "--methods",
        default="1,2,3",
        help="Comma-separated list of methods to run (default: 1,2,3). "
             "1=Cosine, 2=Token-F1, 3=BERTScore.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    methods = [int(m.strip()) for m in args.methods.split(",")]
    results_path = args.results_file

    print(f"Input file : {results_path}")
    print(f"Methods    : {methods}")

    records = load_results(results_path)
    print(f"Rows loaded: {len(records)}\n")

    # -- Pre-load heavy models once ----------------------------------------
    st_model = None
    bert_scorer = None

    if 1 in methods:
        st_model = load_sentence_transformer_model()

    if 3 in methods:
        bert_scorer = load_bert_scorer()

    # -- Score each row -----------------------------------------------------
    for i, item in enumerate(records, 1):
        response = item["response"]
        ground_truth = item["ground_truth"]
        print(f"  [{i}/{len(records)}] {item['query'][:70]}...")

        if 1 in methods:
            item["cosine_similarity"] = cosine_similarity_score(response, ground_truth, model=st_model)

        if 2 in methods:
            item["token_f1"] = token_f1_score(response, ground_truth)

        if 3 in methods:
            item["bert_score_f1"] = bert_score_f1(response, ground_truth, scorer=bert_scorer)

    # -- Output results -----------------------------------------------------
    print_summary(records, methods)

    output_path = str(Path(results_path).with_suffix("")) + "-similarity.jsonl"
    save_results(records, output_path)


if __name__ == "__main__":
    main()
