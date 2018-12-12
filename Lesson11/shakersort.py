import random
import unittest


def cmp(a, b):
    return (a > b) - (a < b)


def swap(L, x, y):
    L[x], L[y] = L[y], L[x]


def shaker_sort(L, left, right, cmpfunc=cmp):
    k = right
    while left < right:
        for j in range(right, left, -1):
            if cmpfunc(L[j-1], L[j]) > 0:
                swap(L, j-1, j)
                k = j
        left = k
        for j in range(left, right):
            if cmpfunc(L[j], L[j+1]) > 0:
                swap(L, j, j+1)
                k = j
        right = k


class ComparisonFunctionsTest(unittest.TestCase):

    def test_standard_comparison(self):
        n = 100
        test_list = list(range(n))
        random.shuffle(test_list)
        shaker_sort(test_list, 0, n - 1)
        self.assertEqual(test_list, list(range(n)))

    def test_reverse_order(self):
        n = 100
        test_list = list(range(n))
        random.shuffle(test_list)
        shaker_sort(test_list, 0, n - 1, cmpfunc=lambda x, y: -cmp(x, y))
        self.assertEqual(test_list, list(range(n - 1, -1, -1)))


if __name__ == '__main__':
    unittest.main()
