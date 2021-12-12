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

def repeatedWord(string):
    hash=Hashtable()
    x=string.replace(',','')
    x = x.lower()
    x=x.split()
    # print(x)
    for i in x:
        node=Node(i,0)
        if hash.contain(i):
            return i
        hash.add(i,0)
        



# if __name__ == "__main__":
   
#     print(repeatedWord('Once upon a time, there was a brave princess who'))

#     print(repeatedWord('It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."'))

#     print(repeatedWord('It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...'))


