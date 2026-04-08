try:
    from fastapi import FastAPI
    import uvicorn
except Exception:
    FastAPI = None
    uvicorn = None

from env.environment import MeetingRoomEnv


class _FallbackApp:
    def get(self, _path):
        def decorator(func):
            return func

        return decorator

    def post(self, _path):
        def decorator(func):
            return func

        return decorator


app = FastAPI() if FastAPI is not None else _FallbackApp()
env = MeetingRoomEnv()


@app.get("/")
def home():
    return {"status": "smart-meeting-room-openenv"}


@app.post("/reset")
def reset():
    return env.reset()


@app.post("/step")
def step(action: dict):
    state, reward, done, info = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info,
    }


def main():
    if uvicorn is None:
        raise RuntimeError("uvicorn is not installed")
    uvicorn.run(app, host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()
