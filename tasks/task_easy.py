def get_task():
    return {
        "id": "task_easy",
        "description": "Select correct room for 4 people",
        "difficulty": "easy",
        "initial_state": {"capacity": 4},
        "action_space": ["select_room_A", "select_room_B"],
        "max_steps": 1,
    }


def grader(action, state):
    if action == "select_room_A":
        return 0.6
    elif action == "select_room_B":
        return 0.3
    return 0.2
