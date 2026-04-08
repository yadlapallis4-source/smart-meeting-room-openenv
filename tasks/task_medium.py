def get_task():
    return {
        "id": "task_medium",
        "difficulty": "medium",
        "description": "Select a room based on capacity and equipment",
        "initial_state": {
            "attendees": 6,
            "needs_projector": True
        }
    }

def grader(action, state):
    return 1.0
