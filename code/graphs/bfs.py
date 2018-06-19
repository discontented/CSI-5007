from collections import deque
import networkx as nx

def bfs(G, s):
    # Initializes state and predecessor arrays.
    for u in G:
        state[u] = "undiscovered"
        p[u] = None
    # Sets source node to discovered
    state[s] = "discovered"
    # No predecessor to source node in BFS tree
    p[s] = None
    
    Q = deque(i)
    while Q.maxlen != 0:
        u = Q.pop
        for v in G.adj(u):
            if state[v] == "undiscovered":
                state[v] = "discovered"
                p[v] = u
                Q.appendleft(v)
        state[u] = "processed"


g = nx.Graph()
g.add_nodes_from([1,2,3])
g.add_edges_from([(1,2),(1,3)])

bfs(g,2)
