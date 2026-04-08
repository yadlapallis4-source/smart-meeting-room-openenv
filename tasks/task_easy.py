def get_task():
    return {
        "id": "task_easy",
        "difficulty": "easy",
        "description": "Simple",
        "initial_state": {},
        "action_space": ["noop()"],
        "max_steps": 1
    }


def grader(action, state):
    return 1.0
