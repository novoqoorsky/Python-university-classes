import random
import unittest


class RandomQueue:

    def __init__(self, size=5):
        self.n = size + 1
        self.items = self.n * [None]
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def insert(self, item):
        if self.is_full():
            raise MemoryError("Queue out of memory")
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.n

    def remove(self):
        if self.is_empty():
            raise LookupError("Empty queue")
        if self.head < self.tail:
            i = random.randint(self.head, self.tail - 1)
        else:
            i = random.randint(self.head, self.n - 1)
        data = self.items[i]
        self.items[i], self.items[self.head] = self.items[self.head], self.items[i]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.n
        return data


class TestRandomQueue(unittest.TestCase):

    def test_randomness(self):
        random_queue = RandomQueue()
        for x in range(5):
            random_queue.insert(x)
        for _ in range(2):
            self.assertNotEqual(None, random_queue.remove())
        for x in range(6, 8):
            random_queue.insert(x)
        for _ in range(5):
            self.assertNotEqual(None, random_queue.remove())
        self.assertTrue(random_queue.is_empty())


if __name__ == '__main__':
    unittest.main()

