def mergeSort(arr):
    n=len(arr)
    if n>1:
        mid=round(n/2)
        left=arr[0:mid]
        right=arr[mid:n]
        mergeSort(left)
        mergeSort(right)
        merge(left,right,arr)
    return arr

def merge(left,right,arr=[]):
    i=0
    j=0
    k=0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1

    if i == len(left):
        while k != len(left)+len(right):
            arr[k]=right[j]
            k+=1
            j+=1
    else:
        while k != len(left)+len(right):
            arr[k]=left[i]
            k+=1
            i+=1


if __name__=="__main__":
    print(mergeSort([8,4,42,32,15,16]))