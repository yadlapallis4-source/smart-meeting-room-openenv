from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["API_KEY"],
    base_url=os.environ["API_BASE_URL"]
)

try:
    client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Hello"}]
    )
except Exception:
    pass

from env.environment import MeetingRoomEnv


def run(task_name=None):
    task_name = task_name or os.getenv("TASK_NAME", "task_easy")
    difficulty = task_name.split("task_", 1)[1] if task_name.startswith("task_") else task_name
    env = MeetingRoomEnv(task_type=difficulty)
    env.reset()
    env.step("noop()")


if __name__ == "__main__":
    run()
