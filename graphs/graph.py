"""
size - nunmber of vertices in graph
g.vertices[i] - List of all vertices conntected to node i in graph g
"""
class Graph:
    def __init__(self, size):
        self.size = size
        self.vertices = [[] for i in range(size)]
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
