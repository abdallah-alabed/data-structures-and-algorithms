class Node():
    def __init__(self, value="",next=None):
        self.value = value
        self.next = next

class EmptyException(Exception):
	pass

class Stack():
    def __init__(self):
        self.top = None

    def push(self,value):
        node = Node(value)
        if self.top != None:
            node.next=self.top
        self.top=node

    def pop(self):
        if self.top != None:        
            temp = self.top
            self.top = self.top.next
            temp.next=None
        else:
            raise Exception('Stack is Empty')

    def peek(self):
        if self.top != None: 
            return self.top.value
        else:
            raise Exception('Stack is Empty')

    def is_empty(self):
        if self.top != None: 
            return False
        else:
            return True

    
    