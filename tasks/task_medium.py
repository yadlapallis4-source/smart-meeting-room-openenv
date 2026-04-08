def grader(action, state):
    if action == "select_room_B":
        return 0.75
    elif action == "select_room_A":
        return 0.4
    else:
        return 0.25
