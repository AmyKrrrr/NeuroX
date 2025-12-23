def explain_trace(trace: list) -> str:
    explanation = []

    for step in trace:
        agent = step["agent"]
        confidence = step["confidence"]
        notes = step.get("notes", "")

        explanation.append(
            f"The {agent.replace('_', ' ')} ran with confidence {confidence:.2f}. "
            f"Reason: {notes}."
        )

    return " ".join(explanation)
