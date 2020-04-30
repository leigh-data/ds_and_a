from collections import namedtuple


class Hashtable:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.nxt = None

    def __init__(self):
        self.n = 5
        self._entries = [None] * self.n
        self.size = 0

    def put(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self._entries[index]

        print(node)
        if node is None:
            self._entries[index] = self.Node(key, value)
            return
        else:
            # add new node to the linked list at the index
            prev = node
            while node:
                prev = node
                node = node.nxt

            prev.nxt = self.Node(key, value)

    def get(self, key):
        index = self.hash(key)
        node = self._entries[index]

        while node and node.key != key:
            node = node.nxt

        if node is None:
            return None
        else:
            return node.value

    def remove(self, key):
        index = self.hash(key)
        node = self._entries[index]
        prev = None

        while node and node.key != key:
            prev = node
            node = node.nxt

        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value

            if prev is None:
                self._entries[index] = node.nxt
            else:
                prev.nxt = prev.nxt.nxt

        return result

    def hash(self, key):
        return key % self.n
