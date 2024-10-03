

# Задаємо, що хочемо отримати на вхід:

figure_1 = int(input("Choose figure 1: "))
figure_2 = int(input("Choose figure 2: "))
action = int(input("Choose operation\n1. +\n2. -\n3. *\n4. /\n"))

# Виконуємо по черзі для всіх дій. Чомусь для четвертої умови не спрацювало для від'ємних значень (0 > figure_2 > 0)

if action == 1:
    print (figure_1 + figure_2)
if action == 2:
    print (figure_1 - figure_2)
if action == 3:
    print (figure_1 * figure_2)
if action == 4:
    if figure_2 > 0:
        print (figure_1 // figure_2)
    elif figure_2 == 0:
        print("Forbidden operation!")
