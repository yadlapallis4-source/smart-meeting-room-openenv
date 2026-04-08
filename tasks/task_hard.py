def grader(action, state):
    if action == "select_room_B":
        return 0.9
    elif action == "select_room_A":
        return 0.5
    else:
        return 0.3
