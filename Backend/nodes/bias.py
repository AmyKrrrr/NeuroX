# app/nodes/bias.py
from app.services.bias_client import detect_bias

MAX_BIAS_CHARS = 1000  # ✅ key fix

def bias_node(state: dict) -> dict:
    """
    Detects bias in raw scraped documents
    """

    documents = state.get("documents", [])
    bias_results = []

    for idx, doc in enumerate(documents, start=1):
        if not doc.strip():
            continue

        snippet = doc[:MAX_BIAS_CHARS]  # ✅ truncate here
        result = detect_bias(snippet)

        bias_results.append({
            "source": f"Source {idx}",
            "label": result["label"],
            "confidence": result["confidence"],
            "bias_score": result["bias_score"],
            "has_bias": result["has_bias"]
        })

    state["bias_scores"] = bias_results
    return state
