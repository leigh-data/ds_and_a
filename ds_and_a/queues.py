import array as arr

from ds_and_a.stacks import Stack


class ArrayQueue:
    def __init__(self, capacity):
        self._items = arr.array('i', [0 for i in range(capacity)])
        self.n = len(self._items)
        self.count = 0
        self.rear = self.front = 0

    def enqueue(self, item):
        if self.is_full():
            raise IndexError

        self._items[self.rear] = item
        self.rear = (self.rear + 1) % self.n
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError

        item = self._items[self.front]
        self._items[self.front] = 0
        self.front = (self.front + 1) % self.n
        self.count -= 1

        return item

    def peek(self):
        if self.is_empty():
            raise IndexError

        return self._items[self.front]

    def is_full(self):
        return self.count == self.n

    def is_empty(self):
        return self.count == 0

    def __str__(self):
        return f"<ArrayQueue: {[item for item in self._items]}>"


class QueueWithTwoStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError

        self.move_stack1_to_stack2()

        return self.stack2.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError

        self.move_stack1_to_stack2()
        return self.stack2.peek()

    def move_stack1_to_stack2(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

    def __str__(self):
        return "<QueueWithTwoStacks>"
