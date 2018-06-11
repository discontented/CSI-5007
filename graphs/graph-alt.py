import networkx as nx

nodes = [1,2,3,4,5]

G = nx.Graph()
G.add_node(nodes)
for u in G:
    state[u] = "undiscovered"
    p[u] = None
