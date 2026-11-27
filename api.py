from fastapi import FastAPI
from pydantic import BaseModel

from tasks_app.models import Task
from tasks_app.services import add_task
from tasks_app.storage import load_tasks, save_tasks

app = FastAPI()


class TaskCreate(BaseModel):
    title: str


@app.get("/")
def root():
    return {"message": "Привет, это менеджер задач"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tasks")
def list_tasks() -> list[Task]:
    return load_tasks()


@app.post("/tasks", status_code=201)
def create_task(data: TaskCreate) -> Task:
    tasks = load_tasks()
    task = add_task(tasks, data.title)
    save_tasks(tasks)
    return task
