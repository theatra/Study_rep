#Створюємо список і порожню змінну:
list = [3, 16, 18, 9, 4, 20, 7, 9]

my_sum_and_multiplication_result = 0

#За допомогою циклу знаходимо потрібні індекси:
for i in range (len(list)):
    if i % 2 == 0:
        #Додати і помножити можна одним рядком:
        my_sum_and_multiplication_result += list[i] * list[-1]
print("The requested result is", my_sum_and_multiplication_result)