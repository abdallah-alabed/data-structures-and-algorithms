from graphs import __version__
from graphs.graph import Vertex , Edge , Graph 
from graphs.buisness_trip import business_trip

def test_version():
    assert __version__ == '0.1.0'


# Node can be successfully added to the graph
def test_add_node():
  g= Graph()
  actual = g.add_node('graph').value
  assert actual == 'graph'

# An edge can be successfully added to the graph
def test_graph_add_edge():
    g= Graph()
    one = g.add_node('one')
    two = g.add_node('two')
    g.add_edge(one, two, 1)
    neighbors = g.get_neighbors(one)
    assert len(neighbors) == 1

# A collection of all nodes can be properly retrieved from the graph
def test_graph_get_nodes():
    g= Graph()
    one = g.add_node('one')
    two = g.add_node('two')
    actual = len(g.get_nodes())
    assert actual == 2

# All appropriate neighbors can be retrieved from the graph
# Neighbors are returned with the weight between nodes included
def test_graph_get_neighbors():
    g= Graph()
    one = g.add_node('one')
    two = g.add_node('two')
    g.add_edge(one, two, 1)
    neighbors = g.get_neighbors(one)
    assert len(neighbors) == 1
    neighbor_edge = neighbors[0]

# second test part
    assert neighbor_edge.vertex.value == 'two'
    assert neighbor_edge.weight == 1

# The proper size is returned, representing the number of nodes in the graph
def test_graph_size():
    g= Graph()
    g.add_node('one')
    actual = g.size()
    assert actual == 1

# An empty gproperly returns null
def test_graph_size_empty():
    g= Graph()
    actual = g.size()
    assert actual == 0



## Code Challenge 36
# Write at least three test assertions for each method that you define.

def test_breadth_1():
    g= Graph()
    one=g.add_node('Pandora')
    two=g.add_node('Arendelle')
    g.add_edge(one, two)
    three=g.add_node('Metroville')
    four=g.add_node('Monstroplolis')
    g.add_edge(two, three, 1)
    g.add_edge(two, four, 1)
    g.add_edge(four, three, 1)
    five=g.add_node('Narnia')
    six=g.add_node('Naboo')
    g.add_edge(three,five,1)
    g.add_edge(three,six,1)
    g.add_edge(four,six,1)
    g.add_edge(five,six, 1)
    assert g.bfs(one) == ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']


def test_breadth_2():
    g= Graph()
    one  =g.add_node('one'  )
    two  =g.add_node('two'  )
    three=g.add_node('three')
    four =g.add_node('four' )
    g.add_edge(one, two, 1)
    g.add_edge(one, three, 1)
    g.add_edge(three, four, 1)
    g.add_edge(two, four, 1)
    assert g.bfs(one) == ['one', 'two', 'three', 'four']

def test_breadth_3():
    g= Graph()
    one  =g.add_node('one'  )
    assert g.bfs(one) == ['one']


def test_business_trip():

    graph = Graph()

    pandora = graph.add_node('Pandora')
    arendelle = graph.add_node('Arendelle')
    metroville = graph.add_node('Metroville')
    monstropolis = graph.add_node('Monstropolis')
    naboo = graph.add_node('Naboo')
    narnia = graph.add_node('Narnia')

    # Pandora Edges
    graph.add_edge(pandora,arendelle,150)
    graph.add_edge(pandora,metroville,82)

    # arendelle Edges
    graph.add_edge(arendelle,pandora,150)
    graph.add_edge(arendelle,metroville,99)
    graph.add_edge(arendelle,monstropolis,42)
    
    # metroville Edges
    graph.add_edge(metroville,pandora,82)
    graph.add_edge(metroville,arendelle,99)
    graph.add_edge(metroville,monstropolis,105)
    graph.add_edge(metroville,naboo,26)
    graph.add_edge(metroville,narnia,37)

    # monstropolis Edges
    graph.add_edge(monstropolis,arendelle,42)
    graph.add_edge(monstropolis,metroville,105)
    graph.add_edge(monstropolis,naboo,73)

    # naboo Edges
    graph.add_edge(naboo,monstropolis,73)
    graph.add_edge(naboo,metroville,26)
    graph.add_edge(naboo,narnia,250)
    
    # narnia Edges
    graph.add_edge(narnia,metroville,37)
    graph.add_edge(narnia,naboo,250)

    assert [True, "$82"] == business_trip(graph,[metroville, pandora])
    assert [True, '$115'] == business_trip(graph,[arendelle,monstropolis, naboo])
    assert [False, "$0"] == business_trip(graph,[naboo, pandora])
    assert [False, '$0'] == business_trip(graph,[narnia, arendelle,naboo])

def test_depth_first():
    graph = Graph()

    node_a =graph.add_node('a')
    node_b =graph.add_node('b')
    node_c =graph.add_node('c')
    node_d =graph.add_node('d')
    node_e =graph.add_node('e')
    node_f =graph.add_node('f')
    node_g =graph.add_node('g')
    node_h =graph.add_node('h')

    # a Edges
    graph.add_edge(node_a,node_b)
    graph.add_edge(node_a,node_d)
    
    # b Edges
    graph.add_edge(node_b,node_a)
    graph.add_edge(node_b,node_c)
    graph.add_edge(node_b,node_d)

    # c Edges
    graph.add_edge(node_c,node_b)
    graph.add_edge(node_c,node_g)

    # d Edges
    graph.add_edge(node_d,node_a)
    graph.add_edge(node_d,node_b)
    graph.add_edge(node_d,node_e)
    graph.add_edge(node_d,node_f)
    graph.add_edge(node_d,node_h)

    # e Edges
    graph.add_edge(node_e,node_d)

    # f Edges
    graph.add_edge(node_f,node_d)
    graph.add_edge(node_f,node_h)

    # g Edges
    graph.add_edge(node_g,node_c)

    # h Edges
    graph.add_edge(node_h,node_d)
    graph.add_edge(node_h,node_f)

    assert graph.dfs(node_a) == ['a', 'b', 'c', 'g', 'd', 'e', 'f', 'h']