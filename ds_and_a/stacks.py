import array as arr


BRACKETS = {'[': ']', '{': '}', '(': ')', '<': '>'}


def string_reverser(str1):
    str1 = str1.strip()
    stack = list()
    reversed = ""

    if not str1:
        raise ValueError

    for char in str1:
        stack.append(char)

    while stack:
        reversed += stack.pop()

    return reversed


def balanced(expression):
    stack = list()

    for char in expression:
        if char in BRACKETS:
            stack.append(BRACKETS[char])

        elif char.isalnum():
            continue

        elif not stack or char != stack.pop():
            return False

    return not stack


class Stack:
    def __init__(self):
        self._items = arr.array('i', [])

    def push(self, item):
        self._items.append(item)

    def pop(self):
        try:
            return self._items.pop()
        except IndexError:
            return None

    def peek(self):
        try:
            return self._items[-1]
        except IndexError:
            return None

    def is_empty(self):
        return len(self._items) == 0

    def __str__(self):
        items = [item for item in reversed(self._items)]
        return f"<Stack: {items}>"


class TwoStacks:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError

        self._items = arr.array('i', [0 for i in range(capacity)])
        self.top1 = -1
        self.top2 = capacity

    def push1(self, item):
        if self.is_full1():
            raise IndexError

        self.top1 += 1
        self._items[self.top1] = item

        return self._items[self.top1]

    def pop1(self):
        if self.is_empty1():
            raise IndexError

        item = self._items[self.top1]
        self.top1 = self.top1 - 1
        return item

    def push2(self, item):
        if self.is_full2():
            return IndexError

        self.top2 -= 1
        self._items[self.top2] = item

    def pop2(self):
        if self.is_empty2():
            return IndexError

        item = self._items[self.top2]
        self.top2 += 1
        return item

    def is_empty1(self):
        return self.top1 == -1

    def is_full1(self):
        return self.top1 + 1 == self.top2

    def is_full2(self):
        return self.top2 - 1 == self.top1

    def is_empty2(self):
        return self.top2 == len(self._items)


class MinStack:
    def __init__(self):
        self.stack = Stack()
        self.min_stack = Stack()

    def push(self, value):
        self.stack.push(value)

        if self.min_stack.is_empty():
            self.min_stack.push(value)
        elif value < self.min_stack.peek():
            self.min_stack.push(value)

    def pop(self):
        if self.stack.is_empty():
            raise IndexError

        top = self.stack.pop()

        if self.min_stack.peek() == top:
            self.min_stack.pop()

        return top

    def min(self):
        return self.min_stack.peek()
