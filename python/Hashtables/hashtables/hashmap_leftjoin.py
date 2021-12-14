from hashtables.hash import Hashtable

syn=Hashtable()
syn.add('fond','enamored')
syn.add('wrath','anger')
syn.add('diligent','employed')
syn.add('outift','garb')
syn.add('guide','usher')

ant=Hashtable()
ant.add('fond','averse')
ant.add('wrath','delight')
ant.add('diligent','idle')
ant.add('flow','jam')
ant.add('guide','follow')


def left_join(syn,ant):

    output=[]
    arraySYN=[]
    arrayANT=[]
    flag=False

    for i in syn.buckets:
        if i != None:
            arraySYN.append(i)
    for j in ant.buckets:
        if j != None:
            arrayANT.append(j)

    for elem in arraySYN:
        flag=False
        for item in arrayANT:
            if item.key == elem.key:
                output.append([item.key , elem.value , item.value])
                flag=True
        if flag == False:
            output.append([elem.key , elem.value , 'NULL'])
    return output


    
if __name__ == "__main__":
    print(left_join(syn,ant))