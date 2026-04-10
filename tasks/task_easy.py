def grader(action, state):
    action = str(action).strip().upper()
    if action == "A":
        return 0.8
    return 0.3


def get_task():
    return {
        "task_id": "T1",
        "description": "Select the best meeting room",
        "grader": grader
    }


