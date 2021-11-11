import pytest
from linked_list import __version__
from linked_list.linked_list import LinkedList, Node
from linked_list.linked_list import zip_lists
from linked_list.linked_list import reverseMe



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
    expected = '123 -> False -> hello -> NULL'
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
    expected = '123 -> False -> hello -> NULL'
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
    excpected = '4 -> 3 -> 2 -> 1 -> 5 -> NULL'
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
    assert ll.__str__() == "4 -> 3 -> 2 -> 1 -> 5 -> 6 -> 7 -> NULL"

def test_insert_node_before_node_located_in_the_middle_of_linked_list():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert_before(3,5)
    assert ll.__str__() == "4 -> 5 -> 3 -> 2 -> 1 -> NULL"

def test_insert_node_before_the_first_node():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert_before(4,5)
    assert ll.__str__() == "5 -> 4 -> 3 -> 2 -> 1 -> NULL"

def test_insert_after_node_located_in_the_middle_of_linked_list():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert_after(3,5)
    assert ll.__str__() == "4 -> 3 -> 5 -> 2 -> 1 -> NULL"

def test_insert_node_after_the_last_node():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert_after(1,5)
    assert ll.__str__() == "4 -> 3 -> 2 -> 1 -> 5 -> NULL"

## for code challenge 7

def test_kthFromEnd_greater_than_the_length_of_the_linked_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    actual = ll.kthFromEnd(10)
    expected = "Exception"
    assert actual == expected

def test_k_same_length_as_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    actual = ll.kthFromEnd(4)
    expected = None
    assert actual == expected

def test_k_is_not_postive_integer():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    actual = ll.kthFromEnd(-3)
    expected = "Exception"
    assert actual == expected

def test_linked_list_size_1():
    ll = LinkedList()
    ll.insert(1)
    actual = ll.kthFromEnd(0)
    expected = 1
    assert actual == expected

def test_k_happy_path():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    actual = ll.kthFromEnd(2)
    expected = 2
    assert actual == expected

## for code challenge 8

# def test_zip_lists_same_length():
#     ll_1 = LinkedList()
#     ll_1.append(1)
#     ll_1.append(2)
#     ll_2 = LinkedList()
#     ll_2.append(3)
#     ll_2.append(4)
#     ll_3 = LinkedList()
#     ll_3 = ll_3.zip_lists(ll_1,ll_2)
#     assert ll_3.__str__() == "1 -> 3 -> 2 -> 4 -> NULL"

# def test_zip_lists_first_one_longer():
#     ll_1 = LinkedList()
#     ll_1.append(1)
#     ll_1.append(2)
#     ll_1.append(3)
#     ll_2 = LinkedList()
#     ll_2.append(4)
#     ll_2.append(5)
#     ll_3 = LinkedList()
#     ll_3 = ll_3.zip_lists(ll_1,ll_2)
#     assert ll_3.__str__() == "1 -> 4 -> 2 -> 5 -> 3 -> NULL"

# def test_zip_lists_second_one_longer():
#     ll_1 = LinkedList()
#     ll_1.append(1)
#     ll_1.append(2)
#     # ll_1.__str__()
#     ll_2 = LinkedList()
#     ll_1.append(3)
#     ll_2.append(4)
#     ll_2.append(5)
#     # ll_2.__str__()
#     actual = zip_lists(ll_1,ll_2)
#     assert actual.__str__() == "1 -> 3 -> 2 -> 4 -> 5 -> NULL"
   

# if __name__ == "__main__":
    # ll_1 = LinkedList()
    # ll_1.append(1)
    # ll_2 = LinkedList()
    # ll_2.append(3)
    # print(ll_1)
    # print(ll_2)
    # cry=ll_1
    # print(ll_2.zip_lists(cry,ll_2))
    # ll = LinkedList()
    # ll.insert('hello')
    # ll.insert(False)
    # ll.insert(123)
    # ll.reverseMe()
    # print(ll.__str__())

def test_reverse():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    expected = '3 -> 2 -> 1 -> NULL'
    reverseMe(ll)
    actual = ll.__str__()
    assert expected == actual