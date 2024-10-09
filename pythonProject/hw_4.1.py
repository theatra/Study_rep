#Створюємо змінну для нового списку і рахуємо нулі за допомогою відповідної функції:
list = [12, 0, 15, 99, 87, 0, 81, 0]
print ("Initial list is:", list)
new_list = []
zeros = list.count(0)

#Переносимо в новий список значення, що не дорівнюють нулю:
for i in list:
    if i != 0:
        new_list.append(i)

#Додаємо відповідну кількість нулів у форматі списку:
new_list = new_list + [0] * zeros

print("The new list is:", new_list)