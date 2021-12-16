# from collections import deque

# class Queue:
#     def __init__(self):
#         self.dq = deque()

#     def enqueue(self, value):
#         self.dq.appendLeft(value)

#     def dequeue(self):
#         self.dq.pop()

#     def __len__(self):
#         return len(self.dq)


# class Stack:
#     def __init__(self):
#         self.dq = deque()

#     def push(self, value):
#         self.dq.append(value)

#     def pop(self):
#         self.dq.pop()

class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.__adj_list = {}

    def add_node(self, value):
        v = Vertex(value)
        self.__adj_list[v] = []
        return v

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.__adj_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self.__adj_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex, weight)
        self.__adj_list[start_vertex].append(edge)

    def get_nodes(self):
        return self.__adj_list.keys()

    def get_neighbors(self, vertex):
        return self.__adj_list.get(vertex, [])

    def size(self):
        return len(self.__adj_list)