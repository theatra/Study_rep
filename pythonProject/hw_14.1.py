from logging import raiseExceptions


class Human:
    # Ініціюємо клас Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    # Прописуємо виведення інформації про його екземпляр:
    def __str__(self):
        return f"{self.first_name} {self.last_name} is a {self.age}yo {self.gender}."

class Student(Human):
    # Наслідуємо клас Student від попереднього + додаємо специфічний параметр, далі також прописуємо виведення:
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Student {self.first_name} {self.last_name} is a {self.age}yo {self.gender} with a record book {self.record_book}."




# NEW # Створюємо власний клас виключення (для випадків перевищення максимуму в 10 студентів у групі):
class ExceededNumberError(Exception):
        pass




# Описуємо параметри нового класу, створюючи порожню множину для зберігання списку студентів:
class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()




    # NEW # Створюємо функції додавання, пошуку і видалення (на базі пошуку); прописуємо викидання виклику:
    def add_student(self, student):
        if len(self.group) >= 10:
                print("Max. number of students is 10!")
                raise ExceededNumberError("Max. number of students exceeded!")

        self.group.add(student)




    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                print(f"Student {last_name} studies in a group {self.number}.")
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)
        else:
            print(f"No student with last name '{last_name}' found.")

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
st3 = Student('female', 25, 'Liza', 'Taylor', 'AN145')
st4 = Student('female', 25, 'Liza', 'Taylor', 'AN145')
st5 = Student('female', 25, 'Liza', 'Taylor', 'AN145')
st6 = Student('female', 25, 'Liza', 'Taylor', 'AN145')
st7 = Student('female', 25, 'Liza', 'Taylor', 'AN145')
st8 = Student('female', 25, 'Liza', 'Taylor', 'AN145')
st9 = Student('female', 25, 'Liza', 'Taylor', 'AN145')
st10 = Student('female', 25, 'Liza', 'Taylor', 'AN145')
st11 = Student('female', 25, 'Liza', 'Taylor', 'AN145')



gr = Group('PD1')

students_to_add = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11]




# NEW # Створюємо блок, що оброблятиме виняток в методі add_student:
for student in students_to_add:
    try:
        gr.add_student(student)
    except ExceededNumberError as e:
        print(f"Error: {e}")




print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
print("Ok")