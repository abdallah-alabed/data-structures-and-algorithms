def sorted(array):
    for i in range(1, len(array)):
        step=i-1
        temp=array[i]

        while step >=0 and temp < array[step]:
            array[step+1]=array[step]
            step-=1

        array[step+1]=temp
    return array
