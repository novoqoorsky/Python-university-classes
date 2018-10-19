import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({x}, {y})".format(x = self.x, y = self.y)

    def __repr__(self):
        return "Time({x}, {y})".format(x = self.x, y = self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other): 
        return self.x * other.y - self.y * other.x

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)


import unittest

class TestPoint(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(Point(3,5)), "(3, 5)")
        self.assertEqual(repr(Point(2, 4)), "Time(2, 4)")

    def test_cmp(self):
        self.assertTrue(Point(1,2) == Point(1,2))
        self.assertTrue(Point(1,2) != Point(1,3))

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(1,2), Point(2, 4))

    def test_sub(self):
        self.assertEqual(Point(1, 2) - Point(1,2), Point(0, 0))

    def test_mul(self):
        self.assertEqual(Point(-1, 2) * (Point(2, -3)), -8)

    def test_cross(self):
        self.assertEqual(Point(1, 2).cross(Point(2, 3)), -1)

    def test_length(self):
        self.assertEqual(Point(3, 4).length(), 5)
        
    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()
