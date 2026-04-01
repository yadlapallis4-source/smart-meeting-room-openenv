from typing import List, Literal, Optional
from pydantic import BaseModel, Field


class Room(BaseModel):
    room_id: str = Field(..., description="Unique room identifier")
    name: str = Field(..., description="Human-readable room name")
    capacity: int = Field(..., ge=1, description="Maximum number of attendees")
    building: str = Field(..., description="Building where the room is located")
    floor: int = Field(..., description="Floor number")
    has_projector: bool = Field(..., description="Whether the room has a projector")
    has_video_conference: bool = Field(
        ..., description="Whether the room supports video conferencing"
    )
    accessible: bool = Field(
        ..., description="Whether the room is wheelchair accessible"
    )
    priority_level: Literal["standard", "premium"] = Field(
        ..., description="Room priority category"
    )


class BookingRequest(BaseModel):
    request_id: str = Field(..., description="Unique booking request identifier")
    team_name: str = Field(..., description="Team requesting the room")
    attendees: int = Field(..., ge=1, description="Number of attendees")
    duration_minutes: int = Field(..., ge=15, description="Meeting duration in minutes")
    needs_projector: bool = Field(..., description="Whether projector is required")
    needs_video_conference: bool = Field(
        ..., description="Whether video conferencing is required"
    )
    accessibility_required: bool = Field(
        ..., description="Whether accessibility is required"
    )
    preferred_building: Optional[str] = Field(
        default=None,
        description="Preferred building, if any",
    )
    preferred_floor: Optional[int] = Field(
        default=None,
        description="Preferred floor, if any",
    )
    urgency: Literal["low", "medium", "high"] = Field(
        ..., description="Urgency level of the booking"
    )
    vip_meeting: bool = Field(
        ..., description="Whether this is a VIP or leadership meeting"
    )


class Action(BaseModel):
    room_id: str = Field(..., description="Chosen room ID")
    confirm: bool = Field(
        default=True,
        description="Whether the agent wants to finalize the booking",
    )
    reasoning_note: Optional[str] = Field(
        default=None,
        description="Optional short explanation for why this room was selected",
    )


class Observation(BaseModel):
    task_id: str = Field(..., description="Current task identifier")
    difficulty: Literal["easy", "medium", "hard"] = Field(
        ..., description="Task difficulty level"
    )
    request: BookingRequest = Field(..., description="Current booking request")
    available_rooms: List[Room] = Field(
        ..., description="Rooms currently available for selection"
    )
    step_count: int = Field(..., ge=0, description="Current step count")
    max_steps: int = Field(..., ge=1, description="Maximum allowed steps")
    message: str = Field(..., description="Instruction or feedback message")
    last_reward: float = Field(
        default=0.0,
        description="Reward obtained from the previous action",
    )
    done: bool = Field(default=False, description="Whether the episode is complete")


class State(BaseModel):
    task_id: str = Field(..., description="Current task identifier")
    difficulty: Literal["easy", "medium", "hard"] = Field(
        ..., description="Task difficulty level"
    )
    request: BookingRequest = Field(..., description="Current booking request")
    available_rooms: List[Room] = Field(
        ..., description="Rooms available in this episode"
    )
    step_count: int = Field(..., ge=0, description="Number of steps taken so far")
    max_steps: int = Field(..., ge=1, description="Maximum steps allowed")
    selected_room_id: Optional[str] = Field(
        default=None,
        description="Most recently selected room ID",
    )
    booking_confirmed: bool = Field(
        default=False,
        description="Whether the booking has been confirmed",
    )
    last_reward: float = Field(
        default=0.0,
        description="Most recent reward value",
    )
    done: bool = Field(default=False, description="Whether the episode has ended")


class Reward(BaseModel):
    value: float = Field(..., description="Reward score for the current step")
    reason: str = Field(..., description="Explanation of why this reward was given")
