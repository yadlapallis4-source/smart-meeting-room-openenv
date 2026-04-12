def grader(state, action, reward, next_state):
    try:
        action = str(action).strip().upper()

        # Example logic using state
        attendees = state.get("attendees", 0)

        if action == "A" and attendees <= 4:
            raw_score = 0.85
        elif action == "B":
            raw_score = 0.5
        else:
            raw_score = 0.25
    except:
        raw_score = 0.0

    final_score = max(0.01, min(0.99, float(raw_score)))
    return final_score


def get_task():
    return {
        "task_id": "T1",
        "description": "Select the best meeting room",
        "grader": grader
    }


