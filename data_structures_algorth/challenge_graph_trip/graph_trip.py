from data_structures_algorth.challenge_graph.graph import Graph

def find_cost_trip(graph,cities):
    
        other_cities = graph.get_neighbors(cities[0])
        cost = 0
        for city in other_cities:
            if city.start_vertex.value in cities[1:len(cities)]:
                 cost = cost + city.weight
        if cost == 0:
            return [False,0]

        return [True,cost]

if __name__=="__main__":
    graph = Graph()
    vertex_paris =graph.add_vertex('paris')
    vertex_dubai =graph.add_vertex('dubai')
    vertex_qatar = graph.add_vertex('qatar')
    # vertex_2 = graph.add_vertex(2)
    graph.add_edges(vertex_paris,vertex_dubai,120)
    # graph.add_edges(vertex_dubai,vertex_paris,120)
    graph.add_edges(vertex_dubai,vertex_qatar,80)
    # graph.add_edges(vertex_qatar,vertex_dubai,80)
    print(find_cost_trip(graph,['paris','dubai']))