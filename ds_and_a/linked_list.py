class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.nxt = nxt

    def __repr__(self):
        return f"<Node: {self.value}>"


class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0

    def is_empty(self):
        return self.first is None

    def last_item(self):
        return self.last

    def first_item(self):
        return self.first

    def add_last(self, item):
        node = Node(item)

        if self.is_empty():
            self.first = self.last = node
        else:
            self.last.nxt = node
            self.last = node

        self.count += 1

    def add_first(self, item):
        node = Node(item)

        if self.is_empty():
            self.first = self.last = node
        else:
            node.nxt = self.first
            self.first = node

        self.count += 1

    def remove_first(self):
        if self.is_empty():
            raise IndexError
        if self.first == self.last:
            self.first = self.last = None
        else:
            second = self.first.nxt
            self.first.nxt = None
            self.first = second

        self.count -= 1

    def remove_last(self):
        if self.is_empty():
            raise IndexError
        if self.last == self.first:
            self.last = self.first = None
        else:
            previous = self._get_previous(self.last)
            self.last = previous
            self.last.nxt = None

        self.count -= 1

    def index_of(self, item):
        index = 0
        current = self.first

        while current:
            if current.value == item:
                return index
            current = current.nxt
            index += 1

        return -1

    def contains(self, item):
        return self.index_of(item) != -1

    def to_list(self):
        lyst = []
        current = self.first

        while current:
            lyst.append(current.value)
            current = current.nxt

        return lyst

    def size(self):
        return self.count

    def reverse(self):
        if self.is_empty():
            return

        previous = self.first
        current = self.first.nxt

        while current:
            nxt = current.nxt
            current.nxt = previous
            previous = current
            current = nxt

        self.last = self.first
        self.last.nxt = None
        self.first = previous

    def get_kth_node_from_end(self, k):
        if self.is_empty():
            raise IndexError

        current = self.first
        advance = self.first

        for _ in range(k):
            advance = advance.nxt
            if advance is None:
                raise ValueError

        while advance != self.last:
            current = current.nxt
            advance = advance.nxt

        return current.value

    def get_middle(self):
        if self.is_empty():
            raise ValueError

        a = self.first
        b = self.first

        while b != self.last and b.nxt != self.last:
            b = b.nxt.nxt
            a = a.nxt

        if b == self.last:
            return a.value
        else:
            return (a.value, a.nxt.value)

    def has_loop(self):
        fast = self.first
        slow = self.first

        while fast != None and fast.nxt != None:
            slow = slow.nxt
            fast = fast.nxt.nxt

            if slow == fast:
                return True

        return False

    def _get_previous(self, node):
        current = self.first

        while current:
            if current.nxt == node:
                return current
            current = current.nxt

        return None
