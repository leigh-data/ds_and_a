import pytest

from ds_and_a.queues import (
    ArrayQueue,
    QueueWithTwoStacks,
    reverse_queue,
    TwoQueueStack)


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


def test_queue_reverse(rq):
    expected_items = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
    expected_string = f"<ArrayQueue: {[item for item in expected_items]}>"

    reverse_queue(rq, 5)
    assert str(rq) == expected_string


def test_queue_reverse_error_negative_k():
    rq = ArrayQueue(10)

    with pytest.raises(ValueError):
        reverse_queue(rq, -11)


def test_queue_reverse_error_high_k(rq):

    with pytest.raises(ValueError):
        reverse_queue(rq, 11)


def test_tqs_push(tqs):
    assert tqs.size() == 1


def test_tqs_pop(tqs):
    assert tqs.pop() == 1


def test_tqs_pop_multiple_items(tqs):
    tqs.push(2)
    tqs.push(3)

    for i in range(3, 0, -1):
        assert tqs.pop() == i
        assert tqs.size() == i - 1


def test_tqs_pop_is_empty_false(tqs):
    assert tqs.is_empty() == False


def test_tqs_pop_is_empty():
    tqs = TwoQueueStack()
    assert tqs.is_empty() == True


def test_tqs__str__(tqs):
    tqs.push(2)
    tqs.push(3)

    assert str(tqs) == "<TwoQueueStack: deque([1, 2, 3])>"


def test_tqs__str__empty(tqs):
    tqs.pop()

    assert str(tqs) == "<TwoQueueStack: deque([])>"
