from tasks_app.models import Task

def add_task(tasks: list[Task], title: str) -> Task:
    new_id = max((t.id for t in tasks), default=0) + 1
    task = Task(id=new_id, title = title)
    tasks.append(task)
    return task


def find_task(tasks: list[Task], task_id: int) -> Task | None:
    for task in tasks:
        if task.id == task_id:
            return task
    return None


def complete_task(tasks: list[Task], task_id: int) -> bool:
    task = find_task(tasks, task_id)
    if task is None:
        return False
    task.done = True
    return True

def delete_task(tasks: list[Task], task_id: int) -> bool:
    task = find_task(tasks, task_id)
    if task is None:
        return False
    tasks.remove(task)
    return True