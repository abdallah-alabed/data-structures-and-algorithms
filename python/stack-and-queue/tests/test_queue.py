from stack_and_queue.queue import Queue , PseudoQueue,Node
import pytest

## code challenge 10
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


# code challenge 11
def test_enqueue_one_element():
    queue = PseudoQueue()
    queue.enqueue(1)
    assert queue.__str__() == '1 -> NULL'

def test_enqueue_multi_elements():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.__str__() == '4 -> 3 -> 2 -> 1 -> NULL'

def test_dequeue_one_element():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    assert queue.__str__() == '2 -> NULL'


