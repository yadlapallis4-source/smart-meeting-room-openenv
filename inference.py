import os
from openai import OpenAI
from env.environment import MeetingRoomEnv

# ENV VARIABLES
base_url = os.environ["API_BASE_URL"]
api_key = os.environ["API_KEY"]

client = OpenAI(base_url=base_url, api_key=api_key)


def run_episode():
    env = MeetingRoomEnv()
    state = env.reset()

    print("[START]")

    try:
        # ONE STEP ONLY (IMPORTANT)
        
        # LLM CALL (MANDATORY)
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Choose best meeting room: A, B, or C"},
                    {"role": "user", "content": str(state)}
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

        except:
            action = "A"

        # STEP ENVIRONMENT
        next_state, reward, done, info = env.step(action)

        # EXACT FORMAT (CRITICAL)
        print(f"[STEP] action={action} reward={reward} done={done}")

    except Exception as e:
        print(f"[ERROR] {str(e)}")

    finally:
        print("[END]")


if __name__ == "__main__":
    run_episode()