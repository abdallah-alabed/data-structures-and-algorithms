from .hash import Hashtable , Node

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
