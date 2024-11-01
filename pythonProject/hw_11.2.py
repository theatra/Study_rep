from inspect import isgenerator

def generate_cube_numbers(end):
   #  Робимо з параметра послідовність, включно з останнім значенням (але починаємо з 2, бо куб одиниці в умовах не вимагається);
   #  зводимо значення послідовності до куба:
   for number in range(2, end + 1):
       pow = number ** 3

       # Перевіряємо, щоб значення в кубі не перевищувало значення аргументу:
       if pow > end:
           break
       yield pow

gen = generate_cube_numbers(1)

assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print("Ok")