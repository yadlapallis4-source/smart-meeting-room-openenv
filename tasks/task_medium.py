def get_task():
    return {
        "id": "task_medium",
        "difficulty": "medium",
        "description": "Select a room based on capacity and equipment"
    }

def grader(action, state):
    return 1.0
