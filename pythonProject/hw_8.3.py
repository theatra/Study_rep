

def find_unique_value(some_list):
    # Створюємо порожній список, у який запишемо цифри, що зустрілися лише 1 раз:
    no_duplication_list = []
    for number in some_list:
        if some_list.count(number) == 1:
            no_duplication_list.append(number)
    # Якщо в ньому усього 1 значення, повертаємо його:
    if len(no_duplication_list) == 1:
        return no_duplication_list[0]
    # Якщо більше, умова не виконана:
    else:
        return False


assert find_unique_value([1, 2, 2, 1]) == False,'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")