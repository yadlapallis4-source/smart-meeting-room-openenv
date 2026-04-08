def get_task():
    return {
        "id": "task_medium",
        "difficulty": "medium",
        "description": "Select a room based on capacity and equipment",
        "initial_state": {
            "attendees": 6,
            "needs_projector": True
        },
        "action_space": [
            "select_room('R1')",
            "select_room('R2')"
        ],
        "max_steps": 1
    }

def grader(action, state):
    return 1.0
