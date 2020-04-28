import pytest

from ds_and_a.linked_list_queue import LinkedListQueue


@pytest.fixture
def queue():
    queue = LinkedListQueue()

    for i in range(1, 11):
        queue.enqueue(i)

    return queue


def test_llc_enqueue(queue):
    initial_count = queue.size()
    queue.enqueue(11)

    assert queue.count == initial_count + 1


def test_llc_dequeue(queue):
    initial_count = queue.size()

    assert queue.dequeue() == 1
    assert queue.count == initial_count - 1


def test_llc_peek(queue):
    assert queue.peek() == 1


def test_llc_peek_empty_error():
    queue = LinkedListQueue()

    with pytest.raises(IndexError):
        assert queue.peek()


def test_llc_is_empty_false(queue):
    assert not queue.is_empty()


def test_llc_is_empty_true():
    queue = LinkedListQueue()
    assert queue.is_empty()


def test__str__(queue):
    expected_items = [i for i in range(1, 11)]
    expected_string = f"<LinkedListQueue: {expected_items}>"

    assert str(queue) == expected_string


def test__str__():
    expected_items = [1]
    expected_string = f"<LinkedListQueue: {expected_items}>"
    queue = LinkedListQueue()
    queue.enqueue(1)

    assert str(queue) == expected_string
