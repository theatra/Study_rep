
# На вхід за умовою очікуємо список, створюємо змінну аби зберегти його у вигляді рядка:
def add_one(digits):
    single_string_number = ""
    for digit in digits:
        single_string_number = single_string_number + str(digit)

    # За умовою додаємо одиницю, для цієї мети вказуємо тип даних int:
    add_one_result_string = int(single_string_number) + 1

    # На виході має бути список; ініціалізуємо порожній і зберігаємо туди вміст нашого рядка у вигляді окремих символів:
    result = []
    for char in str(add_one_result_string):
        result.append(int(char))

    return result

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")