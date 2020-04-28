from ds_and_a.linked_list import Node


class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, item):
        node = Node(item)

        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.nxt = node
            self.tail = node

        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError

        if self.head == self.tail:
            value = self.head.value
            self.head = self.tail = null

        else:
            value = self.head.value
            second = self.head.nxt
            self.head.next = None
            self.head = second

        self.count -= 1

        return value

    def peek(self):
        if self.is_empty():
            raise IndexError

        return self.head.value

    def size(self):
        return self.count

    def is_empty(self):
        return self.head is None

    def __str__(self):
        lyst = []
        current = self.head

        while current:
            lyst.append(current.value)
            current = current.nxt

        return f"<LinkedListQueue: {lyst}>"
