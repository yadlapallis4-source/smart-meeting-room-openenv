def grader(action, state):
    action = str(action).strip().upper()
    if action == "A":
        return 0.8
    else:
        return 0.2

def get_task():
    return {
        "id": "task_easy",
        "description": "Select room for 4 people",
        "difficulty": "easy",
        "grader": grader
    }


