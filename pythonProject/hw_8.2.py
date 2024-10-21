
def is_palindrome(text):
    # Створюємо порожній список, зберігаємо туди lowercse-символи (літери і цифри) з аргумента:
    string_to_test = []
    for char in text:
        if char.isalnum():
            string_to_test.append(char.lower())
    # Перевертаємо отриманий список і дивимося, чи співпадає він із первісним:
    if string_to_test == string_to_test[::-1]:
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
assert is_palindrome('1221') == True, 'Test5'
print("ОК")