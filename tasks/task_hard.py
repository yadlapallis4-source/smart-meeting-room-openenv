def grader(action, state):
    action = str(action).strip().upper()

    attendees = state.get("attendees", 0)
    needs_projector = state.get("projector", False)

    if action == "C" and attendees >= 5 and needs_projector:
        return 0.75
    elif action == "B":
        return 0.5
    else:
        return 0.2


def get_task():
    return {
        "task_id": "T3",
        "description": "Select best room with all constraints",
        "grader": grader
    }


