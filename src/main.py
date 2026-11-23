from fastapi import FastAPI
from src.routes import router

app = FastAPI()


@app.get("/ping")
def health_check():
    return {"status": "pong"}


app.include_router(router)
