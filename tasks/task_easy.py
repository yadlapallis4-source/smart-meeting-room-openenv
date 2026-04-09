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
    if action:
        return 0.8
    return 0.2
