def grader(action, state):
    action = str(action).strip().upper()
    if action == "A":
        return 0.6
    else:
        return 0.4

def get_task():
    return {
        "id": "task_hard",
        "description": "Select optimal room",
        "difficulty": "hard",
        "grader": grader
    }


