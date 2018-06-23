# Install
`python -mpip install -U matplotlib`
`$ easy_install networkx`

# Import
```py
import networkx as nx
```

# Create Graph
```py
G = nx.Graph()
```

# Add Nodes
```py
G.add_node(1)
G.add_nodes_from([2,3])
```

# Add Edges
```py
G.add_edge(1,2)
```

# Get degree of node
```py
G.degree[node]
```

# Drawing
* Import the Matplotlib's plot interface to draw.
```py
import matplotlib.pyplot as plt
```