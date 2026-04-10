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

                content = response.choices[0].message.content or ""
                content = content.upper()

                if "A" in content:
                    action = "A"
                elif "B" in content:
                    action = "B"
                elif "C" in content:
                    action = "C"
                else:
                    action = "A"

            except Exception as llm_error:
                action = "A"

            # Step environment
            next_state, reward, done, info = env.step(action)

            print(f"[STEP] action={action} reward={reward} done={done}")

            break

    except Exception as e:
        print(f"[ERROR] {str(e)}")

    finally:
        print("[END]")


if __name__ == "__main__":
    run_episode()

