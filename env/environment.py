from tasks.task_easy import grader as easy_grader
from tasks.task_medium import grader as medium_grader
from tasks.task_hard import grader as hard_grader


class MeetingRoomEnv:

    def __init__(self, task_type="easy"):
        if task_type not in ["easy", "medium", "hard"]:
            task_type = "easy"

        self.task_type = task_type
        self._state = None

    # -------------------------
    # RESET ENVIRONMENT
    # -------------------------
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

    # -------------------------
    # STEP FUNCTION (IMPORTANT)
    # -------------------------
    def step(self, action=None):

        if self._state is None:
            self.reset()

        self._state["step_count"] += 1
        self._state["last_action"] = action

        # 🔥 REAL GRADING LOGIC (CRITICAL FIX)
        if self.task_type == "easy":
            reward = easy_grader(action, self._state)

        elif self.task_type == "medium":
            reward = medium_grader(action, self._state)

        else:
            reward = hard_grader(action, self._state)

        # Mark done
        done = True
        self._state["done"] = done

        return dict(self._state), reward, done, {}

    # -------------------------
    # GET CURRENT STATE
    # -------------------------
    def state(self):
        return dict(self._state) if self._state is not None else None

    # -------------------------
    # DEFINE TASKS (CRITICAL)
    # -------------------------
    def get_tasks(self):
        return [
            {
                "id": "task_easy",
                "description": "Select correct room for 4 people",
                "difficulty": "easy",
                "grader": easy_grader,
            },
            {
                "id": "task_medium",
                "description": "Select room with projector for 6 people",
                "difficulty": "medium",
                "grader": medium_grader,
            },
            {
                "id": "task_hard",
                "description": "Select best room with constraints (capacity + projector + time)",
                "difficulty": "hard",
                "grader": hard_grader,
            },
        ]
