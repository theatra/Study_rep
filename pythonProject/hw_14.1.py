class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    # Прописуємо виведення інформації про Human:
    def __str__(self):
        return f"{self.first_name} {self.last_name} is a {self.age}yo {self.gender}."

class Student(Human):
    # Наслідуємо клас Student від попереднього + додаємо специфічний параметр, далі також прописуємо виведення:
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Student {self.first_name} {self.last_name} is a {self.age}yo {self.gender} with a record book {self.record_book}."
# Описуємо параметри нового класу, створюючи порожню множину для зберігання списку студентів:
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

human = Human('male', 30, 'Steve', 'Jobs')
student = Student('female', 25, 'Liza', 'Taylor', 'AN145')
print(human)
print(student)

st1 = Student('male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!