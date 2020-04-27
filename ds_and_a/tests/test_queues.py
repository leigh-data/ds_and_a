import pytest

from ds_and_a.queues import ArrayQueue, QueueWithTwoStacks


@pytest.fixture
def aq():
    queue = ArrayQueue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    return queue


@pytest.fixture
def qts():
    queue = QueueWithTwoStacks()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    return queue


def test_array_queue_is_empty():
    queue = ArrayQueue(5)
    assert queue.is_empty() == True


def test_array_queue_is_empty(aq):
    assert aq.is_empty() == False


def test_array_queue_is_full(aq):
    aq.enqueue(5)
    aq.enqueue(3)

    assert aq.is_full() == True


def test_array_queue_is_not_full(aq):
    assert aq.is_full() == False


def test_array_queue_dequeue(aq):
    assert aq.dequeue() == 1
    assert aq.dequeue() == 2
    assert aq.dequeue() == 3

    with pytest.raises(IndexError):
        aq.dequeue()


def test_array_queue_enqueue_error_full_capacity(aq):
    aq.enqueue(1)
    aq.enqueue(1)

    with pytest.raises(IndexError):
        aq.enqueue(3)


def test_array_queue_enqueue():
    aq = ArrayQueue(1)
    aq.enqueue(6)

    assert aq.dequeue() == 6


def test_array_queue_str(aq):
    assert str(aq) == f"<ArrayQueue: {[item for item in aq._items]}>"


def test_qts_dequeue(qts):
    for index in range(3):
        assert qts.dequeue() == (index + 1)


def test_qts_dequeue_error_empty():
    qts = QueueWithTwoStacks()

    with pytest.raises(IndexError):
        qts.dequeue()


def test_qts_enqueue():
    qts = QueueWithTwoStacks()
    qts.enqueue(6)
    assert qts.dequeue() == 6


def test_qts_peek(qts):
    assert qts.peek() == 1


def test_qts_peek_empty_stack_error():
    qts = QueueWithTwoStacks()

    with pytest.raises(IndexError):
        qts.peek()


def test_qts_is_empty_with_items(qts):
    assert qts.is_empty() == False


def test_qts_is_empty_without_items():
    qts = QueueWithTwoStacks()
    assert qts.is_empty() == True


def test_qts___str__(qts):
    assert str(qts) == "<QueueWithTwoStacks>"
