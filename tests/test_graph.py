
from data_structures_algorth.challenge_graph.graph import Graph

# Test if Node can be successfully added to the graph
def test_add_vertex():
    #Arrange
    graph = Graph()
    #Act
    vertex_zero =graph.add_vertex(0)
    #Assert 
    assert vertex_zero.value == 0
    

# An edge can be successfully added to the graph
def test_add_edge():
    #Arrange
    graph = Graph()
    vertex_zero =graph.add_vertex(0)
    vertex_1 =graph.add_vertex(1)
    #Act
    graph.add_edges(vertex_zero,vertex_1,9)
    graph.add_edges(vertex_1,vertex_zero,9)
    #Assert 
    assert graph._adjacency_list.get(vertex_zero.value)[0].weight== 9
   
# A collection of all nodes can be properly retrieved from the graph
def test_get_all_nodes():
    #Arrange
    graph = Graph()
    vertex_zero =graph.add_vertex(0)
    vertex_1 =graph.add_vertex(1)
    #Act
    all_nodes = graph.get_nodes()
    
    #Assert 
    assert all_nodes == [0,1]

# All appropriate neighbors can be retrieved from the graph
# def test_get_neighbors():
#      #Arrange
#     graph = Graph()
#     vertex_zero =graph.add_vertex(0,)
#     vertex_1 =graph.add_vertex(1)
#     vertex_2 = graph.add_vertex(2)
#     graph.add_edges(vertex_zero,vertex_1)
#     graph.add_edges(vertex_1,vertex_zero)
#     graph.add_edges(vertex_1,vertex_2)
#     graph.add_edges(vertex_2,vertex_1)
#     graph.add_edges(vertex_2,vertex_zero)
#     graph.add_edges(vertex_zero,vertex_2)
#     #Act
#     zero_neighbors = str(graph.get_neighbors(vertex_zero))
#     one_neighbors = str(graph.get_neighbors(vertex_1))
    
#     #Assert 
#     assert zero_neighbors == [1,2]
#     assert one_neighbors == [0,2]


        
 
# The proper size is returned, representing the number of nodes in the graph
def test_get_size():
    #Arrange
    
    graph = Graph()
    vertex_zero =graph.add_vertex(0)
    vertex_1 =graph.add_vertex(1)
    vertex_2 = graph.add_vertex(2)
    #Act
    size = graph.size()
    
    #Assert 
    assert size == 3
    
     
# Testiing Breadth traverse 
        
def test_breadth():
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
    list = graph._breadthfirst(vertex_zero)
    
    #Assert 
    assert list == [0,1,2]
