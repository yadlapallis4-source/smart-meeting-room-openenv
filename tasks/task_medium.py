def get_task():
    return {
        "id": "task_medium",
        "description": "Select room with projector",
        "difficulty": "medium",
        "initial_state": {"capacity": 6, "projector": True},
        "action_space": ["A", "B"],
        "max_steps": 1,
    }


