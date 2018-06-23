---
layout: post
mathjax: true
---

# Install
`$ python -mpip install -U matplotlib`

`$ easy_install networkx`

# Import
```py
import networkx as nx
```

# Create Graph
```py
G = nx.Graph()
```

## Directed Graph
```py
DG = nx.DiGraph()
```

# Graph Manipulation

## Add Nodes
```py
G.add_node(1)
G.add_nodes_from([2,3])
```

## Add Edges
```py
G.add_edge(1,2)
```

### Adding Weight
```py
G[1][2]['weight'] = 4
G.edges[3,4]['weight'] = 4.2
```

## Removal
```py
G.remove_node(2)
G.remove_edge(1,3)
```

# Graph Attributes
```py
G.number_of_nodes()
G.number_of_edges()
```

```py
nodes = list(G.nodes)
edges = list(G.edges)
neighbors = list(G.adj[n]) //Neighbors of vertex n
G.degree[node]
```

## DiGraph Attributes
```py
DiGraph.predecessors()
```

# Drawing
* Import the Matplotlib's plot interface to draw.
```py
import matplotlib.pyplot as plt
```