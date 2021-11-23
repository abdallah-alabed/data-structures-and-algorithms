from tree import __version__
import tree
from tree.tree import Node , BinaryTree , BinarySearchTree, breadth_first 
def test_version():
    assert __version__ == '0.1.0'



# Testing pre-order
def test_empty_tree_pre():
    tree = BinaryTree()
    traverse=tree.pre_order()
    assert traverse(tree.root) == 'Tree in Empty'

def test_root_only_pre():
    tree = BinaryTree()
    traverse=tree.pre_order()
    tree.root=Node("A")
    assert traverse(tree.root) == ['A']

def test_pre_order():
    tree = BinaryTree()
    traverse=tree.pre_order()
    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    assert traverse(tree.root) == ['A','B','C']

# Testing in_order
def test_empty_tree_in():
    tree = BinaryTree()
    traverse=tree.in_order()
    assert traverse(tree.root) == 'Tree in Empty'

def test_root_only_in():
    tree = BinaryTree()
    traverse=tree.in_order()
    tree.root=Node("A")
    assert traverse(tree.root) == ['A']

def test_in_order():
    tree = BinaryTree()
    traverse=tree.in_order()
    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    assert traverse(tree.root) == ['B','A','C']

# Testing post_order
def test_empty_tree_post():
    tree = BinaryTree()
    traverse=tree.post_order()
    assert traverse(tree.root) == 'Tree in Empty'

def test_root_only_post():
    tree = BinaryTree()
    traverse=tree.post_order()
    tree.root=Node("A")
    assert traverse(tree.root) == ['A']

def test_post_order():
    tree = BinaryTree()
    traverse=tree.post_order()
    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    assert traverse(tree.root) == ['B','C','A']

## Testing BST 
def test_add_contain_bst():
    search= BinarySearchTree()
    search.root=Node(20)
    search.root.left=Node(11)
    search.root.right=Node(35)
    search.add(22)
    search.add(2)
    assert search.contains(11) == True

def test_add_contain_bst2():
    search= BinarySearchTree()
    search.root=Node(20)
    search.add(22)
    search.add(2)
    search.add(11)
    search.add(33)
    search.add(201)
    search.add(-5)
    assert search.contains(101) == False

## Testing max value , code challenge 16
def test_max_1():
    tree = BinaryTree()
    tree.root=Node(9)
    tree.root.left=Node(4)
    tree.root.right=Node(3)
    assert tree.max_val() == 9

def test_max_2():
    tree = BinaryTree()
    tree.root=Node(9)
    tree.root.left=Node(5)
    tree.root.left.left=Node(1)
    tree.root.left.left.left=Node(10)
    tree.root.left.left.right=Node(18)
    tree.root.left.right=Node(6)
    tree.root.right=Node(3)
    tree.root.right.left=Node(12)
    tree.root.right.left.left=Node(15)
    tree.root.right.left.right=Node(17)
    tree.root.right.right=Node(55)
    tree.root.right.right.right=Node(8)
    assert tree.max_val() == 55

def test_max_3():
    tree = BinaryTree()
    assert tree.max_val() == 'Tree in Empty'

## Testing breadth , code challenge 17
def test_breadth_1():
    tree = BinaryTree()
    tree.root=Node(9)

    tree.root.left=Node(4)
    tree.root.right=Node(3)

    print(breadth_first(tree.root))
    assert breadth_first(tree.root) == [9,4,3]

def test_breadth_2():
    tree = BinaryTree()
    tree.root=Node(9)

    tree.root.left=Node(4)
    tree.root.right=Node(3)

    tree.root.left.left=Node(1)
    tree.root.left.right=Node(5)
    tree.root.right.left=Node(12)
    tree.root.right.right=Node(22)

    print(breadth_first(tree.root))
    assert breadth_first(tree.root) == [9,4,3,1,5,12,22]

def test_breadth_3():
    tree = BinaryTree()
    tree.root=Node(9)

    tree.root.left=Node(4)
    tree.root.right=Node(3)

    tree.root.left.left=Node(1)
    tree.root.left.right=Node(5)
    tree.root.right.left=Node(12)
    tree.root.right.right=Node(22)

    tree.root.left.left.left=Node(10)
    tree.root.left.left.right=Node(18)
    print(breadth_first(tree.root))
    assert breadth_first(tree.root) == [9,4,3,1,5,12,22,10,18]


def test_fizz_buzz1():
    tree = BinaryTree()
    tree.root=Node(9)
    tree.root.left=Node(4)
    tree.root.right=Node(3)
    assert tree.fizz_buzz_tree() == ['Fizz',4,'Fizz']

def test_fizz_buzz2():
    tree = BinaryTree()
    tree.root=Node(3)
    tree.root.left=Node(5)
    tree.root.right=Node(6)
    tree.root.left.left=Node(10)
    tree.root.left.right=Node(22)
    tree.root.right.left=Node(21)
    tree.root.right.right=Node(20)
    assert tree.fizz_buzz_tree() == ['Fizz','Buzz','Buzz',22,'Fizz','Fizz','Buzz']

def test_fizz_buzz3():
    tree = BinaryTree()
    tree.root=Node(9)
    tree.root.left=Node(15)
    tree.root.right=Node(30)
    assert tree.fizz_buzz_tree() == ['Fizz','FizzBuzz','FizzBuzz']
