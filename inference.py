import os
from openai import OpenAI
from env.environment import MeetingRoomEnv

# ENV VARIABLES
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

# OpenAI client
client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)


def run_episode():
    env = MeetingRoomEnv()

    state = env.reset()

    task_name = state.get("task_id", "unknown")
    benchmark = "openenv"

    print(f"[START] task={task_name} env={benchmark} model={MODEL_NAME}")

    rewards = []
    step_count = 0
    success = False

    try:
        done = False

        while not done:
            step_count += 1

            # LLM CALL (MANDATORY)
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": "choose best meeting room"}],
            )

            action = response.choices[0].message.content or "default_action"

            next_state, reward, done, info = env.step(action)

            rewards.append(f"{reward:.2f}")

            print(
                f"[STEP] step={step_count} action={action} reward={reward:.2f} done={str(done).lower()} error=null"
            )

        success = True

    except Exception as e:
        print(
            f"[STEP] step={step_count} action=null reward=0.00 done=true error={str(e)}"
        )

    finally:
        print(
            f"[END] success={str(success).lower()} steps={step_count} rewards={','.join(rewards)}"
        )


if __name__ == "__main__":
    run_episode()
