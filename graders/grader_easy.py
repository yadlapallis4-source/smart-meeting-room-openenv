def grade(request, room):
    # invalid case
    if room is None:
        return 0.0

    # must satisfy capacity
    if room.capacity < request.attendees:
        return 0.0

    # best = minimum sufficient capacity
    diff = room.capacity - request.attendees

    if diff == 0:
        return 1.0
    elif diff <= 2:
        return 0.8
    else:
        return 0.6

def grader(action, state):
    room = next((r for r in state.available_rooms if r.room_id == action.room_id), None)
    return float(grade(state.request, room))
