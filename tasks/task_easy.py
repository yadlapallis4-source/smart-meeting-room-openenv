def grader(action, state):
    action = str(action).strip().upper()

    # Example logic using state
    attendees = state.get("attendees", 0)

    if action == "A" and attendees <= 4:
        return 0.85
    elif action == "B":
        return 0.5
    else:
        return 0.25


def get_task():
    return {
        "task_id": "T1",
        "description": "Select the best meeting room",
        "grader": grader
    }


