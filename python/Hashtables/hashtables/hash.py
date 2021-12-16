class Node():
    def __init__(self,key,value):
        self.key=key    
        self.value=value
        self.next=None

class Hashtable():
    def __init__(self):
        self.size=0
        self.capacity=1024
        self.buckets=[None]*self.capacity

    def hash(self,key):
        asscii_sum=0
        for i in key:
            asscii_ch= ord(i)
            asscii_sum+= asscii_ch
        temp_value=asscii_sum*19
        hashed=temp_value % self.capacity
        return hashed

    def add(self,key,value):
        self.size+=1
        index= self.hash(key)
        node=self.buckets[index]

        if node is None:
           self.buckets[index]= Node(key,value)
           return

        else:  # Collision
            prev=node
            while node is not None:
                prev=node
                node=node.next
            prev.next= Node(key,value)
    
    def get(self,key):
        index= self.hash(key)
        node=self.buckets[index]
        while node is not None and node.key != key:
            node=node.next
        if node is None:
            return "NULL"
        else:
            return node.value

    def contain(self,key):
        index= self.hash(key)
        node=self.buckets[index]
        while node is not None and node.key != key:
            node=node.next
        if node is None:
            return False
        else:
            return True

# def repeatedWord(string):
#     hash=Hashtable()
#     x=string.replace(',','')
#     x = x.lower()
#     x=x.split()
#     # print(x)
#     for i in x:
#         node=Node(i,0)
#         if hash.contain(i):
#             return i
#         hash.add(i,0)
        


# def most_common(string):
#     h=Hashtable()
#     text=string.replace(',' , '')
#     text=text.replace('.' , '')
#     text=text.lower()
#     text=text.split()
#     output=[]
#     for i in text:
#         if h.contain(i) :
#             output.append(i)
#         else:
#             h.add(i,0)
#     print(output)
#     if len(output) != 0:
#         answer=max(output,key=output.count)
#         return answer


# if __name__ == "__main__":
   
#     most_common('In a galaxy far far away')
#     most_common('Taco cat ate a taco')
#     most_common('No. Try not. Do or do not. There is no try.')
