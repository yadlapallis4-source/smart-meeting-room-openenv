from graders.grader_easy import grade

def get_task():
    return {
        "task_id": "task_easy",
        "description": "Select a room that fits the number of attendees without unnecessary resource usage.",
        "difficulty": "easy",
        "goal": "Choose the most appropriate room based only on capacity.",
        "grader": grade,
    }
