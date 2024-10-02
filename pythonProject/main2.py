
number=int(input("Enter a 4-digit number:"))

number_1=(number // 1000)
print(number_1)
number_2=(number % 1000 // 100)
print(number_2)
number_3=(number % 1000 % 100 // 10)
print(number_3)
number_4=(number % 1000 % 100 % 10)
print(number_4)