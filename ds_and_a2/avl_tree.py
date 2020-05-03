class AVLTree:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left
            self.height = 0

        def __str__(self):
            return f"<AVLTree->Node: {self.calue}>"

    def __init__(self):
        self.root = None

    def insert(self, value):
        def recurse(node, value):
            if node is None:
                return self.Node(value)

            if value < node.value:
                node.left = recurse(node.left, value)
            else:
                node.right = recurse(node.right, value)

            # node.height = MAX(left, right)
            node.height = max(
                self.height(node.left),
                self.height(node.right) + 1
            )

            return node
        # balance factor: height of left - height of right

        self.root = recurse(self.root, value)

    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height


tree = AVLTree()
tree.insert(10)
tree.insert(5)
tree.insert(30)
print("END")
