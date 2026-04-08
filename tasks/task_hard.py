def get_task():
    return {
        "id": "task_hard",
        "difficulty": "hard",
        "description": "Simple task",
        "initial_state": {},
        "action_space": ["noop()"],
        "max_steps": 1,
    }


def grader(action, state):
    return 0.7
