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
        # current = self.head
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

        # Second Solution
        # bef = self.head
        # innn = bef.next
        # while value != innn.value:
        #     bef = innn
        #     innn = bef.next
        
        # bef.next=node
        # node.next=innn
    def insert_after(self,value,newValue):
        node=Node(newValue)
        current=self.head
        while current:
            if current.value == value:
                node.next = current.next
                current.next = node
                break
            current=current.next

        # Second Solution
        # innn = self.head
        # aft = innn.next
        # while value != innn.value:
        #     innn = aft
        #     aft = innn.next
        
        # innn.next=node
        # node.next=aft

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


        # Second Solution
        # counter =0 
        # current=self.head

        # while current.next:
        #     counter+=1
        #     current = current.next
        
        # current=self.head
        # if value < 0:
        #     return 'Exception'
        # elif value > counter:
        #     return 'Exception'
        # else:
        #     while counter - value !=0:
        #         current = current.next
        #         counter-=1
        #     return current.value
       

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


def zip_lists(linked_list1,linked_list2):
    output_list=LinkedList()
    current1 = linked_list1.head
    current2 = linked_list2.head

    while current1 and current2  :
        output_list.append(current1)
        current1 = current1.next
        output_list.append(current2)
        current2 = current2.next
    while current1:
        output_list.append(current1)
        current1 = current1.next
    while current2:
        output_list.append(current2)
        current2 = current2.next
    return output_list

def reverseMe(ll):
    previous = None         
    current = ll.head     
    following = current.next    
    while current:
        current.next = previous 
        previous = current      
        current = following         
        if following:               
            following = following.next    
    ll.head = previous



if __name__ == "__main__":
    ll=LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    print(ll.kthFromEnd(1))