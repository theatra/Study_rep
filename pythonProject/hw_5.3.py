import string

type_in = (input("Type in you hashtag-to-be: "))

# Створюємо порожні змінні, а також розділяємо ввід від користувача на окремі слова:
pre_hashtag = []
final_hashtag = []
words = type_in.split()

# Виконуємо умову про відсутність знаків пунктуації та великі літери, результат додаємо в порожній список (окремих слів):
for word in words:
    clean_word = "".join(char for char in word if char not in string.punctuation)
    pre_hashtag.append(clean_word.title())

# Об'єднуємо окремі слова в один рядок, виконуємо умову про довжину:
final_hashtag= "".join(pre_hashtag)
if len(final_hashtag) > 140:
    final_hashtag = final_hashtag[:140]

# Виконуємо конкатенацію:
final_hashtag = "#" + final_hashtag

print("Your final hashtag is: ",final_hashtag)