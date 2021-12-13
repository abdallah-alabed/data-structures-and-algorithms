from hashtables import __version__
from hashtables.hash import Hashtable
from hashtables.hash_repeted import repeatedWord
from hashtables.tree_intersection import tree_intersection , Node , BinaryTree


def test_version():
    assert __version__ == '0.1.0'

# Code Challenge 30

# Adding a key/value to your hashtable results in the value being in the data structure


def test_1():
    h = Hashtable()
    h.add('Abdallah', 100)
    assert h.contain('Abdallah') == True

# Retrieving based on a key returns the value stored


def test_2():
    h = Hashtable()
    h.add('Abdallah', 100)
    assert h.get('Abdallah') == 100

# Successfully returns null for a key that does not exist in the hashtable


def test_3():
    h = Hashtable()
    h.add('Abdallah', 100)
    assert h.get('Issa') == 'NULL'

# Successfully handle a collision within the hashtable


def test_4():
    h = Hashtable()
    h.add('ABD', 100)
    h.add('BAD', 50)
    assert h.contain('BAD') == True
    assert h.contain('ABD') == True

# Successfully retrieve a value from a bucket within the hashtable that has a collision


def test_5():
    h = Hashtable()
    h.add('ABD', 100)
    h.add('BAD', 50)
    assert h.get('BAD') == 50
    assert h.get('ABD') == 100

# Successfully hash a key to an in-range value


def test_6():
    h = Hashtable()
    assert h.hash('Abd') == 901

    # A = 65 , b=98 , d=100
    # 263*19=4997
    # 4997 % 1024= 901


# Code Challenge 31

def test_repeat_1():

    assert repeatedWord('It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...') == 'summer'


def test_repeat_2():

    assert repeatedWord('It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...') == 'it'


def test_repeat_3():
    
    assert repeatedWord(
        'Once upon a time, there was a brave princess who') == 'a'




def test_tree_intersection():
    node1 = Node(150)
    node2 = Node(100)
    node3 = Node(250)
    node4 = Node(75)
    node5 = Node(160)
    node6 = Node(200)
    node7 = Node(350)
    node8 = Node(125)
    node9 = Node(175)
    node10 = Node(300)
    node11 = Node(500)
    binary_tree1=BinaryTree()
    binary_tree1.root=node1
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node5.left = node8
    node5.right = node9
    node7.left = node10
    node7.right = node11

    node_one = Node(42)
    node_two = Node(100)
    node_three = Node(600)
    node_four = Node(15)
    node_five = Node(160)
    node_six = Node(200)
    node_seven = Node(350)
    node_eight = Node(125)
    node_nine = Node(175)
    node_ten = Node(4)
    node_eleven = Node(500)
    binary_tree2=BinaryTree()
    binary_tree2.root=node_one
    node_one.left = node_two
    node_one.right = node_three
    node_two.left = node_four
    node_two.right = node_five
    node_three.left = node_six
    node_three.right = node_seven
    node_five.left = node_eight
    node_five.right = node_nine
    node_seven.left = node_ten
    node_seven.right = node_eleven

    assert tree_intersection(binary_tree1,binary_tree2) == [100, 160, 125, 175, 200, 350, 500]