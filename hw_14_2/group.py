class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()
    # Створюємо функції додавання, пошуку і видалення (на базі пошуку):
    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)
        else:
            print(f"No student with last name '{last_name}' found.")

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                print(f"Student {last_name} studies in a group {self.number}.")
                return student
        return None

    # Для рядкового представлення Групи виводимо номер і елементи множини з нового рядка:
    def __str__(self):
        all_students = ''
        if self.group:
            for student in self.group:
                all_students += str(student) + "\n"

        return f'\nGroup number: {self.number}\nStudents:\n{all_students}'
