def grader(action, state):
    if action == "select_room_A":
        return 0.6
    elif action == "select_room_B":
        return 0.3
    else:
        return 0.2
