# Array insert shift:

## Problem Domain:
we need to create a function that takes in an array and a value that we want to add in the array 
and give the array back with the value exactly in the middle of the array.

## Inputs/Outputs
Inputs: array with n elements , x value to be added  
Outputs: array with n+1 elements and x is the middle number 

## Visual
ex: [1,2,3,4] , 100 -->  [1,2,100,3,4]

## BigO
Time complexity: O(n)

## Algorithm
- create a function that recieves array and number as arguments (arr,x)
- define variable (counter) and equals to 0
- define variable (swaps) and equals the half of the array length
- Define array (xArr)and set its initial value to [x] 
- set array(arr) to array plus xArr
- Loop through the array
  on each loop we need to:
  - swap the values of our x until it reaches the middle
  - increment the variable (i) by 1
  - decrement the variable (f) by 1
- stop the index of x equal swaps
- return the array

## Pseudo Code
- Define function with argument arr,x
- define counter=0
- if len(arr)%2==0:
- define swaps=len(arr)/2
- else: swaps=len(arr)/2 + 0.5
- define xArr= [x]
- arr=arr + xArr
- while counter < swaps: swap arr[len(arr)-1-counter] with arr[len(arr)-2-counter]
            increment counter
        return arr

## Code in Python
def insertShiftArray(arr,x):

    counter =0

    if len(arr)%2==0:

      swaps=len(arr)/2

    else:

      swaps=len(arr)/2 - 0.5
      
    xArr=[x]

    arr= arr + xArr

    while counter< swaps:

      arr[len(arr)-1-counter],arr[len(arr)-2-counter] = arr[len(arr)-2-counter], arr[len(arr)-1-counter]

      counter+=1

    return arr


## Verification
input: [1,2,3,4] ,5

expected output: [1,2,5,3,4]

counter=0

if 4%2==0:   #true

swaps=2  #len(arr)/2

xArr=[5]

arr=arr + xArr

while counter < swaps :   #true counter=0

    arr[len(arr)-1-counter],arr[len(arr)-2-counter] = arr[len(arr)-2-counter], arr[len(arr)-1-counter]



    counter+=1 #1


while counter < swaps :   #true counter=1

    arr[len(arr)-1-counter],arr[len(arr)-2-counter] = arr[len(arr)-2-counter], arr[len(arr)-1-counter]



    counter+=1 #1

while counter < swaps :   #false counter=2

    arr[len(arr)-1-counter],arr[len(arr)-2-counter] = arr[len(arr)-2-counter], arr[len(arr)-1-counter]


return arr