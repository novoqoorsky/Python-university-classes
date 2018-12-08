import unittest


class Stack:

    def __init__(self, size=10):
        self.items = size * [None]
        self.n = 0
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise MemoryError("Stack overflow")
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise LookupError("Empty stack")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None
        return data


class TestStack(unittest.TestCase):

    def test_pop(self):
        stack = Stack()
        self.assertRaises(LookupError, lambda: stack.pop())
        stack.push(3)
        self.assertEqual(3, stack.pop())
        self.assertTrue(stack.is_empty())
        self.assertRaises(LookupError, lambda: stack.pop())

    def test_push(self):
        stack = Stack(size=2)
        stack.push(5)
        stack.push(7)
        self.assertRaises(MemoryError, lambda: stack.push(11))

    def test_mixed_operations(self):
        stack = Stack(size=2)
        self.assertTrue(stack.is_empty())
        stack.push(13)
        stack.push(17)
        self.assertTrue(stack.is_full())
        self.assertRaises(MemoryError, lambda: stack.push(19))
        self.assertEqual(17, stack.pop())
        stack.pop()
        self.assertTrue(stack.is_empty())
        self.assertRaises(LookupError, lambda: stack.pop())


if __name__ == '__main__':
    unittest.main()
