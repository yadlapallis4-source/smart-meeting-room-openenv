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


def select_best_room(state, difficulty):
    """Intelligently select the best room based on requirements and difficulty"""
    rooms = state.get("rooms", [])
    requirements = state.get("requirements", {})
    people_needed = requirements.get("people", 0)
    projector_needed = requirements.get("projector", False)

    # Filter rooms by capability
    suitable_rooms = []
    for room in rooms:
        capacity_ok = room["capacity"] >= people_needed
        projector_ok = not projector_needed or room["projector"]
        if capacity_ok and projector_ok:
            suitable_rooms.append(room)

    if suitable_rooms:
        if difficulty == "hard":
            # Hard: choose smallest suitable room (optimize)
            best_room = min(suitable_rooms, key=lambda r: r["capacity"])
        else:
            # Easy/Medium: choose first suitable room
            best_room = suitable_rooms[0]
        return best_room["id"]
    else:
        # Fallback: choose first available room
        return rooms[0]["id"] if rooms else "A"


def run_episode():
    env = MeetingRoomEnv()
    state = env.reset()
    task_name = state.get("task_id", "unknown")
    benchmark = "openenv"
    difficulty = state.get("difficulty", "easy")

    print(
        f"[START] task={task_name} env={benchmark} model={MODEL_NAME}"
    )

    rewards = []
    step_count = 0
    success = False

    try:
        done = False

        while not done:
            step_count += 1

            # Get context for LLM
            requirements = state.get("requirements", {})
            rooms_info = "\\n".join(
                [
                    f"  Room {r['id']}: capacity={r['capacity']}, projector={r['projector']}"
                    for r in state.get("rooms", [])
                ]
            )

            prompt = f"""You are a meeting room assignment assistant.
Requirements: {requirements}
Available rooms:
{rooms_info}

Select the best room ID (A, B, or C) that meets the requirements.
Respond with only the room ID."""

            # LLM CALL (MANDATORY)
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": prompt}],
            )

            action = response.choices[0].message.content or "A"
            action = action.strip().upper()

            # Fallback to intelligent selection if LLM fails
            if action not in ["A", "B", "C"]:
                action = select_best_room(state, difficulty)

            next_state, reward, done, info = env.step(action)
            rewards.append(f"{reward:.2f}")

            # Provide explanation
            req = state.get("requirements", {})
            explanation = f"Selected Room {action}"
            for room in state.get("rooms", []):
                if room["id"] == action:
                    capacity_str = f"capacity={room['capacity']}"
                    projector_str = f"projector={room['projector']}"
                    explanation += f" ({capacity_str}, {projector_str})"
                    break

            print(
                f"[STEP] step={step_count} action={action} reward={reward:.2f} done={str(done).lower()} error=null"
            )
            print(f"        {explanation}")

            state = next_state
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

