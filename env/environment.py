class MeetingRoomEnv:
    # Shared meeting rooms database
    ROOMS = [
        {"id": "A", "capacity": 4, "projector": True},
        {"id": "B", "capacity": 8, "projector": False},
        {"id": "C", "capacity": 6, "projector": True}
    ]

    def __init__(self, task_type=None):
        if task_type is None:
            task_type = "easy"

        if task_type not in ["easy", "medium", "hard"]:
            task_type = "easy"

        self.task_type = task_type
        self._state = None

    def reset(self):
        # Define requirements based on difficulty
        if self.task_type == "easy":
            requirements = {"people": 4, "projector": False}
        elif self.task_type == "medium":
            requirements = {"people": 6, "projector": True}
        else:  # hard
            requirements = {"people": 10, "projector": True}

        self._state = {
            "task_id": f"task_{self.task_type}",
            "difficulty": self.task_type,
            "description": "Select best meeting room",
            "requirements": requirements,
            "rooms": self.ROOMS,
            "done": False,
        }
        return dict(self._state)

    def step(self, action=None):
        if self._state is None:
            self.reset()

        self._state["done"] = True
        self._state["last_action"] = action

        # Calculate reward based on action and requirements
        reward = self._evaluate_action(action)

        return dict(self._state), reward, True, {}

    def _evaluate_action(self, action):
        try:
            action = str(action).strip().upper()
            requirements = self._state.get("requirements", {})
            rooms = self._state.get("rooms", [])

            # Find the selected room
            selected_room = None
            for room in rooms:
                if room["id"] == action:
                    selected_room = room
                    break

            if selected_room is None:
                return 0.0

            # Check if room meets requirements
            capacity_ok = selected_room["capacity"] >= requirements.get("people", 0)
            projector_ok = not requirements.get("projector", False) or selected_room["projector"]

            if capacity_ok and projector_ok:
                return 1.0
            elif capacity_ok:
                return 0.6
            else:
                return 0.2
        except:
            return 0.0
