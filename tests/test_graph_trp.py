

from data_structures_algorth.challenge_graph.graph import Graph
from data_structures_algorth.challenge_graph_trip.graph_trip import find_cost_trip
# Test if a direct trip is possibla nd return the cost 

def test_direct_trip():
    #Arrange
    graph = Graph()
    vertex_paris =graph.add_vertex('paris')
    vertex_dubai =graph.add_vertex('dubai')
    vertex_qatar = graph.add_vertex('qatar')
    graph.add_edges(vertex_paris,vertex_dubai,120)
    graph.add_edges(vertex_dubai,vertex_qatar,80)
    #Act
    direct_cost = find_cost_trip(graph,['qatar','dubai']) 
    #Assert
    assert direct_cost == [True,80]

def test_direct_cost_trip():
    #Arrange
    graph = Graph()
    vertex_paris =graph.add_vertex('paris')
    vertex_dubai =graph.add_vertex('dubai')
    vertex_qatar = graph.add_vertex('qatar')
    graph.add_edges(vertex_paris,vertex_dubai,120)
    graph.add_edges(vertex_dubai,vertex_qatar,80)
    #Act
    direct_cost = find_cost_trip(graph,['paris','dubai','qatar']) 
    #Assert
    assert direct_cost == [True,120]

def test_in_direct_trip():
    #Arrange
    graph = Graph()
    vertex_paris =graph.add_vertex('paris')
    vertex_dubai =graph.add_vertex('dubai')
    vertex_qatar = graph.add_vertex('qatar')
    graph.add_edges(vertex_paris,vertex_dubai,120)
    graph.add_edges(vertex_dubai,vertex_qatar,80)
    #Act
    direct_cost = find_cost_trip(graph,['paris','qatar']) 
    #Assert
    assert direct_cost == [False,0]