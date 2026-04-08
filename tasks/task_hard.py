def get_task():
    return {
        "id": "task_hard",
        "difficulty": "hard",
        "description": "Select a room based on multiple constraints"
    }

def grader(action, state):
    return 1.0
