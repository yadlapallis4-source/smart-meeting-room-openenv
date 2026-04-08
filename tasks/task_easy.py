def get_task():
    return {
        "id": "task_easy",
        "difficulty": "easy",
        "description": "Select a room based on capacity",
        "initial_state": {
            "attendees": 4,
            "needs_projector": True
        }
    }

def grader(action, state):
    return 1.0
