import networkx as nx
import matplotlib.pyplot as plt
import random

def prim(G, s):
    # Initialize tree
    T = nx.Graph()

def generateDiGraph(num_v = None):
    G = nx.DiGraph()
    if num_v is not None:
        G.add_nodes_from(range(1,num_v + 1))
    return G

def randEdges(G):
    for v in G.nodes:
        eligible = [i for i in G.nodes if i != v]
        u = random.choice(eligible)
        G.add_edge(v,u)

    # ensures connection
    connectDC(G)
    
def connectDC(G):
    # Connect disconnected components in a graph
    """Connects any disconnection in graph.
    """
    UG = G.to_undirected()

    subgraphs = []
    for c in nx.connected_components(UG):
        subgraphs.append(G.subgraph(c))
    
    # if there's a disconnect
    if(len(subgraphs) > 1):
        sg_heads = [] # stores heads to all disconnected subgraphs
        for sg in subgraphs:
            sg_head = list(sg.nodes)[0]
            # print(sg_head)
            sg_heads.append(sg_head)

        for i in range(1, len(sg_heads)):
            # joins all disconnected subgraph heads to the first subgraph head
            G.add_edge(sg_heads[0], sg_heads[i])
            
def addWeight(G, low, high):
    for (u,v,w) in G.edges(data=True):
        w['weight'] = random.randint(low,high)

def shortestPath(G, s, t):
    return (nx.shortest_path_length(G, s, t))

def drawGraph(G):
    pos = nx.shell_layout(G)
    nx.draw_networkx_nodes(G, pos, nodeList = G.nodes())
    nx.draw_networkx_edges(G, pos, nodeList = G.edges())
    # nx.draw_networkx_labels(G, pos)
    weights = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels = weights)
    plt.show()

G = generateDiGraph(8)
randEdges(G)
addWeight(G, 0, 4)
# print(G.edges())
drawGraph(G)