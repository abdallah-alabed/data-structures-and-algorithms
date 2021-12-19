# Graphs
is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

## Code Challenge 36 (Breadth-First Traversal of a Graph)
## Challenge 
1. Loop Through the graph and output the vertices in breadth first formation
2. Arguments (input) : Node 
3. Return (output) : A collection of nodes in the order they were visited. (Display the collection in array)


## Approach & Efficiency
1. Create a method called bfs (Breadth First Search) that takes in the starting vertix as an input
2. mark every vertex that enters the queue as visited so we remove any duplications in vising the vertecies !
3. we get the vertex neighbors and then we dequeue it
4. we keep repeating the process until we clear the queue and visit all the vertices

## BigO
1. Space Complexity: O(1)

2. Time Complexity: O(n^2)

## API
Breadth First Search: explores all vertecies at the present depth prior to moving on to the vertecies at the next depth level. Extra memory, usually a queue, is needed to keep track of the child nodes that were encountered but not yet explored.