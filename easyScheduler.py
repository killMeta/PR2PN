from datetime import datetime
import time

task = input("Введите задание: ")
deadline = input("Выполнить к (ЧЧ:ММ): ")
now = datetime.now()
target = datetime.strptime(deadline, "%H:%M").replace(
    year=now.year,
    month=now.month,
    day=now.day
)
if target < now:
    print("Указанное время уже прошло.")
else:
    print(f"Задание принято: {task}")
    print(f"Решить к: {deadline}")
    while datetime.now() < target:
        time.sleep(1)
    print("\nВремя пришло!")
    print(f"Задание: {task}")
    try:
        answer = eval(task)
        print(f"Ответ: {answer}")
    except:
        print("Не удалось автоматически решить задание.")