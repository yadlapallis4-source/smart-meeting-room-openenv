from graders.grader_medium import grade

def grader(action, state):
    room = next((r for r in state.available_rooms if r.room_id == action.room_id), None)
    return grade(state.request, room)

def get_task():
    return {
        "task_id": "task_medium",
        "description": "Select a room that satisfies capacity and equipment requirements like projector.",
        "difficulty": "medium",
        "goal": "Choose a room that fits attendees and has required equipment.",
        "grader": grader,
    }
