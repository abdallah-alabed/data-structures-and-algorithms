import pytest
from linked_list import __version__
from linked_list.linked_list import LinkedList, Node



def test_version():
    assert __version__ == '0.1.0'


def test_empty_linked_list():
    ll = LinkedList()
    expected = None
    actual = ll.head
    assert expected == actual


def test_append_hello():
    ll = LinkedList()
    ll.insert('hello')
    expected = 'hello -> NULL'
    actual = ll.to_string()
    assert expected == actual

def test_append_multiple():
    ll = LinkedList()
    ll.insert('hello')
    ll.insert(False)
    ll.insert(123)
    expected = 'hello -> False -> 123 -> NULL'
    actual = ll.to_string()
    assert expected == actual


def test_Exists_False():
    ll = LinkedList()
    ll.insert('hello')
    ll.insert(False)
    ll.insert(123)
    expected = False
    actual = ll.includes('lol')
    assert expected == actual


def test_Exists_True():
    ll = LinkedList()
    ll.insert('hello')
    ll.insert(False)
    ll.insert(123)
    expected = True
    actual = ll.includes(123)
    assert expected == actual

