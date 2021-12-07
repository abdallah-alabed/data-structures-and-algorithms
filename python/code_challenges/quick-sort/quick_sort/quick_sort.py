def QuickSort(arr,left,right):
    # left is the first index
    # right is the last index 
    if left<right:
        position=paritition(arr,left,right)
        QuickSort(arr, left, position - 1)
        QuickSort(arr, position + 1 , right)
    return arr
def paritition(arr, left, right):
    pivot=arr[right]
    low=left-1
    for i in range(left , right):
        if arr[i] <= pivot:
            low += 1
            swap(arr, i, low)

    swap(arr, right, low + 1)
    return low+1

def swap(arr, i, low):
    temp = arr[i]
    arr[i]=arr[low]
    arr[low]=temp


if __name__=="__main__":
    print(QuickSort([8,4,42,32,15,16],0,5))