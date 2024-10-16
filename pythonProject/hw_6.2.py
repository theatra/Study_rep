import time

seconds_total = int(input("Enter seconds from 0 to 8640000: "))
full_date = [] # дні, години, хвилини та секунди

# В 1 добі 86400 секунд. Знаходимо кількість діб у вводі користувача і зберігаємо в список (якщо жодної, зберігаємо 0);
# після цього обчислюємо залишок:

if seconds_total >= 86400:
    days = seconds_total // 86400
    full_date.append(f"{days} day(s)")
    seconds_rest_1 = seconds_total - days * 86400
else:
    days = 0
    full_date.append(f"{days} day(s)")
    seconds_rest_1 = seconds_total

# В 1 годині 3600 секунд. Знаходимо кількість годин у залишку від ділення; обчислюємо новий залишок:
hours = seconds_rest_1 // 3600
full_date.append(hours)
seconds_rest_2 = seconds_rest_1 - hours * 3600

# В 1 хвилині 60 секунд. Знаходимо кількість хвилин у залишку від ділення; обчислюємо новий залишок:
minutes = seconds_rest_2 // 60
full_date.append(minutes)
seconds_rest_3 = seconds_rest_2 - minutes * 60

# Все, що лишається після попередньої операції, секунди:
seconds = seconds_rest_3
full_date.append(seconds)

full_date_string = f"{full_date[0]}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

print("Your full date is: ", full_date_string)
