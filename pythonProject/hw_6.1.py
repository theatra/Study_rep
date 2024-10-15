
import string

# Отримуємо ввід від користувача і переконуємося, що він коректний (дві літери и дефіс):

ascii_letter_range = list(input("Type two latin letters, with a hyphen in between: "))

if ascii_letter_range[0].isalpha() and ascii_letter_range[2].isalpha() and ascii_letter_range[1] == "-":
    pass
else:
    print("Invalid input, please respect 'letter-letter' format!")
    exit()

# Отримуємо літери за індексами:
ascii_letter_1 = ascii_letter_range[0]
ascii_letter_2 = ascii_letter_range[2]

# Враховуємо 2 умови, аби за будь-якого порядку літер у вводі список був за алфавітом:
if ascii_letter_1 <= ascii_letter_2:
    start = ascii_letter_2
    end = ascii_letter_1

elif ascii_letter_1 >= ascii_letter_2:
    start = ascii_letter_1
    end = ascii_letter_2

ascii_letter_range = []

# Оскільки враховуються і великі, і малі літери, а пунктуація, що також входить до ascii-символів, - ні,
# маємо прописати купу умов:

if start.isupper() and end.isupper():
    ascii_letter_range = [chr(i) for i in range(start, end + 1) if chr(i).isalpha()]
elif start.islower() and end.islower():
    ascii_letter_range = [chr(i) for i in range(start, end + 1) if chr(i).isalpha()]
elif start.islower() and end.isupper():
    ascii_letter_range = [chr(i) for i in range(ord(start), ord('z') + 1)] + \
                         [chr(i) for i in range(ord('A'), ord(end) + 1)]
else:
    ascii_letter_range = [chr(i) for i in range(ord(start), ord('Z') + 1)] + \
                         [chr(i) for i in range(ord('a'), ord(end) + 1)]

print("".join(ascii_letter_range))
