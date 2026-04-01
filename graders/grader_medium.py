def grade(request, room):
    if room is None:
        return 0.0

    if room.capacity < request.attendees:
        return 0.0

    if request.needs_projector and not room.has_projector:
        return 0.0

    score = 0.6

    # capacity efficiency
    diff = room.capacity - request.attendees
    if diff == 0:
        score += 0.2
    elif diff <= 2:
        score += 0.1

    # building preference
    if request.preferred_building:
        if room.building == request.preferred_building:
            score += 0.2

    return min(score, 1.0)
