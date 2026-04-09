def get_task():
    return {
        "id": "task_medium",
        "description": "Select room with projector",
        "difficulty": "medium",
        "initial_state": {"capacity": 6, "projector": True},
        "action_space": ["A", "B"],
        "max_steps": 1,
    }


def grader(action, state):
    if action == "B":
        return 0.75
    elif action == "A":
        return 0.4
    return 0.25
