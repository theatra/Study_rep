import random

#Задаємо рандомну довжину, вказуємо список:
lengh = random.randint(3,10)
random_list = []

#Вказуємо діапазон значень для цикла:
for value in range(lengh):
    random_list.append(random.randint(1, 99))

print ("Original list:", random_list)

#Визначаємо вигляд нового списка:
new_random_list = [random_list[0], random_list[2], random_list[-2]]

print("New list:",new_random_list)