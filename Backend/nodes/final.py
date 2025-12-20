# app/nodes/final.py

def final_node(state: dict) -> dict:
    """
    Final presentation node.
    Exposes both the report and bias scores to the user.
    """

    state["output"] = {
        "report": state.get("final_report", ""),
        "bias_scores": state.get("bias_scores", [])
    }

    return state
