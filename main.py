from tasks_app.models import Task
from tasks_app.services import add_task
from tasks_app.storage import load_tasks, save_tasks

tasks: list[Task] = load_tasks()

add_task(tasks, "Новая задача")
save_tasks(tasks)

for task in tasks:
    mark = "✓" if task.done else " "
    print(f"[{mark}] {task.id}. {task.title}")