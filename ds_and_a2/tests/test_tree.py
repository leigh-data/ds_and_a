import pytest

from ds_and_a2.tree import Tree


@pytest.fixture
def basic_tree():
    tree = Tree()
    tree.insert(5)

    return tree


@pytest.fixture
def full_tree():
    tree = Tree()
    tree.insert(7)
    tree.insert(4)
    tree.insert(9)
    tree.insert(1)
    tree.insert(6)
    tree.insert(8)
    tree.insert(10)

    return tree


@pytest.fixture
def traversal_tree():
    tree = Tree()
    tree.insert(20)
    tree.insert(10)
    tree.insert(30)
    tree.insert(6)
    tree.insert(14)
    tree.insert(24)
    tree.insert(3)
    tree.insert(8)
    tree.insert(26)

    return tree


def test_node__str__():
    node = Tree.Node(1)
    assert str(node) == "<Node: 1>"


def test_node_children():
    left = Tree.Node(1)
    right = Tree.Node(3)
    parent = Tree.Node(2, left, right)

    assert parent.left == left
    assert parent.right == right


def test_tree_insert_root_is_none(basic_tree):
    assert basic_tree.root.value == 5


def test_tree_insert_lower_value(basic_tree):
    basic_tree.insert(2)
    assert basic_tree.root.left.value == 2


def test_tree_insert_higher_value(basic_tree):
    basic_tree.insert(7)
    assert basic_tree.root.right.value == 7


@pytest.mark.parametrize("value", [7, 4, 9, 1, 6, 8, 10])
def test_tree_find(full_tree, value):
    assert full_tree.find(value) == True


@pytest.mark.parametrize("value", [12, 3, 13, 2, 5, 11])
def test_tree_find_all_false(full_tree, value):
    assert full_tree.find(value) == False


def test_tree_traverse_preorder(traversal_tree):
    assert traversal_tree.traverse_preorder(
    ) == [20, 10, 6, 3, 8, 14, 30, 24, 26]


def test_tree_traverse_inorder(traversal_tree):
    assert traversal_tree.traverse_inorder(
    ) == [3, 6, 8, 10, 14, 20, 24, 26, 30]


def test_tree_traverse_postorder(traversal_tree):
    assert traversal_tree.traverse_postorder(
    ) == [3, 8, 6, 14, 10, 26, 24, 30, 20]


def test_tree_height(full_tree):
    assert full_tree.height() == 2


def test_tree_minimum(full_tree):
    assert full_tree.minimum() == 1


def test_tree_minimum_traversal_tree(traversal_tree):
    assert traversal_tree.minimum() == 3


def test_tree_minimum_recursice(full_tree):
    assert full_tree.minimum() == 1


def test_tree_minimum_recursive_traversal_tree(traversal_tree):
    assert traversal_tree.minimum() == 3


def test__eq__(full_tree):
    tree = Tree()
    tree.insert(7)
    tree.insert(4)
    tree.insert(9)
    tree.insert(1)
    tree.insert(6)
    tree.insert(8)
    tree.insert(10)

    assert tree == full_tree


def test__eq___not_equal(full_tree, traversal_tree):
    assert not traversal_tree == full_tree


def test__eq__not_equal_different_tree(full_tree):
    tree = Tree()
    tree.insert(7)
    tree.insert(4)
    tree.insert(9)
    tree.insert(1)
    tree.insert(6)
    tree.insert(8)
    tree.insert(10)
    tree.insert(16)

    assert not tree == full_tree


def test_is_bst(full_tree):
    assert full_tree.is_bst() == True


def test_is_bst_travesal_tree(traversal_tree):
    assert traversal_tree.is_bst() == True


def test_is_bst_false(full_tree):
    full_tree.root.right.value = -15
    assert not full_tree.is_bst()


def test_is_bst_false(full_tree):
    full_tree.root.left.value = 77777777
    assert not full_tree.is_bst()


def test_get_at_k_distance_0(full_tree):
    assert full_tree.get_at_k_distance(0) == [7]


def test_get_at_k_distance_1(full_tree):
    assert full_tree.get_at_k_distance(1) == [4, 9]


def test_get_at_k_distance_2(full_tree):
    assert full_tree.get_at_k_distance(2) == [1, 6, 8, 10]


def test_get_at_k_distance_3(full_tree):
    assert full_tree.get_at_k_distance(3) == []


def test_get_at_k_distance_30(full_tree):
    assert full_tree.get_at_k_distance(30) == []


def test_size_full_tree(full_tree):
    assert full_tree.size() == 7


def test_size_empty_tree():
    tree = Tree()
    assert tree.size() == 0


def test_size_one_node_tree():
    tree = Tree()
    tree.insert(4)
    assert tree.size() == 1


def test_count_leaves_full_tree(full_tree):
    assert full_tree.count_leaves() == 4


def test_count_leaves_empty_tree():
    tree = Tree()
    assert tree.count_leaves() == 0


def test_count_leaves_one_node_tree():
    tree = Tree()
    tree.insert(4)
    assert tree.count_leaves() == 1


def test_maximum_recursive_full_tree(full_tree):
    assert full_tree.maximum_recursive() == 10


def test_maximum_recursive_traversal_tree(traversal_tree):
    assert traversal_tree.maximum_recursive() == 30


@pytest.mark.parametrize("value", [7, 4, 9, 1, 6, 8, 10])
def test_tree_contains(full_tree, value):
    assert full_tree.contains(value) == True


@pytest.mark.parametrize("value", [12, 3, 13, 2, 5, 11])
def test_tree_contains_all_false(full_tree, value):
    assert full_tree.contains(value) == False
