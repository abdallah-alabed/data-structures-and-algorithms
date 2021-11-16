from stack_and_queue.stack import Stack , validate_brackets
import pytest

def test_push_onto_stack():
    stack=Stack()
    stack.push(1)
    assert stack.top.value == 1

def test_push_multiple_values_onto_stack():
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    assert stack.top.value == 4

def test_pop_off_stack():
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.pop()
    assert stack.top.value == 3

def test_empty_stack():
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    assert stack.is_empty() == False
    stack.pop()
    assert stack.is_empty() == True


def test_peek_the_next_on_the_stack():
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3

def test_instantiate_an_empty_stack():
    stack=Stack()
    assert stack


def test_stack_empty_exception():
    stack = Stack()
    with pytest.raises(Exception):
        assert stack.peek()
    with pytest.raises(Exception):
        assert stack.pop()

## code challenge 13

def test_1_validation():
    assert validate_brackets('{}(){}') == True 

def test_2_validation():
    assert validate_brackets('()[[Extra Characters]]') == True 

def test_3_validation():
    assert validate_brackets('(){}[[]]') == True 

def test_4_validation():
    assert validate_brackets('{}{Code}[Fellows](())') == True 

def test_5_validation():
    assert validate_brackets('[({}]') == False 
    
def test_6_validation():
    assert validate_brackets('(](') == False 

def test_7_validation():
    assert validate_brackets('{(})') == False 

def test_8_validation():
    assert validate_brackets('{') == False 

def test_9_validation():
    assert validate_brackets(')') == False 

def test_10_validation():
    assert validate_brackets('[}') == False 

def test_11_validation():
    assert validate_brackets('{}') == True
