from stack_and_queue.queue import Queue
import pytest

def test_enqueue_onto_queue():
    queue=Queue()
    queue.enqueue(1)
    assert queue.rear.value == 1

def test_enqueue_multiple_values_onto_queue():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.rear.value == 3

def test_dequeue_off_queue():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    assert queue.front.value == 2


def test_peek_the_queue():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.peek() == 1

def test_empty_queue():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    assert queue.is_empty() == False
    queue.dequeue()
    assert queue.is_empty() == True

def test_instantiate_an_empty_queue():
    queue=Queue()
    assert queue

def test_Queue_empty_exception():
    queue = Queue()
    with pytest.raises(Exception):
        assert queue.peek()
    with pytest.raises(Exception):
        assert queue.dequeue()
