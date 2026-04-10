def grader(action, state):
    action = str(action).strip().upper()
    if action == "B":
        return 0.7
    return 0.4


def get_task():
    return {
        "task_id": "T2",
        "description": "Select optimal room with projector",
        "grader": grader
    }


