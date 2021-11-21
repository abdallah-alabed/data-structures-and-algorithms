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


    def in_order(self):
        output = []
        def _traverse(_root):
            if _root is None:
                return  'Tree in Empty'
            if _root.left is not None:
                _traverse(_root.left)
            output.append(_root.value)
            if _root.right is not None:
                _traverse(_root.right)
            return output
        return _traverse

    def post_order(self):
        output = []
        def _traverse(_root):
            if _root is None:
                return 'Tree in Empty'
            if _root.left is not None:
                _traverse(_root.left)
            if _root.right is not None:
                _traverse(_root.right)
            output.append(_root.value)
            return output
        return _traverse

    def max_val(self):
        if self.root is None:
                return 'Tree in Empty'
        else:
            tree = self.pre_order()
            max = self.root.value
            for i in tree(self.root):
                if i > max: 
                    max = i
            return max

class BinarySearchTree(BinaryTree):

    def add(self,value):
        node = Node(value)
        def _traverse(root):
            if value <= root.value:
                if root.left:
                    _traverse(root.left)
                else: 
                    root.left = node
            elif value >= root.value:
                if root.right: 
                    _traverse(root.right)
                else: 
                    root.right = node
        _traverse(self.root)

    def contains(self,value):
        compare = value
        def _traverse(root):
            nonlocal compare
            compare = value
            if compare == root.value: 
                compare = True
            elif compare < root.value:
                if root.left: _traverse(root.left)
                else: 
                    return False
            elif value > root.value:
                if root.right:
                    _traverse(root.right)
                else:
                    return False

            if compare == True:
                return True
            else:
                return False
        return (_traverse(self.root))

