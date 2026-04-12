from fastapi import FastAPI
from pydantic import BaseModel
from env.environment import MeetingRoomEnv

app = FastAPI()
env = MeetingRoomEnv()

class ActionRequest(BaseModel):
    action: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(request: ActionRequest):
    state, reward, done, info = env.step(request.action)
    return {
        "state": state,
        "reward": float(reward),
        "done": bool(done),
        "info": info
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)
