from typing import Tuple, Dict, Any
from .models import Observation, Action, State
from .data import get_rooms, get_easy_request, get_medium_request, get_hard_request


class SmartMeetingEnv:
    def __init__(self, task_type: str = "easy"):
        self.task_type = task_type
        self.state_obj: State = None

    # -----------------------
    # RESET
    # -----------------------
    def reset(self) -> Observation:
        rooms = get_rooms()

        if self.task_type == "easy":
            request = get_easy_request()
        elif self.task_type == "medium":
            request = get_medium_request()
        else:
            request = get_hard_request()

        task_id = self.task_type
        difficulty = task_id.split("_")[1] if "_" in task_id else task_id
        
        self.state_obj = State(
            task_id=request.request_id,
            difficulty=difficulty,
            request=request,
            available_rooms=rooms,
            step_count=0,
            max_steps=1,  # single-step env
            selected_room_id=None,
            booking_confirmed=False,
            last_reward=0.0,
            done=False,
        )

        return self._build_observation("Select the best room for this request.")

    # -----------------------
    # STEP
    # -----------------------
    def step(self, action: Action) -> Tuple[Observation, float, bool, Dict[str, Any]]:
        if self.state_obj.done:
            return self._build_observation("Episode already finished."), 0.0, True, {}

        self.state_obj.step_count += 1

        selected_room = self._find_room(action.room_id)

        reward = self._calculate_reward(selected_room)

        self.state_obj.selected_room_id = action.room_id
        self.state_obj.booking_confirmed = action.confirm
        self.state_obj.last_reward = reward
        self.state_obj.done = True  # single-step episode

        observation = self._build_observation("Booking evaluated.")

        return observation, reward, True, {}

    # -----------------------
    # STATE
    # -----------------------
    def state(self) -> State:
        return self.state_obj

    # -----------------------
    # TASKS
    # -----------------------
    def get_tasks(self):
    return [
        {
            "id": "task_easy",
            "difficulty": "easy",
            "description": "Simple task"
        },
        {
            "id": "task_medium",
            "difficulty": "medium",
            "description": "Simple task"
        },
        {
            "id": "task_hard",
            "difficulty": "hard",
            "description": "Simple task"
        }
    ]

    # -----------------------
    # HELPERS
    # -----------------------
    def _find_room(self, room_id: str):
        for room in self.state_obj.available_rooms:
            if room.room_id == room_id:
                return room
        return None

    def _calculate_reward(self, room) -> float:
        req = self.state_obj.request

        if room is None:
            return -0.2  # invalid room

        # basic constraints
        if room.capacity < req.attendees:
            return 0.0

        if req.needs_projector and not room.has_projector:
            return 0.2

        if req.needs_video_conference and not room.has_video_conference:
            return 0.2

        if req.accessibility_required and not room.accessible:
            return 0.0

        # preference scoring
        score = 0.5

        # better capacity fit (avoid waste)
        capacity_diff = room.capacity - req.attendees
        if capacity_diff == 0:
            score += 0.3
        elif capacity_diff <= 2:
            score += 0.2
        else:
            score += 0.1

        # preferred building
        if req.preferred_building and room.building == req.preferred_building:
            score += 0.1

        # preferred floor
        if req.preferred_floor and room.floor == req.preferred_floor:
            score += 0.1

        # VIP prefers premium
        if req.vip_meeting and room.priority_level == "premium":
            score += 0.1

        return min(score, 1.0)

    def _build_observation(self, message: str) -> Observation:
        return Observation(
            task_id=self.state_obj.task_id,
            difficulty=self.state_obj.difficulty,
            request=self.state_obj.request,
            available_rooms=self.state_obj.available_rooms,
            step_count=self.state_obj.step_count,
            max_steps=self.state_obj.max_steps,
            message=message,
            last_reward=self.state_obj.last_reward,
            done=self.state_obj.done,
        )
