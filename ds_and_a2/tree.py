class Tree:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

        def __str__(self):
            return f"<Node: {self.value}>"

    def __init__(self):
        self.root = None

    def insert(self, value):
        node = self.Node(value)
        if self.root is None:
            self.root = node
            return

        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right

    def find(self, value):
        current = self.root

        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True

        return False

    def traverse_preorder(self):
        values = []

        def traverse(node):
            if node is None:
                return

            values.append(node.value)
            traverse(node.left)
            traverse(node.right)

        traverse(self.root)
        return values

    def traverse_inorder(self):
        values = []

        def traverse(node):
            if node is None:
                return

            traverse(node.left)
            values.append(node.value)
            traverse(node.right)

        traverse(self.root)
        return values

    def traverse_postorder(self):
        values = []

        def traverse(node):
            if node is None:
                return

            traverse(node.left)
            traverse(node.right)
            values.append(node.value)

        traverse(self.root)
        return values

    def height(self):
        def recurse(node):
            if node is None:
                return -1

            if self.is_leaf(node):
                return 0

            return 1 + max(recurse(node.left), recurse(node.right))

        return recurse(self.root)

    def is_leaf(self, node):
        return node.left is None and node.right is None

    def minimum(self):
        current = self.root

        while current.left is not None:
            current = current.left

        return current.value

    def minimum_recursive(self):
        def recurse(node):
            if node.left is None:
                return node.value

            return recurse(node.left)

        return recurse(self.root)

    def is_bst(self):
        p_inf = float("inf")
        n_inf = float("-inf")

        def recurse(node, minimum, maximum):
            if node is None:
                return True

            if node.value < minimum or node.value > maximum:
                return False

            return recurse(node.left, minimum, node.value - 1) and recurse(node.right, node.value + 1, maximum)

        return recurse(self.root, n_inf, p_inf)

    def get_at_k_distance(self, distance):
        lyst = list()

        def recurse(node, distance, lyst):
            if node is None:
                return
            if distance == 0:
                lyst.append(node.value)

            recurse(node.left, distance - 1, lyst)
            recurse(node.right, distance-1, lyst)

        recurse(self.root, distance, lyst)

        return lyst

    def size(self):
        def recurse(node):
            if node is None:
                return 0

            if self.is_leaf(node):
                return 1

            return 1 + recurse(node.left) + recurse(node.right)

        return recurse(self.root)

    def count_leaves(self):
        def recurse(node):
            if node is None:
                return 0

            if self.is_leaf(node):
                return 1

            return recurse(node.left) + recurse(node.right)

        return recurse(self.root)

    def maximum_recursive(self):
        def recurse(node):
            if node.right is None:
                return node.value

            return recurse(node.right)

        return recurse(self.root)

    def contains(self, value):

        def recurse(node, value):
            if node is None:
                return False

            if node.value == value:
                return True

            return recurse(node.left, value) or recurse(node.right, value)

        return recurse(self.root, value)

        return

    def __eq__(self, other):
        def recurse(first, second):
            if first is None and second is None:
                return True

            if first is not None and second is not None:
                return first.value == second.value and recurse(first.left, second.left) and recurse(first.right, second.right)

            return False

        if other is None:
            return False

        return recurse(self.root, other.root)

    # def are_siblings(self,)
