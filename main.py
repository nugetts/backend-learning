from tasks_app.models import Task
from tasks_app.services import add_task, complete_task, delete_task
from tasks_app.storage import load_tasks, save_tasks


def show_tasks(tasks: list[Task]) -> None:
    if not tasks:
        print("Задач пока нет.")
        return
    for task in tasks:
        mark = "✓" if task.done else " "
        print(f"[{mark}] {task.id}. {task.title}")


def ask_id() -> int | None:
    text = input("Номер задачи: ")
    if not text.isdigit():
        print("Нужно ввести число.")
        return None
    return int(text)


def main() -> None:
    tasks = load_tasks()

    while True:
        print()
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Отметить сделанной")
        print("4. Удалить задачу")
        print("0. Выйти")
        choice = input("Выбери действие: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Название задачи: ")
            add_task(tasks, title)
            save_tasks(tasks)
            print("Добавлено.")
        elif choice == "3":
            task_id = ask_id()
            if task_id is not None:
                if complete_task(tasks, task_id):
                    save_tasks(tasks)
                    print("Отмечено.")
                else:
                    print("Такой задачи нет.")
        elif choice == "4":
            task_id = ask_id()
            if task_id is not None:
                if delete_task(tasks, task_id):
                    save_tasks(tasks)
                    print("Удалено.")
                else:
                    print("Такой задачи нет.")
        elif choice == "0":
            print("Пока!")
            break
        else:
            print("Не понял, выбери цифру из меню.")


if __name__ == "__main__":
    main()