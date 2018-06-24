# Python included libraries
import sys
import random

# Installed libraries
try:
    import networkx as nx
except ImportError:
    sys.exit("""You need networkx!
                run pip install networkx.""")

try:
    import matplotlib.pyplot as plt
except ImportError:
    sys.exit("""You need matplotlib!
                run pip install matplotlib""")

class DiGraph:
    """Creates a directed graph that could optionally be weighted.
    
    G.V - Set of vertices
    G.E - Set of edges

    Returns:
        DiGraph -- A directed, weighted graph.
    
    Example
    -------    
    G = DiGraph() - Initializes an empty directed graph.
    G = DiGraph(4, 1, 4) - Inializes a directed graph with 4 vertices, random edges, and weights from 0 to 4.
    G.drawGraph() - Draws current graph object.

    """

    
    def __init__(self, num_V = None, weightL = None, weightH = None):
        """Initializes a weighted, directed graph.  Vertices are labelled sequentially from 1 to num_V.
        
        Keyword Arguments:
            num_V {int} -- Number of vertices. (default: {None})
            weightL {int} -- Lowest weight.  Can be negative. (default: {None})
            weightH {int} -- Highest weight. (default: {None})
        """
        self.G = nx.DiGraph()

        if num_V is not None:
            self.G.add_nodes_from(range(1, num_V + 1))
        
        self.randEdges()
        self.V = self.G.nodes()
        self.E = self.G.edges()

        if (weightL and weightH) is not None:
            self.addWeight(weightL, weightH)

    def addWeight(self, low, high):
        """Adds random weight to edges between low and high
        
        Arguments:
            low {int} -- Lowest weight.  Can be negative
            high {int} -- Highest weight
        """

        for (u, v, w) in self.G.edges(data=True):
            w['weight'] = random.randint(low, high + 1)

    def randEdges(self):
        """Generates random edges of this DiGraph object.
        Post-Condition: All vertices are connected by at least one directed edge.
        """

        for v in self.G.nodes:
            eligible = [i for i in self.G.nodes if i != v]
            u = random.choice(eligible)
            self.G.add_edge(v,u)

        # ensures connection
        self.connectDC()

    def connectDC(self):
        """Connects two or more disconnected components within this DiGraph object.
        """
        UG = self.G.to_undirected()

        subgraphs = []
        for c in nx.connected_components(UG):
            subgraphs.append(self.G.subgraph(c))
        
        # if there's a disconnect
        if(len(subgraphs) > 1):
            sg_heads = [] # stores heads to all disconnected subgraphs
            for sg in subgraphs:
                sg_head = list(sg.nodes)[0]
                # print(sg_head)
                sg_heads.append(sg_head)

            for i in range(1, len(sg_heads)):
                # joins all disconnected subgraph heads to the first subgraph head
                self.G.add_edge(sg_heads[0], sg_heads[i])

    def drawGraph(self):
        pos = nx.shell_layout(self.G)

        nx.draw_networkx_nodes(self.G, pos, nodeList=self.G.nodes())
        nx.draw_networkx_edges(self.G, pos, nodeList=self.G.edges())
        nx.draw_networkx_labels(self.G, pos)

        weights = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=weights)
        
        plt.show()

    def w(self, u, v):
        """Get weight of edge (u,v)
        
        Arguments:
            u {int} -- Source vertex
            v {int} -- Destination vertex
        
        Returns:
            list -- Weight of (u,v)
        """

        weights = nx.get_edge_attributes(self.G, 'weight')
        return weights[(u,v)]
