from human import Human

class Student(Human):
    # Наслідуємо клас Student від попереднього + додаємо специфічний параметр, далі також прописуємо виведення:
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Student {self.first_name} {self.last_name} is a {self.age}yo {self.gender} with a record book {self.record_book}."

    # Метод порівняння, щоб справдилася умова з assert gr.find_student('Jobs') == st1:
    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return (
                self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.age == other.age and
                self.gender == other.gender and
                self.record_book == other.record_book
        )
    #  Уникаємо помилки:
    def __hash__(self):
        return hash(str(self))