def get_task():
    return {
        "id": "task_hard",
        "difficulty": "hard",
        "description": "Select best room considering capacity, projector, and time slot",
        "initial_state": {"capacity": 10, "projector": True, "time": "10AM"},
        "action_space": ["select_room_A", "select_room_B"],
        "max_steps": 1,
    }


def grader(action, state):
    if action == "select_room_B":
        return 0.85
    else:
        return 0.5
