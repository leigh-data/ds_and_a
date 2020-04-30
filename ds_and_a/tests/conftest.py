import pytest


from ds_and_a.queues import (
    ArrayQueue,
    QueueWithTwoStacks,
    reverse_queue,
    TwoQueueStack)


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


@pytest.fixture
def rq():
    queue = ArrayQueue(10)

    for i in range(1, 11):
        queue.enqueue(i)

    return queue


@pytest.fixture
def tqs():
    stack = TwoQueueStack()
    stack.push(1)

    return stack
