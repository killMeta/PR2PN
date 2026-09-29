import os
import shutil
import time
import logging
from datetime import datetime

logging.basicConfig(
    filename="scheduler.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

tasks = []
def file_operation(task):
    try:
        op = task["operation"]
        src = task["source"]
        dst = task.get("destination")
        if op == "copy":
            shutil.copy2(src, dst)
        elif op == "move":
            shutil.move(src, dst)
        elif op == "delete":
            os.remove(src)
        elif op == "archive":
            shutil.make_archive(dst, "zip", src)
        logging.info(
            f"Task {task['id']} - {op} - SUCCESS"
        )

        print(f"Задача {task['id']} выполнена.")
    except Exception as e:
        logging.error(
            f"Task {task['id']} - FAILED: {e}"
        )
        
        print(f"Ошибка: {e}")
def add_task():
    task = {
        "id": len(tasks) + 1,
        "operation": input(
            "Операция (copy/move/delete/archive): "
        ),
        "source": input("Исходный файл: "),
        "destination": input(
            "Файл назначения: "
        ),
        "time": input(
            "Время (HH:MM): "
        )
    }
    tasks.append(task)
    print("Задача добавлена.")
def show_tasks():
    if not tasks:
        print("Задач нет.")
        return
    for task in tasks:
        print(
            f"{task['id']}. "
            f"{task['operation']} | "
            f"{task['source']} | "
            f"{task['time']}"
        )
def scheduler():
    print("Шедулер запущен. Ctrl+C для выхода.")
    while True:
        now = datetime.now().strftime("%H:%M")
        for task in tasks:
            if task["time"] == now:
                file_operation(task)
        time.sleep(60)
def main():
    while True:
        print("\n1 - Добавить задачу")
        print("2 - Показать задачи")
        print("3 - Запустить шедулер")
        print("4 - Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            scheduler()
        elif choice == "4":
            break
if __name__ == "__main__":
    main()