from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from tasks_app import db
from tasks_app.models import Task

db.init_db()

app = FastAPI()


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str
    done: bool


@app.get("/")
def root():
    return {"message": "Привет, это менеджер задач"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tasks")
def list_tasks() -> list[Task]:
    return db.get_all_tasks()


@app.post("/tasks", status_code=201)
def create_task(data: TaskCreate) -> Task:
    return db.create_task(data.title)


@app.get("/tasks/{task_id}")
def get_task(task_id: int) -> Task:
    task = db.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, data: TaskUpdate) -> Task:
    task = db.update_task(task_id, data.title, data.done)
    if task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task


@app.delete("/tasks/{task_id}", status_code=204)
def remove_task(task_id: int):
    if not db.delete_task(task_id):
        raise HTTPException(status_code=404, detail="Задача не найдена")
