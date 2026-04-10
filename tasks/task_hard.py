def grader(action, state):
    action = str(action).strip().upper()
    if action == "A":
        return 0.6
    return 0.4


