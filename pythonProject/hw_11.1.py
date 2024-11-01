
from inspect import isgenerator

def prime_generator(end):
    # До параметра додамо + 1, аби останнє значення також враховувалося; одразу пропускаємо 0 і 1, а 2 - "зараховуємо":
    for number in range(end+1):
        if number <= 1:
            continue

        if number == 2:
            yield number
        # Для решти чисел з аргументу послідовно перевіряємо, щоб вони не ділилися націло ані на що, окрім себе.
        # Починаємо з двійки і поступово збільшуємо значення, аж допоки не дійдемо до власне number:
        d = 2
        while number % d != 0:
            d += 1
            if d == number:
                yield number

gen = prime_generator(29)

assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
