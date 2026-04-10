def grader(action, state):
    action = str(action).strip().upper()
    needs_projector = state.get("projector", False)

    if action == "B" and needs_projector:
        return 0.8
    elif action == "A":
        return 0.55
    else:
        return 0.35


def get_task():
    return {
        "id": "task_medium",
        "description": "Select optimal room with projector",
        "grader": grader
    }