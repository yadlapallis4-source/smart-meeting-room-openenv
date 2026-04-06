from fastapi import FastAPI
from env.environment import SmartMeetingEnv
from env.models import Action
import uvicorn

app = FastAPI()
env = SmartMeetingEnv()

@app.get("/")
def home():
    return {"status": "Smart Meeting OpenEnv running"}

@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "message": "Environment reset successfully",
        "task_id": obs.task_id
    }

@app.post("/step")
def step(action: dict):
    try:
        act = Action(**action)
    except Exception as e:
        return {"error": f"Invalid action: {str(e)}"}

    try:
        obs, reward, done, info = env.step(act)
        return {
            "reward": float(reward),
            "done": bool(done),
            "task_id": obs.task_id,
            "info": info if isinstance(info, dict) else {}
        }
    except Exception as e:
        return {"error": str(e)}

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
