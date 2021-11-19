from tree import __version__
import tree
from tree.tree import Node , BinaryTree , BinarySearchTree

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


