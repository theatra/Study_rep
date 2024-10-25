

def popular_words(text, pop_list):
    # Все, що отримали як аргумент text, розбиваємо на окремі lowercase слова:
    all_words = [word.lower() for word in text.split()]

    # Створюємо словник, де первісно всі value - 0:
    wordcount = {word: 0 for word in pop_list}

    # За допомогою циклу перебираємо всі слова першого аргумента; якщо знахдимо їх в масиві другого аргумента,
    # відповідно змінюємо значення value в словнику:
    for word in all_words:
        if word in pop_list:
            wordcount[word] += 1

    return wordcount

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

# v2 Робимо те саме, але з методом update:
def popular_words(text, word_list):
    words = text.lower().split()

    wordcount = {}

    for word in word_list:
        if word_list.count(word) > 0:
            wordcount.update({word: words.count(word)})
        else:
            wordcount.update({word: 0})

    return wordcount

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')