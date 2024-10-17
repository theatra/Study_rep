

def common_elements():
    # Генеруємо числа у форматі списку:
    number_list = list(range(100))

    print (f"The initial list is as follows {number_list}")

    # Створюємо 2 окремі підсписки для кожного виду чисел:
    div_by_3_list = []
    div_by_5_list = []

    # Розподіляємо числа по відповідним спискам:
    for number in number_list:
        if number % 3 == 0:
            div_by_3_list.append(number)

        if number % 5 == 0:
            div_by_5_list.append(number)

    # Перетворюємо списки на множини:
    final_div_by_3_list = set(div_by_3_list)
    final_div_by_5_list = set(div_by_5_list)

    print(f"\nThe first number list is as follows {final_div_by_3_list}")
    print(f"\nThe second number list is as follows {final_div_by_5_list}")

    # Знаходимо числа "на перетині":
    intersecting_numbers = final_div_by_5_list.intersection(final_div_by_3_list)
    return intersecting_numbers

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

print(f"\nThe intersecting numbers are as follows {common_elements()}")



