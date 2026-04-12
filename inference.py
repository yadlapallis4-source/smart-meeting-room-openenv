import os
from openai import OpenAI
from env.environment import MeetingRoomEnv

# ENV VARIABLES
client = OpenAI(base_url=os.environ["API_BASE_URL"], api_key=os.environ["API_KEY"])


def run_episode():
    env = MeetingRoomEnv()
    state = env.reset()

    print("[START]", flush=True)

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

            print(f"[DEBUG] LLM_RESPONSE={response.choices[0].message.content}", flush=True)

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

        except Exception as e:
            print(f"[ERROR] LLM FAILED: {str(e)}", flush=True)
            action = "A"

        # STEP ENVIRONMENT
        next_state, reward, done, info = env.step(action)

        # EXACT FORMAT (CRITICAL)
        print(f"[STEP] action={action} reward={float(reward):.2f} done={str(done).lower()}", flush=True)

    except Exception as e:
        print(f"[ERROR] {str(e)}", flush=True)

    finally:
        print("[END]", flush=True)


if __name__ == "__main__":
    run_episode()