from graphs import __version__
from graphs.graph import Vertex , Edge , Graph

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







