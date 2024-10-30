def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    # Ініціюємо змінну, що рахуватиме ітерації, та змінну з першим аргументом:
    count = 0
    current_value = begin
    # Створюємо цикл, який зберігатиме отримане ф-єю pow значення + 1, аж допоки не буде досягнуто значення end:
    while count < end:
        yield current_value
        current_value = func(current_value)
        count += 1

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')

