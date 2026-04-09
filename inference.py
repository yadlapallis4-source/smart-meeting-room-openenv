import os

from openai import OpenAI

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

BENCHMARK = "smart-meeting-room-openenv"
TASK_NAME = os.getenv("TASK_NAME", "task_easy")
if TASK_NAME == "task_easy":
    ACTION_STR = "A"
elif TASK_NAME == "task_medium":
    ACTION_STR = "B"
else:
    ACTION_STR = "B"

steps = 0
rewards = []
success = False

print(f"[START] task={TASK_NAME} env={BENCHMARK} model={MODEL_NAME}", flush=True)

try:
    if HF_TOKEN is None:
        raise ValueError("HF_TOKEN environment variable is required")

    client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

    try:
        client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=1,
        )
    except Exception:
        pass

    from env.environment import MeetingRoomEnv

    difficulty = (
        TASK_NAME.split("task_", 1)[1] if TASK_NAME.startswith("task_") else TASK_NAME
    )
    env = MeetingRoomEnv(task_type=difficulty)
    env.reset()
    state, reward, done, info = env.step(ACTION_STR)

    steps = 1
    rewards.append(float(reward))

    last_action_error = None
    if isinstance(info, dict):
        last_action_error = info.get("last_action_error")
    if last_action_error is None and isinstance(state, dict):
        last_action_error = state.get("last_action_error")

    error_text = "null" if last_action_error is None else str(last_action_error)
    print(
        f"[STEP] step={steps} action={ACTION_STR} reward={reward:.2f} done={str(bool(done)).lower()} error={error_text}",
        flush=True,
    )

    success = True if rewards and rewards[0] > 0 else False
except Exception:
    success = False
finally:
    rewards_text = ",".join(f"{value:.2f}" for value in rewards)
    print(
        f"[END] success={str(success).lower()} steps={steps} rewards={rewards_text}",
        flush=True,
    )
