from graders.grader_hard import grade

def get_task():
    return {
        "task_id": "task_hard",
        "description": "Select the best room considering multiple constraints such as capacity, equipment, accessibility, and preferences.",
        "difficulty": "hard",
        "goal": "Choose the most optimal room satisfying all constraints and preferences.",
        "grader": grade,
    }
