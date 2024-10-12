# Створюємо калькулятор в межах нескінченного циклу while true:

while True:
    figure_1 = int(input("Choose figure 1: "))
    figure_2 = int(input("Choose figure 2: "))
    action = int(input("Choose operation\n1. +\n2. -\n3. *\n4. /\n"))

    if action == 1:
        print(figure_1 + figure_2)
    if action == 2:
        print(figure_1 - figure_2)
    if action == 3:
        print(figure_1 * figure_2)
    if action == 4:
        if figure_2 > 0:
            print(figure_1 // figure_2)
        elif figure_2 == 0:
            print("Forbidden operation!")

    # Створюємо змінну для вводу від користувача, і далі новий цикл з відповідними умовами:
    answer = (input("Do you want to continue? Type Y or N: "))

    if answer == "Y":
        print("Ok let's proceed to calculations!")
    elif answer == "N":
        print("Goodbye!")
        break
    else:
        print("Invalid answer. You had to choose Y or N!")
