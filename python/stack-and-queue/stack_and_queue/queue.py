class Node():
    def __init__(self, value="",next=None):
        self.value = value
        self.next = next

class EmptyException(Exception):
	pass

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        node=Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        
    def dequeue(self):
        if self.front != None:        
            temp = self.front
            self.front = temp.next
            temp.next=None
        else:
            raise Exception('Queue is Empty')

    def peek(self):
        if self.front != None: 
            return self.front.value
        else:
            raise Exception('Queue is Empty')

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False