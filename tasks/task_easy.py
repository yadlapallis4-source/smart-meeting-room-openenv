def grader(action, state):
    action = str(action).strip().upper()
    if action == "A":
        return 0.8
    else:
        return 0.2


