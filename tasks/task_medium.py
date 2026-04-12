def grader(state, action, reward, next_state):
    try:
        action = str(action).strip().upper()
        needs_projector = state.get("projector", False)

        if action == "B" and needs_projector:
            raw_score = 0.8
        elif action == "A":
            raw_score = 0.55
        else:
            raw_score = 0.35
    except:
        raw_score = 0.0

    final_score = max(0.01, min(0.99, float(raw_score)))
    return final_score


def get_task():
    return {
        "id": "task_medium",
        "description": "Select optimal room with projector",
        "grader": grader
    }