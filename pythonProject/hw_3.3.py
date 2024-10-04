

numbers = []

result = len(numbers) % 2
print(result)
if result == 0:
    first_part = numbers[:len(numbers)//2]
    second_part = numbers[len(numbers)//2:]
    print([first_part] + [second_part])
if result > 0:
    first_part = numbers[:len(numbers) // 2]
    second_part = numbers[len(numbers) // 2:]
    print([second_part] + [first_part])