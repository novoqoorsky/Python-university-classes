import unittest


class Queue:

    def __init__(self, size=5):
        self.n = size + 1
        self.items = self.n * [None]
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise MemoryError("Queue out of memory")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise LookupError("Empty queue")
        data = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.n
        return data


class TestStack(unittest.TestCase):

    def test_get(self):
        queue = Queue(size=2)
        self.assertRaises(LookupError, lambda: queue.get())
        queue.put(3)
        queue.put(5)
        self.assertEqual(3, queue.get())
        queue.put(7)
        self.assertEqual(5, queue.get())
        self.assertEqual(7, queue.get())
        self.assertTrue(queue.is_empty())

    def test_put(self):
        queue = Queue(size=2)
        queue.put(13)
        queue.put(17)
        self.assertRaises(MemoryError, lambda: queue.put(19))
        x = queue.get()
        queue.put(x)
        queue.get()
        self.assertEqual(x, queue.get())


if __name__ == '__main__':
    unittest.main()
