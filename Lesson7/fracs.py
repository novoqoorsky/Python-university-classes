import unittest
from math import gcd


class Frac:
    """ A class representing fraction """

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError("Denominator of value 0!")
        self.x = x
        self.y = y

    def __str__(self):
        if self.y != 1:
            return "{x} / {y}".format(x=self.x, y=self.y)
        return "({x})".format(x=self.x)

    def __repr__(self):
        return "Frac({x}, {y})".format(x=self.x, y=self.y)

    def __eq__(self, other):
        the_lcm = lcm(self.y, other.y)
        frac1_numerator = self.x * (the_lcm / self.y)
        frac2_numerator = other.x * (the_lcm / other.y)
        return frac1_numerator == frac2_numerator

    def __add__(self, other):
        frac2 = convert_to_frac(other)
        the_lcm = lcm(self.y, frac2.y)
        frac1_extended = [self.x * (the_lcm / self.y), the_lcm]
        frac2_extended = [frac2.x * (the_lcm / frac2.y), the_lcm]
        return Frac(frac1_extended[0] + frac2_extended[0], the_lcm)

    __radd__ = __add__

    def __sub__(self, other):
        frac2 = convert_to_frac(other)
        return self + (-frac2)

    def __rsub__(self, other):
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):
        frac2 = convert_to_frac(other)
        return Frac(self.x * frac2.x, self.y * frac2.y)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, Frac):
            if other.x == 0:
                raise ValueError("Division by 0!")
        else:
            if other == 0:
                raise ValueError("Division by 0!")
        frac2 = convert_to_frac(other)
        return self * (~frac2)

    def __rtruediv__(self, other):
        frac2 = convert_to_frac(other)
        return frac2 / self

    def __pos__(self):
        return Frac(abs(self.x), self.y)

    def __neg__(self):
        return Frac(-self.x, self.y)

    def __invert__(self):
        return Frac(self.y, self.x)

    def __float__(self):
        return self.x / self.y


def lcm(a, b):
    return (a * b) // gcd(a, b)


def convert_to_frac(number):
    if not isinstance(number, Frac):
        frac = Frac(float(number).as_integer_ratio()[0], float(number).as_integer_ratio()[1])
    else:
        frac = number
    return frac


class TestFrac(unittest.TestCase):

    def setUp(self):
        self.zero = Frac(0, 1)

    def test_constructor(self):
        try:
            Frac(1, 0)
        except ValueError:
            print("Construction exception caught")

    def test_print(self):
        self.assertEqual(str(Frac(3, 5)), "3 / 5")
        self.assertEqual(repr(Frac(2, 4)), "Frac(2, 4)")

    def test_equality(self):
        self.assertTrue(Frac(1, 2) == Frac(1, 2))
        self.assertTrue(Frac(1, 2) == Frac(3, 6))
        self.assertFalse(Frac(1, 2) == Frac(-1, 2))

    def test_add_frac(self):
        self.assertTrue(Frac(1, 2) + Frac(1, 3) == Frac(5, 6))
        self.assertEqual(Frac(1, 2) + 1, Frac(3, 2))
        self.assertEqual(Frac(1, 2) + 2.0, Frac(5, 2))
        self.assertEqual(2.5 + Frac(1, 2), Frac(6, 2))
        self.assertEqual(2.5 + Frac(1, 2), Frac(3, 1))

    def test_sub_frac(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(1, 2) - 1.0, Frac(-1, 2))
        self.assertEqual(-1 - Frac(1, 2), Frac(-3, 2))

    def test_mul_frac(self):
        self.assertEqual(Frac(1, 2) * Frac(-1, 3), Frac(-1, 6))
        self.assertEqual(Frac(2, 5) * Frac(5, 1), Frac(2, 1))
        self.assertEqual(Frac(3, 8) * 4.0, Frac(3, 2))
        self.assertEqual(4 * Frac(3, 8), Frac(6, 4))

    def test_div_frac(self):
        try:
            Frac(1, 2) / 0
        except ValueError:
            print("Division exception caught")
        try:
            Frac(1, 2) / Frac(0, 0)
        except ValueError:
            print("Division exception caught")
        self.assertEqual(Frac(1, 2) / Frac(1, 3), Frac(3, 2))
        self.assertEqual(Frac(1, 3) / Frac(1, 2), Frac(2, 3))
        self.assertEqual(Frac(1, 2) / 5, Frac(1, 10))
        self.assertEqual(8.0 / Frac(1, 2), Frac(16, 1))

    def test_unary_operators(self):
        self.assertEqual(+Frac(1, 2), Frac(1, 2))
        self.assertEqual(-Frac(1, 2), Frac(-1, 2))
        self.assertEqual(~Frac(1, 2), Frac(2, 1))
        self.assertEqual(float(Frac(1, 2)), 0.5)
        self.assertEqual(float(~(-Frac(2, 8))), -4.0)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
