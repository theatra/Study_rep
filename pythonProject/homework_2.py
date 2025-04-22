
# Обираємо число і шукаємо (методом ручного перебору))) формули, за якими можна отримати цифри, що складають це число.

'''number = 3458

number_1 = number // 1000
print (number_1)

number_2 = number % 1000 // 100
print (number_2)

number_3 = number % 1000 % 100 // 10
print (number_3)

number_4 = number % 10
print (number_4)

print (int(number_4), "\n", (number_3), "\n", (number_2), "\n", (number_1))
'''

# Все вийшло, тепер можна використати функцію input. На вхід очікуємо ціле число (int):

number = (int(input("Please enter a 4-digit number:")))

print ("The number you entered is:", number, ". It has the following digits:")

number_1 = number // 1000
print (number_1)

number_2 = number % 1000 // 100
print (number_2)

number_3 = number % 1000 % 100 // 10
print (number_3)

number_4 = number % 10
print (number_4)


