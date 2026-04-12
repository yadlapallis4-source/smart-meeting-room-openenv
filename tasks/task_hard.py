def grader(action, state) -> float:
    try:
        action = str(action).strip().upper()

        attendees = state.get("attendees", 0)
        needs_projector = state.get("projector", False)

        if action == "C" and attendees >= 5 and needs_projector:
            raw_score = 0.75
        elif action == "B":
            raw_score = 0.5
        else:
            raw_score = 0.2
    except:
        raw_score = 0.0

    final_score = max(0.01, min(0.99, float(raw_score)))
    return final_score


def get_task():
    return {
        "task_id": "T3",
        "description": "Select best room with all constraints",
        "grader": grader
    }


