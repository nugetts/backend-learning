from tasks_app.models import Task
from tasks_app.services import add_task, find_task, complete_task

tasks: list[Task] = []

add_task(tasks, "Купить молоко")
add_task(tasks, "Сделать домашку")

complete_task(tasks, 1)

for task in tasks:
    mark = "✓" if task.done else " "
    print(f"[{mark}] {task.id}. {task.title}")

print(find_task(tasks, 99))
print(complete_task(tasks, 99))