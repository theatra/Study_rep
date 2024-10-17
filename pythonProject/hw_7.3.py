

def second_index(text, some_str):
    # Спочатку знаходимо першу появу some_str, якщо є, і на її основі за індексом знаходимо другу:
    first_occurence = text.find(some_str)
    if first_occurence != -1:
        second_occurence = text.find(some_str, first_occurence + 1)
    # Далі вказуємо, яке значення треба повернути (за відсутності другої появи - None):
    return second_occurence if second_occurence != -1 else None

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
