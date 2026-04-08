def get_task():
    return {
        "id": "task_easy",
        "difficulty": "easy",
        "description": "Select a room based on capacity"
    }

def grader(action, state):
    return 1.0
