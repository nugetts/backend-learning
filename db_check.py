from tasks_app.db import (
    create_task,
    delete_task,
    get_all_tasks,
    get_task,
    init_db,
    update_task,
)

init_db()

t = create_task("Проверить базу")
print("создана:", t)
print("найдена:", get_task(t.id))
print("изменена:", update_task(t.id, "Проверить базу ещё раз", True))
print("все задачи:", get_all_tasks())
print("удалена:", delete_task(t.id))
print("удалена повторно:", delete_task(t.id))
print("после удаления:", get_task(t.id))
