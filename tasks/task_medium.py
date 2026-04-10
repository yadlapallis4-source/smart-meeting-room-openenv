def grader(action, state):
    """Medium: Check capacity AND projector availability"""
    try:
        action = str(action).strip().upper()
        rooms = state.get("rooms", [])
        req = state.get("requirements", {})

        for room in rooms:
            if room["id"] == action:
                capacity_ok = room["capacity"] >= req.get("people", 0)
                projector_ok = not req.get("projector", False) or room["projector"]

                if capacity_ok and projector_ok:
                    return 1.0
                elif capacity_ok:
                    return 0.6
                else:
                    return 0.2
        return 0.0
    except:
        return 0.0

def get_task():
    return {
        "id": "task_medium",
        "description": "Select room with projector and sufficient capacity (6+ people)",
        "difficulty": "medium",
        "grader": grader
    }


