# Array binary search

## Problem Domain:
we need to create a function that takes in an array and a value from the array values,the function should return the index of the 
value in the array.

## Inputs/Outputs
Inputs: array with n elements , x is a value from the array itself 
Outputs: index of the vaue in the array

## Visual
ex: [1,2,3,4] , 3 -->  2

## BigO
Time complexity: O(n)

## Algorithm
- create a function that recieves array and number as arguments (arr,x)
- create a variable i to work as a counter
- Loop through the array if i< length of the array
  on loop we need to:
  - create variable called result
  - subtract the value (x) from the from array value of index 0 
  - if the subtraction results to 0 then we return the index
  - if not we move to the next index and repeat
- stop the search if the subtraction = 0
- return the index

## Pseudo Code
- Define function with argument arr,x
- define a counter i
- while i< len(arr):
- result=x-arr[i]
- if result=0 --> break 
- else:
            increment i
        return i

## Code in Python
def BinarySearch(arr,x):
    i=0
    while i < len(arr):
      result=x-arr[i]
      if result == 0:
        break
      else:
        i+=1

    return i

## Verification
input: [1,2,3,4] ,3

expected output: 2

i=0

if 3-1==0   #false

i+=1

i=1

if 3-2==0   #false

i=2

if 3-3==0   #true

break

return i
