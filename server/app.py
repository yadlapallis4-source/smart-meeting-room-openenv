from fastapi import FastAPI
import uvicorn
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

def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
