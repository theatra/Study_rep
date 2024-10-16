
# Очікуємо ввод у форматі списку:
number = list(input("Enter a number up to 4 digits: "))

# Перетворюємо його елементи на цілі числа:
for i in range(len(number)):
    number[i] = int(number[i])

 # Створюємо цикл для умови, що чисел більше одного (а якщо й одне, то не дев'ятка); а також створюмо рядок для множення:
while len(number) > 1 or (len(number) == 1 and number[0] > 9):
    multiplication_result = 1

# Перебираємо числа списку по одному, послідовно перемножаючи:
    for digit in number:
        multiplication_result = multiplication_result * digit

    print("Current multiplication result:", multiplication_result)

# Якщо добуток більший від 9, знову ділимо на окремі цифри (тип даних міняємо на int). Після цього - знову до циклу while:
    if multiplication_result > 9:
        number = list(str(multiplication_result))
        for i in range(len(number)):
            number[i] = int(number[i])
    else:
        print("Final result:", multiplication_result)
        break

print ("Bye")


