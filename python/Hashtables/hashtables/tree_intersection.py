# from python.tree.tree.tree import Node , BinaryTree
from hashtables.hash import Hashtable

def tree_intersection(tree1,tree2):

    tree1_Output= tree1.pre_order()
    tree2_Output= tree2.pre_order()

    hash_table = Hashtable()

    result = []
    
    # print(tree1_Output)
    
    for i in tree1_Output:
        hash_table.add(i,i)
    for i in tree2_Output:
        if hash_table.contains(i):
            result.append(i)
    return result











class Node:
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree():
    def __init__(self):
        self.root=None

    def pre_order(self):
        output = []
        def _traverse(_root):
            if _root is None:
                return  'Tree in Empty'
            output.append(_root.value)
            if _root.left is not None:
                _traverse(_root.left)
            if _root.right is not None:
                _traverse(_root.right)
            return output
        return _traverse
