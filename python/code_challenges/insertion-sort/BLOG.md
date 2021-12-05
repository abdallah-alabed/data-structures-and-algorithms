# Insertion Sort
Selection Sort is a sorting algorithm that traverses the array multiple times as it slowly builds out the sorting sequence. The traversal keeps track of the minimum value and places it in the front of the array which should be incrementally sorted.

## Pesudo Code
   
    InsertionSort(arr)
      FOR i = 1 to arr.length

        int j <-- i - 1
        int temp <-- arr[i]

        WHILE j >= 0 AND temp < arr[j]
          arr[j + 1] <-- arr[j]
          j <-- j - 1

        arr[j + 1] <-- temp
&nbsp;

## Tracing
![cc26](./cc26.png)

## Big0
1. Time Complexity:  O(n^2)
2. Space Complexity: O(1)