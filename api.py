from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from tasks_app.models import Task
from tasks_app.services import add_task, delete_task, find_task
from tasks_app.storage import load_tasks, save_tasks

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
    return load_tasks()


@app.post("/tasks", status_code=201)
def create_task(data: TaskCreate) -> Task:
    tasks = load_tasks()
    task = add_task(tasks, data.title)
    save_tasks(tasks)
    return task


@app.get("/tasks/{task_id}")
def get_task(task_id: int) -> Task:
    task = find_task(load_tasks(), task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, data: TaskUpdate) -> Task:
    tasks = load_tasks()
    task = find_task(tasks, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    task.title = data.title
    task.done = data.done
    save_tasks(tasks)
    return task


@app.delete("/tasks/{task_id}", status_code=204)
def remove_task(task_id: int):
    tasks = load_tasks()
    if not delete_task(tasks, task_id):
        raise HTTPException(status_code=404, detail="Задача не найдена")
    save_tasks(tasks)
