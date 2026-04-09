def get_task():
    return {
        "id": "task_easy",
        "description": "Select room for 4 people",
        "difficulty": "easy",
        "initial_state": {"capacity": 4},
        "action_space": ["A", "B"],
        "max_steps": 1,
    }


def grader(action, state):
    if action == "A":
        return 0.6
    elif action == "B":
        return 0.3
    return 0.2
