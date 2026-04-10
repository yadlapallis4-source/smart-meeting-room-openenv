def grader(action, state):
    action = str(action).strip().upper()
    if action == "C":
        return 0.6
    return 0.5


def get_task():
    return {
        "task_id": "T3",
        "description": "Select best room with all constraints",
        "grader": grader
    }


