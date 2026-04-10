def grader(action, state):
    action = str(action).strip().upper()
    if action == "A":
        return 0.8
    return 0.2


