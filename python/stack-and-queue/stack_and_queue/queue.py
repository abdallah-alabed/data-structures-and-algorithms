from stack_and_queue.stack import Stack


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

class PseudoQueue():
    def __init__(self):
        self.stack1 = Stack() 
        self.stack2 = Stack()

    def enqueue(self, value):
        c_top=self.stack2.top
        self.stack1.push(value)
        b_top = self.stack1.top
        self.stack1.pop()   
        self.stack2.push(b_top)
        if c_top != None:
            self.stack2.top.next=c_top

    def dequeue(self):
        while self.stack2.top != None:
            print(self.stack2.top)
            c_top=self.stack2.top
            self.stack2.pop()
            self.stack1.push(c_top)
            self.stack2.top=c_top.next
        print(self.stack1.top)
        c_top=self.stack1.top
        self.stack1.pop()
        print(self.stack1.top)
        while self.stack1.top != None:
            if c_top.next != None:
                self.stack1.top=c_top.next
            self.stack1.pop()
            self.stack2.push(c_top)
            self.stack1.top=self.stack1.top.next
        print(self.stack2.top)


    def __str__(self):
        check=self.stack2.top
        outputStr=""
        while check:
            outputStr +=f"{vars(check.value)['value']} -> "
            check = check.next
        outputStr += 'NULL'
        return outputStr


class AnimalNode:
    def __init__(self,type,value="",next=None):
        self.value= value
        self.next = next
        self.type = type

class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,animal,value):
        node = AnimalNode(animal,value) 
        if animal == 'cat' or animal == 'dog':
            self.type = AnimalNode(animal,value)
        else:
            raise Exception('only Cats and Dogs')

        if self.front is None:
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node

    def dequeue(self,pref):
        if pref == 'cat':
            current=self.front
            if current.type == pref:
                self.front=current.next
                current.next = None
            else:
                prev=current
                current=current.next
                while current.type != pref:
                    prev=current
                    current=current.next
                prev.next=current.next
                current.next=None
        elif pref == 'dog':
            current=self.front
            if current.type == pref:
                self.front=current.next
                current.next = None
            else:
                prev=current
                current=current.next
                while current.type != pref:
                    prev=current
                    current=current.next
                prev.next=current.next
                current.next=None
        else:
            raise Exception('only Cats and Dogs')
    def __str__(self):
        check=self.front
        outputStr=""
        while check:
            outputStr +=f"{check.value},{check.type} -> "
            check = check.next
        outputStr += 'NULL'
        return outputStr

    # def enqueue(self,animal,value):
    #     if animal=='dog':
    #         self.q1.enqueue(value)
    #     elif animal=='cat':
    #         self.q2.enqueue(value)
    #     else:
    #         raise Exception('only Cats and Dogs')

    # def dequeue(self,pref):
    #     if pref=='dog':
    #         self.q1.dequeue()
    #     elif pref=='cat':
    #         self.q2.dequeue()
    #     else:
    #         raise Exception('NULL')

