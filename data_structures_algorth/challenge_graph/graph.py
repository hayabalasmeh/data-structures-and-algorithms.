from data_structures_algorth.challenge_stack_and_queue.stack_queue import Queue

class Vertex:
  
    def __init__(self,value):
        """
            construct an object vertex with a value and a list of pointers to the children nodes

        """
        self.value = value
        self.neighbor = []
    def __str__(self) -> str:
        return self.value
  



class Edge:
  def __init__(self, vertex, weight=1):
    """
    Construct an object edge with a weight connected to vertex
    
    """
    self.start_vertex = vertex
   
    self.weight = weight

# edge1 = Edge(vertex)



class Graph:
  
    def __init__(self):
        """
            construct a Graph object with a pointer to the root node

        """
        self._adjacency_list = {

        }

    def _breadthfirst(self,root, action=lambda nodes: print(nodes)):
        """ 
        Performs a level order traversal of the graph and calls action at each node
        """
        nodes = []
        breadth = Queue()
        visited = []

        breadth.enqueue(root)
        visited.append(root.value)

        while breadth.front:
            front = breadth.dequeue()
            nodes.append(front.value)

            for child in front.neighbor:
                if not child.value in visited:
                    visited.append(child.value)
                    breadth.enqueue(child)   

        return nodes

    def add_vertex(self, value):
        """ 
            Adds a vertex to the graph

            arguments
            value


        """
        vertex = Vertex(value)
        self._adjacency_list[value]= []
        return vertex
        

    def add_edges(self, vertex1, vertex2, weight=1):
        """ 
        Adds an edge to our graph
        
        """  
        edge = Edge(vertex1, weight)
        edge.start_vertex.neighbor.append(vertex2)
        self._adjacency_list[vertex1.value] =  edge.start_vertex.neighbor
       

    
    def get_nodes(self):
        return list(self._adjacency_list.keys())
        

    def get_neighbors(self,vertex):
        neighbors = self._adjacency_list[vertex.value]
        
        
        return [neighbor.value for neighbor in neighbors]
        
       

    def size(self):
        """Returns the total number of nodes in the graph
        """
        return len(self._adjacency_list.keys())
    
    # def to_adj_list(self):
    #     return self._adjacency_list
    
if __name__== '__main__':
        dic = {}
        space = 5
        dic[space] = 0
        # print(len(dic.keys()))
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
        print(graph.size())
        print(graph.get_nodes())
        print(graph._breadthfirst(vertex_zero))
        print(graph.get_neighbors(vertex_zero))


   
