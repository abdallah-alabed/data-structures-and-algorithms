# Graphs
is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

## Code Challenge 38 (Business-trip)
## Challenge 
Create a function that calculates the route cost for the an input array of lists.


## Approach & Efficiency
1. Create a function called business_trip  that takes in a grapgh and a route array (cityNames)
2. for every city in the list we find its neighbors 
3. we check if the next city in the array is a neighbor to the first one and return [False , "$0"] if Not
4. we keep repeating the process and addind the edges weight to get the final cost !

## BigO
1. Space Complexity: O(1)

2. Time Complexity: O(n)

