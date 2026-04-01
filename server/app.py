from fastapi import FastAPI
from env.environment import MeetingRoomEnv
from env.models import Action
import uvicorn

app = FastAPI()
env = MeetingRoomEnv(task_type="easy")

@app.post("/reset")
def reset():
    obs = env.reset()
    return {"message": "Environment reset successfully", "task_id": obs.task_id}

@app.post("/step")
def step(action: dict):
    act = Action(**action)
    obs, reward, done, info = env.step(act)
    return {
        "reward": float(reward),
        "done": bool(done),
        "task_id": obs.task_id,
        "info": info if isinstance(info, dict) else {},
    }

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
