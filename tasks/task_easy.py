def get_task():
    return {
        "id": "task_easy",
        "difficulty": "easy",
        "description": "Select the correct meeting room for 4 people",
        "initial_state": {"capacity": 4},
        "action_space": ["select_room_A", "select_room_B"],
        "max_steps": 1,
    }


def grader(action, state):
    if action == "select_room_A":
        return 0.7
    else:
        return 0.3
