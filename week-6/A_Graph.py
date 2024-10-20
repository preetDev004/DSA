
'''
In this file, I'll be showing you how to implement
a basic graph with an adjacency list (Bidirection with different weights),
and dijkstra's algorithm. 
Homework: can you convert my implementation of dijkstra to A*?
'''
class Vertex:
    def __init__(self, data):
        # Actual vertex data
        self.data = data
        # List of adjacencies to the vertex with the weight stored as a tuple : (other, weight)
        self.adjacencies = []

    def add_adjacency(self, other, weight):
        # Add an adjacent vertex and its weight if its not already in the list
        for adj, _ in self.adjacencies:
            if adj == other:
                return
        self.adjacencies.append((other, weight))

    def __str__(self):
        # String representation of the vertex data
        data = [other.data for other, _ in self.adjacencies]
        weight = [weight for _, weight in self.adjacencies]
        return f"Node: {str(self.data)} Adjacencies: {data} With Weight: {weight}"
    
class Graph:
    def __init__(self):
        self.verticies = set()

    def add_edge(self, u, v, weight):
        # Check if thoes vertices exisits otherwise add them first
        if u not in self.verticies:
            self.verticies.add(u)
        if v not in self.verticies:
            self.verticies.add(v)
        
        # Add them as each others adjacencies.
        u.add_adjacency(v, weight)
        v.add_adjacency(u, weight)
    
    # for bidirection with different wights
    def add_edge_bidirectional(self, u, v, w1, w2):
        # Check if thoes vertices exisits otherwise add them first
        if u not in self.verticies:
            self.verticies.add(u)
        if v not in self.verticies:
            self.verticies.add(v)
        
        # Add them as each others adjacencies.
        u.add_adjacency(v, w1)
        v.add_adjacency(u, w2)
        
    def dijkstra(self, source):
        pass

    def AStar(self, source):
        pass

if __name__ == "__main__":
    v1 = Vertex(4)    
    v2 = Vertex(35)    
    v3 = Vertex(12)    
    v4 = Vertex(41)    
    v5 = Vertex(23)    

    g1 = Graph()
    g1.add_edge(v1, v2, 6)
    g1.add_edge(v1, v4, 7)
    g1.add_edge(v2, v3, 12)
    g1.add_edge(v3, v5, 14)
    g1.add_edge(v5, v4, 18)

    print(v1)
    print(v2)
    print(v3)
    print(v4)
    print(v5)