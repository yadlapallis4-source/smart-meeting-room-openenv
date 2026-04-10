
class MeetingRoomEnv:
    def __init__(self, task_type=None):
        if task_type is None:
            task_type = "easy"

        if task_type not in ["easy", "medium", "hard"]:
            task_type = "easy"

        self.task_type = task_type
        self._state = None

    def reset(self):
        self._state = {
            "task_id": f"task_{self.task_type}",
            "difficulty": self.task_type,
            "description": "Meeting room selection task",
            "step_count": 0,
            "max_steps": 1,
            "done": False,
        }
        return dict(self._state)

    def step(self, action=None):
        if self._state is None:
            self.reset()

        self._state["step_count"] += 1
        self._state["last_action"] = action
        self._state["done"] = True

        return dict(self._state), 0.5, True, {}
