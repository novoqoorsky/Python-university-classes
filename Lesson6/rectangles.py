from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[({x1}, {y1}), ({x2}, {y2})]".format(x1 = self.pt1.x, y1 = self.pt1.y, x2 = self.pt2.x, y2 = self.pt2.y)

    def __repr__(self):
        return "Rectangle({x1}, {y1}, {x2}, {y2})".format(x1 = self.pt1.x, y1 = self.pt1.y, x2 = self.pt2.x, y2 = self.pt2.y)

    def __eq__(self, other):
        return self.pt1.x == other.pt1.x and self.pt1.y == other.pt1.y and self.pt2.x == other.pt2.x and self.pt2.y == other.pt2.y

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)


import unittest

class TestRectangle(unittest.TestCase):

    def test_print(self):
        self.assertEqual(str(Rectangle(3, 5, 6, 8)), "[(3, 5), (6, 8)]")
        self.assertEqual(repr(Rectangle(3, 5, 6, 8)), "Rectangle(3, 5, 6, 8)")
        
    def test_cmp(self):
        self.assertTrue(Rectangle(3, 5, 6, 8) == Rectangle(3, 5, 6, 8))
        self.assertTrue(Rectangle(3, 5, 6, 8) != Rectangle(3, 5, 7, 8))

    def test_center(self):
        self.assertEqual(Rectangle(3, 5, 6, 8).center(), Point(4.5, 6.5))

    def test_area(self):
        self.assertEqual(Rectangle(3, 5, 6, 8).area(), 9)

    def test_move(self):
        self.assertEqual(Rectangle(3, 5, 6, 8).move(1, 2), Rectangle(4, 7, 7, 10))

if __name__ == "__main__":
    unittest.main() 
