# Graphs
is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

## Code Challenge 38 (Depth First Graph)
## Challenge 
Create a function that returns the graph in depth first order


## Approach & Efficiency
1. Create a method called dfs that takes in the starting vertex
2. add the vertex to the output array and mark it as visited
3. check if the vertex have neighbors and traverse to them too 
4. if the node have multiple neighbors we do the same for each neighbor in order 
5. return the results array after we visit all the vertices

## BigO
1. Space Complexity: O(1)

2. Time Complexity: O(n)

