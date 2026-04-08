def get_task():
    return {
        "id": "task_hard",
        "difficulty": "hard",
        "description": "Select a room based on multiple constraints",
        "initial_state": {
            "attendees": 8,
            "needs_projector": True
        }
    }

def grader(action, state):
    return 1.0
