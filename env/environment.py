from tasks.task_easy import grader as easy_grader
from tasks.task_medium import grader as medium_grader
from tasks.task_hard import grader as hard_grader


class MeetingRoomEnv:

    def __init__(self, task_type="easy"):
        if task_type not in ["easy", "medium", "hard"]:
            task_type = "easy"
        self.task_type = task_type
        self._state = None

    def reset(self):
        self._state = {
            "task_id": f"task_{self.task_type}",
            "difficulty": self.task_type,
            "description": "Simple",
            "step_count": 0,
            "max_steps": 1,
            "done": False,
        }
        return dict(self._state)

    def step(self, action=None):
        if self._state is None:
            self.reset()

        self._state["step_count"] = min(self._state["step_count"] + 1, 1)
        self._state["last_action"] = action
        self._state["done"] = True

        return dict(self._state), 0.8, True, {}

    def state(self):
        return dict(self._state) if self._state is not None else None

    def get_tasks(self):
        return {
            "task_easy": {
                "id": "task_easy",
                "description": "Simple",
                "difficulty": "easy",
                "grader": easy_grader,
            },
            "task_medium": {
                "id": "task_medium",
                "description": "Simple",
                "difficulty": "medium",
                "grader": medium_grader,
            },
            "task_hard": {
                "id": "task_hard",
                "description": "Simple",
                "difficulty": "hard",
                "grader": hard_grader,
            },
        }
