import networkx as nx
import matplotlib.pyplot as plt
import random

class DiGraph:
    def __init__(self, V = None, weightL = None, weightH = None):
        self.G = nx.DiGraph()
        if V is not None:
            self.G.add_nodes_from(range(1, V + 1))
        self.randEdges()

        if (weightL and weightH) is not None:
            self.addWeight(weightL, weightH)

    def addWeight(self, low, high):
        for (u, v, w) in self.G.edges(data=True):
            w['weight'] = random.randint(low, high)

    def randEdges(self):
        for v in self.G.nodes:
            eligible = [i for i in self.G.nodes if i != v]
            u = random.choice(eligible)
            self.G.add_edge(v,u)

        # ensures connection
        self.connectDC()

    def connectDC(self):
        # Connect disconnected components in a graph
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
