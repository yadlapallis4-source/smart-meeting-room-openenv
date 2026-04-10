def get_task():
    return {
        "id": "task_medium",
        "description": "Select room with projector",
        "difficulty": "medium",
        "initial_state": {"capacity": 6, "projector": True},
        "action_space": ["A", "B"],
        "max_steps": 1,
    }


def grader(action, state):
    # correct answer = "B"
    if str(action).upper() == "B":
        return 0.7
    return 0.3
