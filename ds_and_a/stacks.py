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
