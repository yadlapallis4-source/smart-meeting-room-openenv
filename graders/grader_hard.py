def grade(request, room):
    if room is None:
        return 0.0

    if room.capacity < request.attendees:
        return 0.0

    if request.needs_projector and not room.has_projector:
        return 0.0

    if request.needs_video_conference and not room.has_video_conference:
        return 0.0

    if request.accessibility_required and not room.accessible:
        return 0.0

    score = 0.5

    # capacity efficiency
    diff = room.capacity - request.attendees
    if diff == 0:
        score += 0.2
    elif diff <= 2:
        score += 0.1

    # building preference
    if request.preferred_building:
        if room.building == request.preferred_building:
            score += 0.1

    # floor preference
    if request.preferred_floor:
        if room.floor == request.preferred_floor:
            score += 0.1

    # VIP prefers premium
    if request.vip_meeting and room.priority_level == "premium":
        score += 0.1

    return min(score, 1.0)

def grader(action, state):
    room = next((r for r in state.available_rooms if r.room_id == action.room_id), None)
    return float(grade(state.request, room))
