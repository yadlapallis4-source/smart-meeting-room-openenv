from tasks.task_easy import grader as easy_grader
from tasks.task_medium import grader as medium_grader
from tasks.task_hard import grader as hard_grader


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

        if self.task_type == "easy":
            reward = easy_grader(action, self._state)
        elif self.task_type == "medium":
            reward = medium_grader(action, self._state)
        else:
            reward = hard_grader(action, self._state)

        done = True
        state = dict(self._state)
        state.pop("done", None)

        return state, float(reward), done, {}

    def state(self):
        return dict(self._state) if self._state is not None else None

    def get_tasks(self):
    return [
        {
            "id": "task_easy",
            "description": "Select room for 4 people",
            "difficulty": "easy",
            "grader": easy_grader,
        },
        {
            "id": "task_medium",
            "description": "Select room with projector",
            "difficulty": "medium",
            "grader": medium_grader,
        },
        {
            "id": "task_hard",
            "description": "Select optimal room",
            "difficulty": "hard",
            "grader": hard_grader,
        },
    ]
