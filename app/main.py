from fastapi import FastAPI
from app.routers import task
from app.routers import user

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message" : "Welcome to TaskManager"}

app.include_router(task.task_router)
app.include_router(user.user_router)