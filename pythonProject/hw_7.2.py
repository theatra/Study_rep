# Створюємо функцію. Щоб мати змогу окремо звертатися до частин аргумента,
# ділимо рядок на окремі слова, визначаємо їх за індексами:
def correct_sentence(text):
    words = text.split()

    word_1 = words[0]
    word_2 = words[1] if len(words) > 1 else None
# Виконуємо умови з assert щодо len(списку), капіталізації й закінчення на точку:
    if len(words) == 2 and word_2.endswith("."):
        return f"{word_1.capitalize()} {word_2}"

    elif len(words) == 2 and word_2.isalpha():
        return f"{word_1.capitalize()} {word_2}."

    elif len(words) == 1:
        return f"{word_1.capitalize()}."

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')

