def get_task():
    return {
        "id": "task_medium",
        "difficulty": "medium",
        "description": "Select a meeting room with projector for 6 people",
        "initial_state": {"capacity": 6, "projector": True},
        "action_space": ["select_room_A", "select_room_B"],
        "max_steps": 1,
    }


def grader(action, state):
    if action == "select_room_B":
        return 0.75
    else:
        return 0.4
