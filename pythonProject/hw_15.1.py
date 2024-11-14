class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
            return self.width * self.height

    def __eq__(self, other):
        # Обчислюємо обидві площі:
        self_square = self.get_square()
        other_square = other.get_square()

        # Перевіряємо на тип даних, прописуємо порівняння:
        if isinstance (other, Rectangle):
            return self.get_square() == other.get_square()
        else:
            raise TypeError("Must be the square of a rectangular!")

    # Так само перевіряємо на тип даних, прописуємо додавання (в наступному методі те саме):
    def __add__(self, other):
        if not isinstance (other, Rectangle):
            raise TypeError("Must be the square of a rectangular!")
        if isinstance (other, Rectangle):
            total_area = self.get_square() + other.get_square()
            return Rectangle(total_area, 1)


    def __mul__(self, n):
        if not isinstance(n, int):
            raise TypeError("N must be an integer!")

        new_area = self.get_square() * n
        # Аби повернути прямокутник з валідними сторонами, обчислюємо нову висоту, виходячи з нової площі і старої ширини:
        new_height = new_area // self.width  # Integer division to get the new height
        return Rectangle(self.width, new_height)

    # Строкове представлення:
    def __str__(self):
        if isinstance (other,(Rectangle)):
            return f"Rectangle(width={self.width}, height={self.height}, area={self.get_square()})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'