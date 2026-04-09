def get_task():
    return {
        "id": "task_hard",
        "description": "Select best room with constraints",
        "difficulty": "hard",
        "initial_state": {"capacity": 10, "projector": True},
        "action_space": ["select_room_A", "select_room_B"],
        "max_steps": 1,
    }


def grader(action, state):
    if action == "select_room_B":
        return 0.9
    elif action == "select_room_A":
        return 0.5
    return 0.3
