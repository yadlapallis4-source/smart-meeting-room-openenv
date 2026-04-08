import os
from typing import List

from openai import OpenAI

from env.environment import SmartMeetingEnv
from env.models import Action


# ------------------------
# CONFIG
# ------------------------

MODEL_NAME = os.environ["MODEL_NAME"]
HF_TOKEN = os.getenv("HF_TOKEN")
LOCAL_IMAGE_NAME = os.getenv("LOCAL_IMAGE_NAME")

client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)


# ------------------------
# LOG FUNCTIONS (MANDATORY FORMAT)
# ------------------------

def log_start(task: str, env: str, model: str):
    print(f"[START] task={task} env={env} model={model}", flush=True)


def log_step(step: int, action: str, reward: float, done: bool, error):
    error_val = error if error else "null"
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error={error_val}",
        flush=True,
    )


def log_end(success: bool, steps: int, score: float, rewards: List[float]):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}",
        flush=True,
    )


# ------------------------
# SIMPLE AGENT (RULE BASED)
# ------------------------

def select_best_room(observation):
    request = observation.request
    rooms = observation.available_rooms

    best_room = None
    best_score = -1

    for room in rooms:
        score = 0

        if room.capacity >= request.attendees:
            score += 2

            diff = room.capacity - request.attendees
            if diff == 0:
                score += 2
            elif diff <= 2:
                score += 1

        if request.needs_projector and room.has_projector:
            score += 1

        if request.needs_video_conference and room.has_video_conference:
            score += 1

        if request.accessibility_required and room.accessible:
            score += 1

        if request.preferred_building and room.building == request.preferred_building:
            score += 1

        if request.preferred_floor and room.floor == request.preferred_floor:
            score += 1

        if request.vip_meeting and room.priority_level == "premium":
            score += 1

        if score > best_score:
            best_score = score
            best_room = room

    return best_room.room_id if best_room else rooms[0].room_id


# ------------------------
# MAIN
# ------------------------

def run(task_name="task_easy"):
    env = SmartMeetingEnv(task_type=task_name)

    log_start(task_name, "smart-meeting-room-openenv", MODEL_NAME)

    rewards = []
    step_count = 0
    score = 0.0

    try:
        obs = env.reset()

        while True:
            step_count += 1

            llm_text = "Selected based on constraints"
            try:
                response = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=[
                        {"role": "user", "content": "Choose a valid action"}
                    ]
                )
                if response and hasattr(response, "choices") and response.choices:
                    content = response.choices[0].message.content
                    if content:
                        llm_text = content
            except Exception as e:
                print(f"API Error: {e}")

            room_id = select_best_room(obs)

            action = Action(
                room_id=room_id,
                confirm=True,
                reasoning_note=llm_text,
            )

            obs, reward, done, _ = env.step(action)

            rewards.append(reward)

            log_step(
                step_count,
                f"select_room('{room_id}')",
                reward,
                done,
                None,
            )

            if done:
                break

        score = float(rewards[-1]) if rewards else 0.0
        success = score > 0.5 

    except Exception as e:
        if step_count == 0:
            step_count = 1
        log_step(step_count, "noop()", 0.0, True, str(e))
        success = False
        score = 0.0
        if not rewards:
            rewards.append(0.0)

    log_end(success, step_count, score, rewards)


if __name__ == "__main__":
    task = os.getenv("TASK_NAME", "task_easy")
    run(task)
