from tasks_app import db
from tasks_app.models import Task


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
    db.init_db()

    while True:
        print()
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Отметить сделанной")
        print("4. Удалить задачу")
        print("0. Выйти")
        choice = input("Выбери действие: ")

        if choice == "1":
            show_tasks(db.get_all_tasks())
        elif choice == "2":
            title = input("Название задачи: ")
            db.create_task(title)
            print("Добавлено.")
        elif choice == "3":
            task_id = ask_id()
            if task_id is not None:
                task = db.get_task(task_id)
                if task is None:
                    print("Такой задачи нет.")
                else:
                    db.update_task(task_id, task.title, True)
                    print("Отмечено.")
        elif choice == "4":
            task_id = ask_id()
            if task_id is not None:
                if db.delete_task(task_id):
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