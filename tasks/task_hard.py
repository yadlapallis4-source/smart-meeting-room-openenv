def grader(action, state):
    """Hard: Pick the smallest room that satisfies all requirements (optimization)"""
    try:
        action = str(action).strip().upper()
        rooms = state.get("rooms", [])
        req = state.get("requirements", {})

        # Find all rooms that meet requirements
        candidates = []
        for room in rooms:
            capacity_ok = room["capacity"] >= req.get("people", 0)
            projector_ok = not req.get("projector", False) or room["projector"]
            if capacity_ok and projector_ok:
                candidates.append(room)

        if not candidates:
            # No perfect match available
            for room in rooms:
                if room["id"] == action:
                    if room["capacity"] >= req.get("people", 0):
                        return 0.5
                    else:
                        return 0.1
            return 0.0

        # Find the optimal (smallest) room
        optimal = min(candidates, key=lambda r: r["capacity"])

        if action == optimal["id"]:
            return 1.0
        else:
            # Selected a valid room but not optimal
            selected = next((r for r in candidates if r["id"] == action), None)
            if selected:
                return 0.7
            return 0.0
    except:
        return 0.0

def get_task():
    return {
        "id": "task_hard",
        "description": "Select the smallest room that meets capacity and projector requirements (10+ people, projector)",
        "difficulty": "hard",
        "grader": grader
    }


