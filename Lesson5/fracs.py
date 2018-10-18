from math import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)

def add_frac(frac1, frac2):
    the_lcm = lcm(frac1[1], frac2[1])
    frac1_extended = [frac1[0] * (the_lcm / frac1[1]), the_lcm]
    frac2_extended = [frac2[0] * (the_lcm / frac2[1]), the_lcm]
    return [frac1_extended[0] + frac2_extended[0], the_lcm]

def sub_frac(frac1, frac2):
    return add_frac(frac1, [-frac2[0], frac2[1]])

def mul_frac(frac1, frac2):
    return [frac1[0] * frac2[0], frac1[1] * frac2[1]]

def div_frac(frac1, frac2):
    return mul_frac(frac1, [frac2[1], frac2[0]])

def is_positive(frac):
    return frac[0] > 0 and frac[1] > 0 or (frac[0] < 0 and frac[1] < 0)

def is_zero(frac):
    return frac[0] == 0

def cmp_frac(frac1, frac2):
    the_lcm = lcm(frac1[1], frac2[1])
    frac1_numerator = frac1[0] * (the_lcm / frac1[1])
    frac2_numerator = frac2[0] * (the_lcm / frac2[1])
    if frac1_numerator == frac2_numerator: return 0
    elif frac1_numerator > frac2_numerator: return 1
    else: return -1

def frac2float(frac):
    return frac[0] / frac[1]

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])

    def test_is_positive(self):
        self.assertEqual(is_positive([-1, 2]), False)
        self.assertEqual(is_positive([1, 2]), True)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 3]), True)
        self.assertEqual(is_zero([1, 3]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 2]), 0)
        self.assertEqual(cmp_frac([1, 2], [3, 6]), 0)
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 2], [3, 4]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)

    def test_mixed_operations(self):
        self.assertEqual(cmp_frac(add_frac([12, 49], [7, 56]),
                                  mul_frac([99, 100], [32, 35])), -1)
        self.assertEqual(cmp_frac(sub_frac([4, 5], [1, 4]),
                                  div_frac([1, 1], [100, 55])), 0)
        self.assertEqual(frac2float(sub_frac([12, 10], [0, 1])), 1.2)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()
