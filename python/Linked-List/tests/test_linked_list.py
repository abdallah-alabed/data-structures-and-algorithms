import pytest
from linked_list import __version__
from linked_list.linked_list import LinkedList, Node


## For code challenge 5
def test_version():
    assert __version__ == '0.1.0'


def test_empty_linked_list():
    ll = LinkedList()
    expected = None
    actual = ll.head
    assert expected == actual

def test_insert_hello():
    ll = LinkedList()
    ll.insert('hello')
    expected = 'hello -> NULL'
    actual = ll.__str__()
    assert expected == actual

def test_head():
    node1=Node(5)
    ll = LinkedList()
    ll.head=node1
    assert ll.head == node1


def test_insert_multiple():
    ll = LinkedList()
    ll.insert('hello')
    ll.insert(False)
    ll.insert(123)
    expected = 'hello -> False -> 123 -> NULL'
    actual = ll.__str__()
    assert expected == actual

def test_Exists_True():
    ll = LinkedList()
    ll.insert('hello')
    ll.insert(False)
    ll.insert(123)
    expected = True
    actual = ll.includes(123)
    assert expected == actual

def test_Exists_False():
    ll = LinkedList()
    ll.insert('hello')
    ll.insert(False)
    ll.insert(123)
    expected = False
    actual = ll.includes('lol')
    assert expected == actual

def test__str__():
    ll = LinkedList()
    ll.insert('hello')
    ll.insert(False)
    ll.insert(123)
    expected = 'hello -> False -> 123 -> NULL'
    actual = ll.__str__()
    assert expected == actual


## for code challenge 6

def test_add__node_to_the_end_of_the_linked_list():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.append(5)
    actual=ll.__str__()
    excpected = '1 -> 2 -> 3 -> 4 -> 5 -> NULL'
    assert excpected == actual 

def test_add_multiple_nodes_to_the_end_of_linked_list():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    assert ll.__str__() == "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> NULL"

def test_insert_node_before_node_located_in_the_middle_of_linked_list():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert_before(3,5)
    assert ll.__str__() == "1 -> 2 -> 5 -> 3 -> 4 -> NULL"

def test_insert_node_before_the_first_node():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert_before(1,5)
    assert ll.__str__() == "5 -> 1 -> 2 -> 3 -> 4 -> NULL"

def test_insert_after_node_located_in_the_middle_of_linked_list():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert_after(3,5)
    assert ll.__str__() == "1 -> 2 -> 3 -> 5 -> 4 -> NULL"

def test_insert_node_after_the_last_node():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert_after(4,5)
    assert ll.__str__() == "1 -> 2 -> 3 -> 4 -> 5 -> NULL"