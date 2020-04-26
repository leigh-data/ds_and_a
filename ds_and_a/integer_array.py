import array as arr


class IntegerArray:
    def __init__(self, length):
        self._items = arr.array('i', [0 for _ in range(length)])
        self._count = length

    def insert(self, item):
        self._resize()
        self._items[self._count] = item
        self._count += 1

    def insert_at(self, item, index):
        if index < 0 or index > self._count:
            raise IndexError("The index is invalid")

        self._resize()

        for i in range(self._count, index, -1):
            self._items[i] = self._items[i-1]

        self._items[index] = item
        self._count += 1

    def remove_at(self, index):
        if index < 0 or index >= self._count:
            raise IndexError("The index is invalid")

        for i in range(index, self._count - 1):
            self._items[i] = self._items[i + 1]

        self._count -= 1

    def index_of(self, item):
        for i in range(self._count):
            if self._items[i] == item:
                return i

        return -1

    def intersection(self, other_array):
        intersection_set = IntegerArray(0)

        for item in self._items:
            if other_array.index_of(item) >= 0:
                intersection_set.insert(item)

        return intersection_set

    def reverse(self):
        n = self._count
        new_items = arr.array('i', [0 for _ in range(n)])

        for i in range(n):
            new_items[i] = self._items[n - i - 1]

        self._items = new_items

    def max(self):
        maximum = self._items[0]

        for i in range(1, self._count):
            if self._items[i] > maximum:
                maximum = self._items[i]

        return maximum

    def __str__(self):
        temp = ''
        for i in range(self._count):
            temp += str(self._items[i]) + ','
        return f"<IntegerArray: [{temp[:-1]}]>"

    def __len__(self):
        return self._count

    def _resize(self):
        if self._count == 0:
            new_items = arr.array('i', [0])
            self._items = new_items

        if len(self._items) == self._count:
            new_items = arr.array('i', [0 for _ in range(self._count * 2)])
            for i in range(self._count):
                new_items[i] = self._items[i]

            self._items = new_items
