def grader(action, state):
    action = str(action).strip().upper()
    if action == "B":
        return 0.7
    else:
        return 0.3


