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
        node = Node(value)
        if self.head:
            node.next=self.head
        self.head = node

    def includes(self,value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
                    

    def append(self,newValue):
        node = Node(newValue)
        current=self.head
        if current:
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node

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
        
             
    def zip_lists(self,linked_list1,linked_list2):
        output_list=LinkedList()
        current1 = linked_list1.head
        current2 = linked_list2.head

        while current1 and current2  :
            output_list.append(current1)
            output_list.append(current2)
            current1 = current1.next
            current2 = current2.next
        while current1:
            output_list.append(current1)
            current1 = current1.next
        while current2:
            output_list.append(current2)
            current2 = current2.next
        return output_list

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

    def __repr__(self):
 
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