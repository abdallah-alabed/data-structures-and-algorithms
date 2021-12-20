from graphs.graph import Graph , Edge , Vertex, Queue

def business_trip(graph,cityNames):
    cost = 0
    def trav(cityNames):
        nonlocal cost
        one = cityNames.pop(0)
        neighbors = graph.get_neighbors(one)
        vertices = [i.vertex for i in neighbors]
        for i in neighbors:
            if cityNames[0] not in vertices:
                return [False , "$0"]
            if i.vertex in cityNames:
                print(i.weight)
                cost += i.weight
                if len(cityNames)>1:
                    trav(cityNames)
    trav(cityNames)
    if cost == 0:
        return [False , "$0"]
    else:
        return [True , f"${cost}"]
