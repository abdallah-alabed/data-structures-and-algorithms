from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        self.dq.pop()

    def __len__(self):
        return len(self.dq)

    def peek(self):
        if self.front != None: 
            return self.front.value
        else:
            raise Exception('Queue is Empty')

class Stack:
    def __init__(self):
        self.dq = deque()

    def push(self, value):
        self.dq.append(value)

    def pop(self):
        self.dq.pop()

class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight

    def __str__(self):
        return str(self.vertex)

class Graph:
    def __init__(self):
        self.__adj_list = {}

    def add_node(self, value):
        v = Vertex(value)
        self.__adj_list[v] = []
        return v

    def add_edge(self, start_vertex, end_vertex, weight=1):
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

    def dfs(self, start_vertex):
        result = []
        result.append(start_vertex.value)

        def trav(vertex):
            edge =self.__adj_list[vertex]
            for i in edge:
                my_vertex = i.vertex.value
                if my_vertex not in result:
                    result.append(my_vertex)
                    trav(i.vertex)
        trav(start_vertex)
        return result
            

    def bfs(self, start_vertex):
        queue = Queue()
        result = []
        visited = set()

        queue.enqueue(start_vertex)
        visited.add(start_vertex)
        result.append(start_vertex.value)
    
        while len(queue) != 0:
            # print(queue.dq)
            current_vertex = queue.dq[-1] #queue.dequeue()
            neighbors = self.get_neighbors(current_vertex)
            current_vertex=queue.dequeue()
            
            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor)
                    result.append(neighbor.value)
                    
        print(result)
        return result