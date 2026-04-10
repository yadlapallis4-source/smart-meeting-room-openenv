import os
from openai import OpenAI
from env.environment import MeetingRoomEnv

# ENV VARIABLES (Phase 2 format)
base_url = os.environ["API_BASE_URL"]
api_key = os.environ["API_KEY"]

# OpenAI client
client = OpenAI(base_url=base_url, api_key=api_key)


def run_episode():
    env = MeetingRoomEnv()
    state = env.reset()

    print("[START]")

    try:
        done = False
        step_count = 0

        while not done:
            step_count += 1

            # LLM CALL (MANDATORY)
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a smart meeting room selector."},
                        {"role": "user", "content": f"State: {state}"}
                    ]
                )

                action = response.choices[0].message.content or "A"
                action = str(action).strip().upper()

                # Fallback to simple default if invalid
                if action not in ["A", "B", "C"]:
                    action = "A"

            except Exception as llm_error:
                action = "A"

            # Step environment
            next_state, reward, done, info = env.step(action)

            print(f"[STEP] action={action}")

            state = next_state

    except Exception as e:
        print(f"[ERROR] {str(e)}")

    finally:
        print("[END]")


if __name__ == "__main__":
    run_episode()

