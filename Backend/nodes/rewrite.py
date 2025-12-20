from app.services.llm import summarize_and_rewrite

def rewrite_node(state: dict) -> dict:
    """
    Generates the final neutral report from raw documents.
    """

    documents = state.get("documents", [])
    combined_text = "\n\n".join(documents)

    if not combined_text.strip():
        state["final_report"] = ""
        return state

    final_report = summarize_and_rewrite(combined_text)
    state["final_report"] = final_report
    return state
