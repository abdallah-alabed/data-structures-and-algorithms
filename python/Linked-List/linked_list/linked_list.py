class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    This class creates data algorithm for Linked List
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
        

    def to_string(self):
 
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



# if __name__=="__main__":
#     ll = LinkedList()
#     ll.insert(1)
#     ll.insert(2)
#     ll.insert(3)
#     ll.insert(4)
#     print(ll.to_string())
    