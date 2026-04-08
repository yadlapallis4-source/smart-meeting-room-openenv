from graders.grader_easy import grade

def grader(action, state):
    room = next((r for r in state.available_rooms if r.room_id == action.room_id), None)
    return grade(state.request, room)

def get_task():
    return {
        "task_id": "task_easy",
        "description": "Select a room that fits the number of attendees without unnecessary resource usage.",
        "difficulty": "easy",
        "goal": "Choose the most appropriate room based only on capacity.",
        "grader": grader,
    }
