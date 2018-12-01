"""
9.5 Do klasy DoubleList dopisać metody remove_max() i remove_min(), które usuwają z listy element
największy lub najmniejszy. Funkcje zwracają ten element (cały węzeł). Dla pustej listy wywołujemy wyjątek Exception.
"""

import unittest


class Node:

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:

    def __init__(self, array=None):
        self.length = 0
        self.head = None
        self.tail = None
        for element in array:
            self.insert_tail(element)

    def is_empty(self):
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, data):
        if self.head:
            node = Node(data)
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            node = Node(data)
            self.head = node
            self.tail = node
        self.length += 1

    def insert_tail(self, data):
        if self.tail:
            node = Node(data)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            node = Node(data)
            self.head = node
            self.tail = node
        self.length += 1

    def remove_head(self):
        if self.head is None:
            raise Exception("Empty list")
        elif self.head is self.tail:
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.head
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return node

    def remove_tail(self):
        if self.head is None:
            raise Exception("Empty list")
        elif self.head is self.tail:
            node = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return node

    def remove_max(self):
        max_value_node = self.max_value()
        if max_value_node == self.head:
            return self.remove_head()
        elif max_value_node == self.tail:
            return self.remove_tail()
        else:
            next_node = max_value_node.next
            previous_node = max_value_node.prev
            previous_node.next = next_node
            next_node.prev = previous_node
            max_value_node.next = max_value_node.prev = None
            return max_value_node

    def remove_min(self):
        min_value_node = self.min_value()
        if min_value_node == self.head:
            return self.remove_head()
        elif min_value_node == self.tail:
            return self.remove_tail()
        else:
            next_node = min_value_node.next
            previous_node = min_value_node.prev
            previous_node.next = next_node
            next_node.prev = previous_node
            min_value_node.next = min_value_node.prev = None
            return min_value_node

    def max_value(self):
        if self.head is None:
            raise Exception("Empty list")
        current_node = self.head
        current_max_node = self.head
        while current_node:
            if current_node.data > current_max_node.data:
                current_max_node = current_node
            current_node = current_node.next
        return current_max_node

    def min_value(self):
        if self.head is None:
            raise Exception("Empty list")
        current_node = self.head
        current_min_node = self.head
        while current_node:
            if current_node.data < current_min_node.data:
                current_min_node = current_node
            current_node = current_node.next
        return current_min_node

    def __str__(self):
        result = '[ '
        current_node = self.head
        while current_node is not None:
            result += str(current_node.data)
            result += ' '
            current_node = current_node.next
        result += ']'
        return result


class TestRemoval(unittest.TestCase):

    def test_max_removal_on_empty_list(self):
        self.assertRaises(Exception, lambda: DoublyLinkedList().remove_max())

    def test_min_removal_on_one_element_list(self):
        test_list = DoublyLinkedList([2])
        self.assertEqual(2, test_list.remove_max().data)
        self.assertTrue(test_list.is_empty())

    def test_removal_when_min_is_head(self):
        test_list = DoublyLinkedList([2, 5, 8])
        self.assertEqual(2, test_list.remove_min().data)
        self.assertEqual('[ 5 8 ]', str(test_list))

    def test_removal_when_min_is_tail(self):
        test_list = DoublyLinkedList([2, 5, 8, 1])
        self.assertEqual(1, test_list.remove_min().data)
        self.assertEqual('[ 2 5 8 ]', str(test_list))

    def test_removal_when_max_is_head(self):
        test_list = DoublyLinkedList([3.14, 1.618, 1.01])
        self.assertEqual(3.14, test_list.remove_max().data)
        self.assertEqual('[ 1.618 1.01 ]', str(test_list))

    def test_removal_when_max_is_tail(self):
        test_list = DoublyLinkedList([21.0, 37.0])
        self.assertEqual(37.0, test_list.remove_max().data)
        self.assertEqual('[ 21.0 ]', str(test_list))

    def test_various_removals(self):
        test_list = DoublyLinkedList(['making', 'out', 'test', 'data', 'is', 'fun'])
        self.assertEqual('test', test_list.remove_max().data)
        self.assertEqual('data', test_list.remove_min().data)
        self.assertEqual('[ making out is fun ]', str(test_list))
        test_list = DoublyLinkedList([1, 2, 3, 4, 5, 6])
        for i in range(test_list.length):
            self.assertEqual(i + 1, test_list.remove_min().data)


if __name__ == '__main__':
    unittest.main()
