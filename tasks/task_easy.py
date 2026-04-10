def grader(action, state):
    """Easy: Check if room capacity meets requirement (no projector needed)"""
    try:
        action = str(action).strip().upper()
        rooms = state.get("rooms", [])
        req = state.get("requirements", {})

        for room in rooms:
            if room["id"] == action:
                # Easy: only check capacity
                if room["capacity"] >= req.get("people", 0):
                    return 1.0
                else:
                    return 0.2
        return 0.0
    except:
        return 0.0

def get_task():
    return {
        "id": "task_easy",
        "description": "Select room with sufficient capacity (4+ people)",
        "difficulty": "easy",
        "grader": grader
    }


