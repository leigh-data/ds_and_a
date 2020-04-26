import pytest

from ds_and_a.linked_list import LinkedList


@pytest.fixture
def linked_list():
    test_list = LinkedList()
    test_list.add_last(1)
    test_list.add_last(2)
    test_list.add_last(3)

    return test_list


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def looped_list(linked_list):

    node = linked_list.last
    linked_list.add_last(4)
    linked_list.add_last(5)

    linked_list.last.nxt = node
    return linked_list


def test__repr__(linked_list):
    first = linked_list.first_item()
    rep_string = f"<Node: {first.value}>"
    assert str(first) == rep_string


def test_add_first_new_list(empty_list):
    empty_list.add_first(1)

    assert empty_list.size() == 1


def test_add_first_existing_list():
    linked_list = LinkedList()
    linked_list.add_first(1)
    linked_list.add_first(2)

    assert linked_list.size() == 2


def test_to_list_empty_list(empty_list):
    lyst = empty_list.to_list()

    assert lyst == []


def test_to_list_one_item(empty_list):
    empty_list.add_first(1)

    lyst = empty_list.to_list()

    assert lyst == [1]


def test_to_list_many_items(empty_list):
    item_list = [1, 2, 3]

    for item in item_list:
        empty_list.add_last(item)

    assert empty_list.to_list() == item_list


def test_add_last_new_list(empty_list):
    empty_list.add_last(1)

    assert empty_list.size() == 1
    assert empty_list.to_list() == [1]


def test_add_last_existing_list(empty_list):
    empty_list.add_last(1)
    empty_list.add_last(2)

    assert empty_list.size() == 2
    assert empty_list.to_list() == [1, 2]


def test_remove_first_one_node(empty_list):
    empty_list.add_first(1)
    empty_list.remove_first()
    assert empty_list.to_list() == []


def test_remove_first_two_item_list(empty_list):
    empty_list.add_last(1)
    empty_list.add_last(2)
    empty_list.remove_first()

    assert empty_list.size() == 1
    assert empty_list.to_list() == [2]


def test_remove_first_three_item_list(linked_list):
    linked_list.remove_first()

    assert linked_list.size() == 2
    assert linked_list.to_list() == [2, 3]


def test_remove_first_error_empty_list(empty_list):
    with pytest.raises(IndexError):
        empty_list.remove_first()


def test_remove_last_one_node(empty_list):
    empty_list.add_first(1)
    empty_list.remove_last()

    assert empty_list.to_list() == []


def test_remove_last_two_item_list(empty_list):
    empty_list.add_last(1)
    empty_list.add_last(2)
    empty_list.remove_last()

    assert empty_list.size() == 1
    assert empty_list.to_list() == [1]


def test_remove_last_three_item_list(linked_list):
    linked_list.remove_last()

    assert linked_list.size() == 2
    assert linked_list.to_list() == [1, 2]


def test_remove_last_error(empty_list):
    with pytest.raises(IndexError):
        empty_list.remove_last()


def test_index_of_three_item_list(linked_list):
    assert linked_list.index_of(2) == 1


def test_index_of_three_item_list_non_existent_value(linked_list):
    assert linked_list.index_of(4) == -1


def tet_index_of_one_item_list(empty_list):
    empty_list.add_last(1)

    assert empty_list.index_of(1) == 0


def test_contains_three_item_list(linked_list):
    assert linked_list.contains(2)


def test_contains_three_item_list_non_existent_value(linked_list):
    assert not linked_list.contains(4)


def test_last_item_three_item_list(linked_list):
    assert linked_list.last_item().value == 3


def test_last_empty_list(empty_list):
    assert empty_list.last_item() is None


def test_first_item_three_item_list(linked_list):
    assert linked_list.first_item().value == 1


def test_first_empty_list(empty_list):
    assert empty_list.first_item() is None


def test__get_previous_one_item_list(empty_list):
    linked_list = empty_list
    linked_list.add_first(1)
    node = linked_list.first_item()

    assert linked_list._get_previous(node) is None


def test_reverse(linked_list):
    linked_list.reverse()

    assert linked_list.to_list() == [3, 2, 1]


def test_reverse_even_elements(linked_list):
    linked_list.add_last(4)
    linked_list.reverse()

    assert linked_list.to_list() == [4, 3, 2, 1]


def test_reverse_empty_list(empty_list):
    empty_list.reverse()

    assert empty_list.to_list() == []


def test_get_kth_node(linked_list):
    linked_list.add_last(4)
    linked_list.add_last(5)

    assert linked_list.get_kth_node_from_end(0) == 5
    assert linked_list.get_kth_node_from_end(1) == 4
    assert linked_list.get_kth_node_from_end(2) == 3
    assert linked_list.get_kth_node_from_end(3) == 2
    assert linked_list.get_kth_node_from_end(4) == 1


def test_get_kth_node_too_high_k(linked_list):
    linked_list.add_last(4)
    linked_list.add_last(5)

    with pytest.raises(ValueError):
        linked_list.get_kth_node_from_end(6)


def test_get_kth_node_empty(empty_list):
    with pytest.raises(IndexError):
        empty_list.get_kth_node_from_end(6)


def test_get_middle(linked_list):
    assert linked_list.get_middle() == 2


def test_get_middle_even(linked_list):
    linked_list.add_last(4)
    assert linked_list.get_middle() == (2, 3)


def test_get_middle_error(empty_list):
    with pytest.raises(ValueError):
        empty_list.get_middle()


def test_has_loop(looped_list):
    assert looped_list.has_loop() == True


def test_does_not_have_loop(linked_list):
    assert linked_list.has_loop() == False
