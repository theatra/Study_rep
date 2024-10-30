def first_word(text):
    # Розбиваємо рядок на окремі слова; метод replace довелося застосувати для виконання assert 6:
    words = text.replace(".", " ").split()

    # Отримані слова звільняємо від небуквенних знаків; для апострофа в assert 5 також довелося прописати умову окремо:
    for word in words:
        cleaned_word = word.strip(" .,!")
        if cleaned_word and (cleaned_word.isalpha() or "'" in cleaned_word):  # Ensure the cleaned word is not empty
            return cleaned_word

    return None

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')