from points import Point
import unittest


class Rectangle:
    """ A class representing rectangle """

    def __init__(self, x1, y1, x2, y2):
        if x1 > x2:
            raise ValueError("x1 cannot be greater than x2!")
        if y1 > y2:
            raise ValueError("y1 cannot be greater than y2!")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[({x1}, {y1}), ({x2}, {y2})]".format(x1=self.pt1.x, y1=self.pt1.y,
                                                     x2=self.pt2.x, y2=self.pt2.y)

    def __repr__(self):
        return "Rectangle({x1}, {y1}, {x2}, {y2})".format(x1=self.pt1.x, y1=self.pt1.y,
                                                          x2=self.pt2.x, y2=self.pt2.y)

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

    def intersection(self, other):
        if self.pt1.x > other.pt2.x or other.pt1.x > self.pt2.x or self.pt1.y > other.pt2.y or other.pt1.y > self.pt2.y:
            return Rectangle(0, 0, 0, 0)    # no intersection
        return Rectangle(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y),
                         min(self.pt2.x, other.pt2.x), min(self.pt2.y, other.pt2.y))

    def cover(self, other):
        return Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y),
                         max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))

    def make4(self):
        center = self.center()
        return [Rectangle(self.pt1.x, self.pt1.y, center.x, center.y),
                Rectangle(center.x, center.y, self.pt2.x, self.pt2.y),
                Rectangle(self.pt1.x, center.y, center.x, self.pt2.y),
                Rectangle(center.x, self.pt1.y, self.pt2.x, center.y)]


class TestRectangle(unittest.TestCase):

    def test_construction(self):
        try:
            Rectangle(2, 3, 1, 4)
        except ValueError:
            print("Construction exception caught")
        try:
            Rectangle(2, 4, 1, 3)
        except ValueError:
            print("Construction exception caught")
        try:
            Rectangle(2, 3, 4, 5)
        except ValueError:
            print("Construction exception caught")

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

    def test_intersection(self):
        self.assertEqual(Rectangle(0, 0, 3, 3).intersection(Rectangle(4, 1, 5, 5)), Rectangle(0, 0, 0, 0))
        self.assertEqual(Rectangle(0, 0, 3, 3).intersection(Rectangle(4, 0, 6, 3)), Rectangle(0, 0, 0, 0))
        self.assertEqual(Rectangle(0, 0, 3, 3).intersection(Rectangle(3.01, 0, 6, 3)), Rectangle(0, 0, 0, 0))
        self.assertEqual(Rectangle(0, 0, 3, 3).intersection(Rectangle(-3, -3, 0, 0)), Rectangle(0, 0, 0, 0))
        self.assertEqual(Rectangle(-5, -5, -4, -1).intersection(Rectangle(-3, -3, 0, 0)), Rectangle(0, 0, 0, 0))
        self.assertEqual(Rectangle(0, 0, 3, 3).intersection(Rectangle(2, 2, 4, 4)), Rectangle(2, 2, 3, 3))
        self.assertEqual(Rectangle(-4, 1, 3, 4).intersection(Rectangle(2, 0, 4, 1)), Rectangle(2, 1, 3, 1))
        self.assertEqual(Rectangle(-2, -3, 4, 1).intersection(Rectangle(0, -1, 1, 0)), Rectangle(0, -1, 1, 0))
        self.assertEqual(Rectangle(-2, -3, 4, 1).intersection(Rectangle(1, -3, 4, -2)), Rectangle(1, -3, 4, -2))

    def test_cover(self):
        self.assertEqual(Rectangle(-2, -3, 4, 1).cover(Rectangle(0, -1, 1, 0)), Rectangle(-2, -3, 4, 1))
        self.assertEqual(Rectangle(-2, -3, 4, 1).cover(Rectangle(1, -3, 4, -2)), Rectangle(-2, -3, 4, 1))
        self.assertEqual(Rectangle(0, 0, 3, 3).cover(Rectangle(2, 2, 4, 4)), Rectangle(0, 0, 4, 4))
        self.assertEqual(Rectangle(0, 0, 3, 3).cover(Rectangle(4, 1, 5, 5)), Rectangle(0, 0, 5, 5))
        self.assertEqual(Rectangle(-2, -4, 3, 5).cover(Rectangle(1, -7, 6, 3)), Rectangle(-2, -7, 6, 5))

    def test_make4(self):
        self.assertTrue(Rectangle(0, 0, 2, 2) in Rectangle(-2, -2, 2, 2).make4())
        self.assertTrue(Rectangle(0, 0, 3, 3) not in Rectangle(-2, -2, 2, 2).make4())
        self.assertTrue(Rectangle(-3, -5, 1, 1) in Rectangle(-3, -5, 5, 7).make4())
        self.assertTrue(Rectangle(-3, 1, 1, 7) in Rectangle(-3, -5, 5, 7).make4())
        self.assertTrue(Rectangle(1, 1, 5, 7) in Rectangle(-3, -5, 5, 7).make4())
        self.assertTrue(Rectangle(1, -5, 5, 1) in Rectangle(-3, -5, 5, 7).make4())
        self.assertTrue(Rectangle(21, 69, 37, 2115) not in Rectangle(-3, -5, 5, 7).make4())


if __name__ == "__main__":
    unittest.main()
