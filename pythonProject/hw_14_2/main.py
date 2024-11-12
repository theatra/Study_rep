from human import Human
from student import Student
from group import Group

def main():
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

    assert gr.find_student('Jobs') == st1
    assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
    assert gr.find_student('Jobs2') is None, 'Test2'
    assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

    gr.delete_student('Taylor')
    print(gr)

    gr.delete_student('Taylor')


if __name__ == "__main__":
    main()