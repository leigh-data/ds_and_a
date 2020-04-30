import pytest

from ds_and_a.priority_queue import PriorityQueue


@pytest.fixture
def pq():
    queue = PriorityQueue()
    queue.add(1)
    queue.add(3)
    queue.add(5)
    queue.add(7)

    return queue


def test_priority_queue_add_item(pq):
    pq.add(2)
    assert "<PriorityQueue: [1, 2, 3, 5, 7]>" == str(pq)
    assert pq.count == 5


def test_priority_queue_add_item_small_value(pq):
    pq.add(-1)
    assert "<PriorityQueue: [-1, 1, 3, 5, 7]>" == str(pq)
    assert pq.count == 5


def test_priority_queue_add_item_error_full_queue(pq):
    pq.add(2)

    with pytest.raises(IndexError):
        pq.add(-1)


def test_priority_queue_delete_items(pq):
    count = pq.count - 1
    for item in range(7, 0, -2):
        assert pq.remove() == item
        assert pq.count == count
        count -= 1


def test_priority_queue_delete_items_error_empty_queue(pq):
    for item in range(7, 0, -2):
        pq.remove()

    with pytest.raises(IndexError):
        pq.remove()


def test_priority_queue_is_full(pq):
    pq.add(-1)
    assert pq.is_full() == True


def test_priority_queue_is_full_false():
    pq = PriorityQueue()
    assert pq.is_full() == False


def test_priority_queue__str__(pq):
    assert "<PriorityQueue: [1, 3, 5, 7]>" == str(pq)


def test_priority_queue__str___2_items():
    pq = PriorityQueue()
    pq.add(-1)
    pq.add(6)
    assert "<PriorityQueue: [-1, 6]>" == str(pq)


def test_priority_queue__str___no_items():
    pq = PriorityQueue()
    assert "<PriorityQueue: []>" == str(pq)
