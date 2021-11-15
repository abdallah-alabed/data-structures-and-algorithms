from stack_and_queue.queue import Queue , PseudoQueue,Node,AnimalNode,AnimalShelter
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

# def test_dequeue_one_element():
#     queue = PseudoQueue()
#     queue.enqueue(1)
#     queue.enqueue(2)
#     queue.dequeue()
#     assert queue.__str__() == '2 -> NULL'


## code challenge 12
def test_enqueue_onto_animal():
    queue=AnimalShelter()
    queue.enqueue('dog',1)
    assert queue.__str__() == '1,dog -> NULL'

def test_enqueue_multiple_onto_animal():
    queue=AnimalShelter()
    queue.enqueue('dog',1)
    queue.enqueue('cat',2)
    queue.enqueue('cat',3)
    queue.enqueue('dog',4)
    queue.enqueue('cat',5)
    assert queue.__str__() == '1,dog -> 2,cat -> 3,cat -> 4,dog -> 5,cat -> NULL'

def test_dequeue_cat():
    queue=AnimalShelter()
    queue.enqueue('dog',1)
    queue.enqueue('cat',2)
    queue.enqueue('cat',3)
    queue.enqueue('dog',4)
    queue.enqueue('cat',5)
    queue.dequeue('cat')
    assert queue.__str__() == '1,dog -> 3,cat -> 4,dog -> 5,cat -> NULL'

def test_dequeue_dog():
    queue=AnimalShelter()
    queue.enqueue('dog',1)
    queue.enqueue('cat',2)
    queue.enqueue('cat',3)
    queue.enqueue('dog',4)
    queue.enqueue('cat',5)
    queue.dequeue('dog')
    assert queue.__str__() == '2,cat -> 3,cat -> 4,dog -> 5,cat -> NULL'

def test_enqueue_dog():
    queue=AnimalShelter()
    queue.enqueue('dog',1)
    with pytest.raises(Exception):
        assert queue.enqueue('crocodile',2)

