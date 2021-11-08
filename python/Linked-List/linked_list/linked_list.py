class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    This class creates data structure for Linked List
    """

    def __init__(self):
        self.head=None

    def insert(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
        else:
            current=self.head
            while current.next != None:
                current=current.next
            current.next=node

    def includes(self,value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
        

    def __str__(self):
 
        output = ""
        if self.head is None:
            output+="NULL HEAD"
        else:
            current = self.head
            while current:
                output += f"{current.value} -> "
                current = current.next
            output += "NULL"
        return output             

    def append(self,newValue):
        node=Node(newValue)
        if self.head is None:
            self.head=node
        else:
            current=self.head
            while current.next != None:
                current=current.next
            current.next=node

    def insert_before(self,value,newValue):
        node = Node(newValue)
        current = self.head
        prev =self.head

        while current:
            if current.value == value:
                if current==prev:
                    self.head = node
                    node.next = current
                    break
                else:
                    prev.next = node
                    node.next = current
            prev = current
            current = current.next

    def insert_after(self,value,newValue):
        node=Node(newValue)
        current=self.head
        while current:
            if current.value == value:
                node.next = current.next
                current.next = node
                break
            current=current.next

    def kthFromEnd(self,value):
        current = self.head
        NodesCounter=1
        while current.next != None:
            NodesCounter +=1
            current=current.next
        current=self.head
        if value > NodesCounter:
            return("Exception")
        elif value < 0:
            return("Exception")
        NodeValue = NodesCounter - value - 1
        for i in range(NodesCounter):
            if i == NodeValue:
                return current.value
            else:
                current=current.next
        
             
    