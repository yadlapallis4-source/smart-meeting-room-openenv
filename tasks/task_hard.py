def get_task():
    return {
        "id": "task_hard",
        "description": "Select optimal room with constraints",
        "difficulty": "hard",
        "initial_state": {"capacity": 10, "projector": True, "time": "10AM"},
        "action_space": ["A", "B"],
        "max_steps": 1,
    }
