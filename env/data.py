from typing import List
from .models import Room, BookingRequest


def get_rooms() -> List[Room]:
    return [
        Room(
            room_id="R1",
            name="Small Meeting Room",
            capacity=4,
            building="A",
            floor=1,
            has_projector=False,
            has_video_conference=False,
            accessible=True,
            priority_level="standard",
        ),
        Room(
            room_id="R2",
            name="Medium Conference Room",
            capacity=8,
            building="A",
            floor=2,
            has_projector=True,
            has_video_conference=False,
            accessible=True,
            priority_level="standard",
        ),
        Room(
            room_id="R3",
            name="Large Conference Room",
            capacity=12,
            building="B",
            floor=3,
            has_projector=True,
            has_video_conference=True,
            accessible=True,
            priority_level="premium",
        ),
        Room(
            room_id="R4",
            name="Video Meeting Room",
            capacity=6,
            building="B",
            floor=1,
            has_projector=False,
            has_video_conference=True,
            accessible=True,
            priority_level="standard",
        ),
        Room(
            room_id="R5",
            name="Executive Board Room",
            capacity=10,
            building="A",
            floor=5,
            has_projector=True,
            has_video_conference=True,
            accessible=True,
            priority_level="premium",
        ),
        Room(
            room_id="R6",
            name="Compact Room",
            capacity=3,
            building="C",
            floor=1,
            has_projector=False,
            has_video_conference=False,
            accessible=False,
            priority_level="standard",
        ),
    ]


# ---------------------------
# TASKS (3 LEVELS)
# ---------------------------


def get_easy_request() -> BookingRequest:
    return BookingRequest(
        request_id="T1",
        team_name="Design Team",
        attendees=3,
        duration_minutes=30,
        needs_projector=False,
        needs_video_conference=False,
        accessibility_required=False,
        preferred_building=None,
        preferred_floor=None,
        urgency="low",
        vip_meeting=False,
    )


def get_medium_request() -> BookingRequest:
    return BookingRequest(
        request_id="T2",
        team_name="Engineering Team",
        attendees=6,
        duration_minutes=60,
        needs_projector=True,
        needs_video_conference=False,
        accessibility_required=False,
        preferred_building="A",
        preferred_floor=None,
        urgency="medium",
        vip_meeting=False,
    )


def get_hard_request() -> BookingRequest:
    return BookingRequest(
        request_id="T3",
        team_name="Leadership",
        attendees=9,
        duration_minutes=90,
        needs_projector=True,
        needs_video_conference=True,
        accessibility_required=True,
        preferred_building="A",
        preferred_floor=5,
        urgency="high",
        vip_meeting=True,
    )
