import pytest

from ds_and_a.integer_array import IntegerArray


def test_create_integer_array_empty():
    int_array = IntegerArray(0)
    assert len(int_array) == 0


def test_create_integer_with_three():
    int_array = IntegerArray(3)
    assert len(int_array) == 3


def test_index_of_one_item_array():
    int_array = IntegerArray(1)
    assert int_array.index_of(0) == 0


def test_insert_at_empty_array():
    int_array = IntegerArray(0)
    int_array.insert_at(1, 0)
    assert len(int_array) == 1


def test_insert_at_two_item_array():
    int_array = IntegerArray(2)
    int_array.insert_at(1, 1)
    assert int_array.index_of(1) == 1
    assert int_array.index_of(0) == 0


def test_insert_at_bad_index_negative_number():
    int_array = IntegerArray(0)

    with pytest.raises(IndexError):
        int_array.insert_at(5, -1)


def test_insert_at_bad_index_high_index():
    int_array = IntegerArray(0)

    with pytest.raises(IndexError):
        int_array.insert_at(1, 6)


def test_insert_empty_array():
    int_array = IntegerArray(0)
    int_array.insert(1)
    assert int_array.index_of(1) == 0


def test_insert_three_item_array():
    int_array = IntegerArray(3)
    int_array.insert(3)
    assert len(int_array) == 4
    assert int_array.index_of(3) == 3


def test_remove_at_three_item_array():
    int_array = IntegerArray(0)
    int_array.insert(1)
    int_array.insert(2)
    int_array.insert(3)

    int_array.remove_at(1)
    assert len(int_array) == 2


def test_remove_at_error_high_index():
    int_array = IntegerArray(0)
    int_array.insert(1)
    int_array.insert(2)
    int_array.insert(3)

    with pytest.raises(IndexError):
        int_array.remove_at(6)


def test_remove_at_negative_index():
    int_array = IntegerArray(0)

    with pytest.raises(IndexError):
        int_array.remove_at(-1)


def test_intersection_two_elements():
    other_array = IntegerArray(0)
    other_array.insert(5)
    other_array.insert(6)
    other_array.insert(7)
    other_array.insert(8)

    int_array = IntegerArray(0)
    int_array.insert(3)
    int_array.insert(4)
    int_array.insert(5)
    int_array.insert(6)

    results = int_array.intersection(other_array)
    assert len(results) == 2


def test_intersection_empty_array():
    other_array = IntegerArray(0)
    other_array.insert(5)
    other_array.insert(6)
    other_array.insert(7)
    other_array.insert(8)

    int_array = IntegerArray(0)
    int_array.insert(1)
    int_array.insert(2)
    int_array.insert(3)
    int_array.insert(4)

    results = int_array.intersection(other_array)
    assert len(results) == 0


def test_reverse():
    int_array = IntegerArray(0)
    int_array.insert(5)
    int_array.insert(6)
    int_array.insert(7)
    int_array.insert(8)
    int_array.reverse()

    assert str(int_array) == "<IntegerArray: [8,7,6,5]>"


def test_max_first_element():
    int_array = IntegerArray(0)
    int_array.insert(1000)
    int_array.insert(6)
    int_array.insert(7)
    int_array.insert(8)

    assert int_array.max() == 1000


def test_max_middle_element():
    int_array = IntegerArray(0)
    int_array.insert(5)
    int_array.insert(6)
    int_array.insert(1000)
    int_array.insert(7)
    int_array.insert(8)

    assert int_array.max() == 1000


def test__len__empty_array():
    int_array = IntegerArray(0)

    assert len(int_array) == 0


def test__len__multiple_items():
    int_array = IntegerArray(0)
    int_array.insert(5)
    int_array.insert(6)
    int_array.insert(7)

    assert len(int_array) == 3


def test__len__multiple_init():
    int_array = IntegerArray(3)

    assert len(int_array) == 3


def test__str__empty():
    int_array = IntegerArray(0)

    assert str(int_array) == "<IntegerArray: []>"


def test__str__multiple_items():
    int_array = IntegerArray(0)
    int_array.insert(8)
    int_array.insert(7)
    int_array.insert(6)
    int_array.insert(5)

    assert str(int_array) == "<IntegerArray: [8,7,6,5]>"


def test__str__multiple_initializer():
    int_array = IntegerArray(3)
    assert str(int_array) == "<IntegerArray: [0,0,0]>"
