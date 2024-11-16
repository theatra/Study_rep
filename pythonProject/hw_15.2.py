class Fraction:
    def __init__(self, numerator, denominator, reduce_on_init=True):
        if denominator == 0:
            raise ValueError("Must have denominator other than 0!")
        self.numerator = numerator
        self.denominator = denominator
        # Скорочувати дріб щоразу не треба:
        if reduce_on_init:
            self.reduce()

    def reduce(self):
        # Найбільший спільний дільник:
        def biggest_common_denominator(numerator, denominator):
            if numerator == 0:
                return denominator
            elif denominator == 0:
                return numerator
            elif numerator >= denominator:
                return biggest_common_denominator(numerator % denominator, denominator)
            else:
                return biggest_common_denominator(numerator, denominator % numerator)

        sign = 1
        if self.numerator > 0 > self.denominator or \
                (self.numerator < 0 < self.denominator):
            sign = -1
        a, b = abs(self.numerator), abs(self.denominator)
        c = biggest_common_denominator(a, b)  # GCD
        self.numerator = sign * (a // c)
        self.denominator = b // c

    def __mul__(self, other):
        if isinstance(other, Fraction):
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            result = Fraction(numerator, denominator, reduce_on_init=False)
            return result
        else:
            raise ValueError("Must be a fraction!")

    def __add__(self, other):
        if isinstance(other, Fraction):
            # Add the fractions (find a common denominator)
            numerator = self.numerator * other.denominator + \
                        self.denominator * other.numerator
            denominator = self.denominator * other.denominator
            result = Fraction(numerator, denominator, reduce_on_init=False)
            return result
        else:
            raise ValueError("Must be a fraction!")

    def __sub__(self, other):
        if isinstance(other, Fraction):
            # Subtract the fractions (find a common denominator)
            numerator = self.numerator * other.denominator - \
                        self.denominator * other.numerator
            denominator = self.denominator * other.denominator
            result = Fraction(numerator, denominator, reduce_on_init=False)  # Do not reduce immediately
            return result
        else:
            raise ValueError("Must be a fraction!")

    def __eq__(self, other):
        # Для порівняння треба скорочувати за необхідності:
        if isinstance(other, Fraction):
            self.reduce()
            other.reduce()
            return self.numerator == other.numerator and self.denominator == other.denominator
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < self.denominator * other.numerator
        return False

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator > self.denominator * other.numerator
        return False

    def __str__(self):
        return f"Fraction: {self.numerator}, {self.denominator}"

# Create fractions without automatic reduction on initialization
f_a = Fraction(2, 3, reduce_on_init=False)
f_b = Fraction(3, 6, reduce_on_init=False)

f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
