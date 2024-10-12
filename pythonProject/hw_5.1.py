
potential_variable_name = input("Please enter a potential variable: ")

# Варіант, мабуть, примітивний - але зрозумілий))

if  (len(potential_variable_name) == 0 or
    potential_variable_name[0].isdigit() or
    any(char.isupper() for char in potential_variable_name) or
    potential_variable_name in keyword.kwlist or
    # Подвійний андерскор напряму виключаємо в умові, а далі вилучаємо одинарний зі списку string.punctuation, і він стає дозволеним символом:
    "__" in potential_variable_name or
    any(char in string.punctuation.replace("_", "") for char in potential_variable_name)):
        print("False")
else:
    print("True")