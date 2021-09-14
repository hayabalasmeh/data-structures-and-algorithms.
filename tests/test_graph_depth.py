from data_structures_algorth.challenge_graph.graph import Graph

def test_depth():
     #Arrange
    graph = Graph()
    vertex_zero =graph.add_vertex(0)
    vertex_1 =graph.add_vertex(1)
    vertex_2 = graph.add_vertex(2)
    graph.add_edges(vertex_zero,vertex_1)
    graph.add_edges(vertex_1,vertex_zero)
    graph.add_edges(vertex_1,vertex_2)
    graph.add_edges(vertex_2,vertex_1)
    graph.add_edges(vertex_2,vertex_zero)
    graph.add_edges(vertex_zero,vertex_2)
    #Act
    list = graph.graph_depth_first(vertex_zero)
    
    #Assert 
    assert list == [0,2,1]