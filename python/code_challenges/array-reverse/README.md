# Array Reverse:

## Problem Domain:
we need to create a function that takes in an array and give the array back with the items reversed inside it.

## Inputs/Outputs
Inputs: array with n elements  
Outputs: Input Array Reversed  

## Visual
ex: [1,2,3,4] -->  [4,3,2,1]

## BigO
Time complexity: O(n)

## Algorithm
- create a function that recieves the array as an argument
- Define variable and set its initial value to 1 (i)
- Define variable and set its initial value to array length -1 (f)
- Loop through the array
  on each loop we need to:
  - swap the elements with the two variables indexes
  - increment the variable (i) by 1
  - decrement the variable (f) by 1
- stop the loop when we reach the middle
- return the array

## Pseudo Code
- Define function with argument arr
- define i=0
- define f=  array length-1
- while i < f: swap arr[i] with arr[f] 
            i++
            f--
        return arr

## Code in Python
def reverseArray(arr):
i=0
f=len(arr)-1
while i < f:
    arr[i],arr[f]=arr[f],arr[i]
    i+=1
    f-=1
return arr

## Verification
input: [1,2,3,4] 
expected output: [4,3,2,1]

(i=0,f=3)
while i < f:   #true
    arr[i],arr[f]=arr[f],arr[i]
    <!--     1,4 = 4,1      -->
    i+=1 #1
    f-=1 #2
(i=1,f=2)
while i < f:   #true
    arr[i],arr[f]=arr[f],arr[i]
    <!--     2,3 = 3,2      -->
    i+=1 #2
    f-=1 #1
(i=2,f=1)
while i < f:   #false
return arr