# Graphs
is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

## Challenge
1. add node: add a node (vertix) to the graph
2. add edge: create an edge to connect two vertices together
3. get nodes: return all the nodes in the graph
4. get neighbors: return all the neighbor vertices to the requested vertix
5. size: return the size of the graph

## Approach & Efficiency
1. had to create 3 classes:
    - graph
    - vertix
    - edge
2. add node: create a vertix and add it to the adjacency list
3. add edge: takes the first and last vertices and create an edge between them
4. get nodes: return all the nodes in the adjacency list
5. get neighbors: takes the target vertix and return all the neighbor vertices to the requested vertix
6. size: return the size of the graph

## API
Vertex - A vertex, also called a “node”, is a data object that can have zero or more adjacent vertices.
Edge - An edge is a connection between two nodes.
Neighbor - The neighbors of a node are its adjacent nodes, i.e., are connected via an edge.
Degree - The degree of a vertex is the number of edges connected to that vertex.