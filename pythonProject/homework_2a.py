# Обираємо число і шукаємо (методом ручного перебору))) формули, за якими можна отримати цифри, що складають це число.

'''number = 34584

number_1 = number // 10000

number_2 = number % 10000 // 1000

number_3 = number % 10000 % 1000 // 100

number_4 = number % 10000 % 1000 % 100 // 10

number_5 = number % 10'''

# Все вийшло, тепер можна використати функцію input. На вхід очікуємо ціле число (int). Далі виводимо у зворотному порядку (чомусь не вийшло застосувати новий рядок /n).

number = (int(input("Please enter a 5-digit number:")))

print ("The number you entered is:", number, ". It has the following digits in the ascending order:")

print (number_5)
print (number_4)
print (number_3)
print (number_2)
print (number_1)