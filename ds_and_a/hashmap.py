class HashMap:
    class Node:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value

        def __str__(self):
            return f"<Node: {self.value}>"

        def __repr__(self):
            return str(self)

    def __init__(self):
        self._entries = [self.Node()] * 5
        self.count = 0

    def put(self, key, value):
        entry = self.get_entry(key)
        index = self.get_index(key)
        if entry != None:
            entry.value = value
            return

        if self.count == len(self._entries):
            raise IndexError

        self._entries[index] = self.Node(key, value)
        self.count += 1

    def get(self, key):
        entry = self.get_entry(key)
        if entry is not None:
            return entry.value
        else:
            return None

    def remove(self, key):
        index = self.get_index(key)

        if index == -1 or self._entries[index] is None:
            return

        self._entries[index] = None
        self.count -= 1

    def size(self):
        return self.count

    def _index(self, key, i):
        return (hash(key) + i) % len(self._entries)

    def get_index(self, key):
        steps = 0
        n = len(self._entries)

        while steps < n:
            index = self._index(key, steps)
            entry = self._entries[index]
            steps += 1
            if entry == None or entry.key == key:
                return index

        return -1

    def get_entry(self, key):
        index = self.get_index(key)
        if index >= 0:
            return self._entries[index]
        else:
            return None

    def __str__(self):
        temp = str([str(node) for node in self._entries])
        return f"<HashMap: [<Node: {temp}]>"
