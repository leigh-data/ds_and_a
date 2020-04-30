import array as arr


class PriorityQueue:
    def __init__(self):
        self._items = arr.array('i', [0 for _ in range(5)])
        self.count = 0

    def add(self, item):
        if self.is_full():
            raise IndexError

        index = self._shift_items_to_insert(item)

        self._items[index] = item
        self.count += 1

    def _shift_items_to_insert(self, item):
        index = self.count - 1

        while index >= 0:
            if self._items[index] > item:
                self._items[index + 1] = self._items[index]
                index -= 1
            else:
                break

        return index + 1

    def remove(self):
        if self.is_empty():
            raise IndexError

        self.count -= 1
        return self._items[self.count]

    def is_full(self):
        return self.count == len(self._items)

    def is_empty(self):
        return self.count == 0

    def __str__(self):
        items = [self._items[i] for i in range(self.count)]
        return f"<PriorityQueue: {items}>"
