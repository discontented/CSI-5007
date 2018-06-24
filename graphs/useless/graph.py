"""
size - number of vertices in graph
g.vertices[i] - List of all vertices conntected to node i in graph g
"""
class Graph:
    """Adjacency matrix implementation of a graph
    
    Returns:
        [type] -- [description]
    """

    def __init__(self, size):
        self.size = size
        # Initialize unconnected vertices
        self.vertices = [[0 for i in range(size) for j in range(size)]
    
    def add_edge(self,i,j):
        if not (i in self.vertices[j]):
            # adds vertex i to the list of vertices connected to j in graph g
            self.vertices[j].append(i)
            # adds veretex j to the list of vertices connected to i in graph g
            self.vertices[i].append(j)

    def num_edges(g):
        count = 0
        for i in range(g.size):
            count += len(g.vertices[i])
        return int(count/2)
