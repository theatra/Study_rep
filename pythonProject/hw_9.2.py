
def difference(*args):
    if not args:
        return 0
    # Відсортуємо елементи і виконаємо віднімання за індексами:
    args = sorted(args)
    result = args[-1] - args[0]

    # Окремо пропишемо умову, коли отримане число не ціле (у цьому випадку застосуємо округлення):
    if type(result) == float:
        result = round(result, 2)

    print(result)
    return result

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
