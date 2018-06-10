---
layout: post
mathjax: true
---

- [Basics](#basics)
    - [Runtime Analysis](#runtime-analysis)
    - [Principle of Optimality](#principle-of-optimality)
- [Graph Representations](#graph-representations)
    - [Adjacency Matrix](#adjacency-matrix)
    - [Adjacency List](#adjacency-list)
        - [Adjacency List Implementation](#adjacency-list-implementation)
- [Graph Traversal](#graph-traversal)
    - [Key Ideas](#key-ideas)
        - [Vertex States](#vertex-states)
- [Breadth First Search](#breadth-first-search)
    - [Application](#application)
    - [Properties](#properties)
    - [Steps](#steps)
    - [Psuedocode](#psuedocode)
    - [Runtime](#runtime)
- [Depth First Search (DFS)](#depth-first-search-dfs)
- [Applications](#applications)
    - [Properties](#properties)
    - [Predecessor Graph](#predecessor-graph)
    - [Steps](#steps)
    - [DFS Strategies](#dfs-strategies)
        - [Pre-order](#pre-order)
        - [In-order **INCOMPLETE**](#in-order-incomplete)
        - [Post-Order](#post-order)
    - [Pseudocode](#pseudocode)
    - [Python Implementation](#python-implementation)
        - [Iterative](#iterative)
        - [Recursive](#recursive)
    - [Runtime](#runtime)
- [Minimum Spanning Trees (MST)](#minimum-spanning-trees-mst)
    - [Prim's Algorithm](#prims-algorithm)
        - [Pseudocode](#pseudocode)
    - [Kruskal's Algorithm](#kruskals-algorithm)

# Basics

* graph $G=(V,E)$ contains $n$ vertices and $m$ edges

## Runtime Analysis
* The runtime of a graph algorithm for a given graph $G=(V,E)$ is measured in terms of the number of vertices ($\lvert V\rvert$) and number of edges ($\lvert E\rvert$)
* Inside asymptotic notation, the cardinality is ommitted.
    * $\Theta(\lvert V\rvert, \lvert E\rvert)\equiv \Theta(V, E)$

## Principle of Optimality
> If $v_1,...,v_j,...,v_k$ is a shortest path from $v_1$ to $v_k$ passing through $v_j$, then the subpath $v_1,...,v_j$ is a shortest path from $v_1$ to $v_j$

# Graph Representations

|Graph|Data Structure|
|---|---|
|Sparse Graph $(\lvert E\rvert << {\lvert V\rvert}^2)$|[Adjacency List](#adjacency-list)|
|Dense Graph $(\lvert E\rvert << {\lvert V\rvert}^2)$|[Adjancency Matrix](#adjacency-matrix)|

## Adjacency Matrix
* $G$ is represented by a $n \times n$ matrix $M$

$$
M[i,j]=
\begin{cases}
1 & \text{if $(i,j)$ is an edge of $G$} \\
0 & \text{if $(i,j)$ is not an edge of $G$}
\end{cases}
$$

* Pros
    * Rapid search for edges in graph
    * Rapid update to edge insertion and deletion
* Cons
    * Uses excessive space for graphs with many vertices and few edges

## Adjacency List
* Pros
    * More efficiently stores sparse graphs
* Cons
    * Slower to find edge as it is necessary to search from head of linked list to find edge.


### Adjacency List Implementation
```c
#define MAXV 1000

typedef struct {
    int y;
    int weight;
    struct edgenode *next;
} edgenode;

typedef struct {
    edgenode *edges[MAXV+1];
    int degree[MAXV+1];
    int nvertices;
    int nedges;
    bool directed;
} graph
```

# Graph Traversal

## Key Ideas
* Mark every vertex which is visted to keep track of if the graph has been completely explored.
    * There are numerous implementations of this, such as tracking visited nodes by adding to an array, or changing the state on the property of a vertex if it is coded as an object.

### Vertex States

|State|Description|
|---|---|
|undiscovered|Vertex is in its initial state and has not been visited.|
|discovered|Vertex has been found but incident edges have not been checked.|
|processed|Vertex where all incident edges have been visited.

# Breadth First Search
![bfs brilliant](https://ds055uzetaobb.cloudfront.net/image_optimizer/62cdd0cb92ee8629cb1422e04d76a12da176bd02.gif)

## Application
* Finding optimal solution out of available options.
    * Find connected components
* Find shortest path in unweighted graphs.
* Test for bipartite property.

## Properties
* Builds a breadth-first tree with root $s$
    * $s$ - A distinguished source vertex.
* Explores edges of $G$ to **discover** every vertex that is reachable from $s$.
    * Vertex is **discovered** the first time it is encountered in a search.
* Distance ($d$) is the shortest path from any vertex $v$ to the source vertex $s$
* Algorithm discovers all vertices at distance $k$ from $s$ before discovering any vertices at $d = k + 1$
* $u.\pi$ represents the predecessor of $u$ in book psuedocode.
* Uses a queue

## Steps
1. Pick source vertex, `s`, from graph.
    1. `s` becomes the root of the tree.
2. Look at each neighbor in an order.
3. Visit each neighbor vertex in that same order.
4. Repeat breadth-first search for each `k+1` vertex from `s`

## Psuedocode
```
BFS(G, s)
    for each vertex $u\in V[G] - {s}$ do
        state[u] = "undiscovered"
        p[u] = nil //no parent is in BFS tree
    state[s] = "discovered"
    p[s] = nil
    Q = {s}
    while Q != $\emptyset$ do
        u = dequeue[Q]
        process vertex u as desired
        for each $v \in Adj[u]$ do
            process edge $(u,v)$ as desired
            if state[v] = "undiscovered" then
                state[v] = discovered"
                p[v] = u
                enqueue[Q, v]
        state[u] = "processed"
```

* `p[*]` represents predecessor of vertex
* A vertex is **discovered** the first time it is visited.
* A vertex is **processed** after all outgoing edges from it have been traversed.

## Runtime
$O(n + m)$

# Depth First Search (DFS)
![dfs](https://ds055uzetaobb.cloudfront.net/image_optimizer/35a0e3d657f653ec7b3c6113ad4b55264cae5516.gif)

# Applications
* Connnected components
* Topological Sorting
    * **Topological Sort**
        * Linear ordering of its vertices such that for every directed edge $uv$ from vertex $u$ to vertex $v$, $u$ comes before $v$ in the ordering.
* Finding cycles in directed graphs

## Properties
* Finds the longest path of a graph $G$
* Explores deep into a graph whenever possible.
* Uses a stack to keep track of vertices.
* Explores edges out of the most recently discovered vertex $v$ that still has unexplored edges leaving it.
* Once $v$'s edges have been explored, the search backtracks to explore edges leaving the vertex from which $v$ was discovered.
* Continues until all vertices $v$ that are reachable from the original source vertex $s$ have been discovered.
* Algorithm repeats process until it has discovered very vertex.

## Predecessor Graph
* Whenever a DFS discoveres a vertex $v$ during a scan of an already discovered vertex $u$, it sets $v$'s predecessor attribute $v.\pi$ to $u$
* The predecessor subgraph produced by a DFS forms a **predecessor forest** because the search may repeat from multiple source ($s$) vertices

_Predecessor Subgraph Representation_
$$
G_{\pi}=(V,E_{\pi}), \text{where } E_{\pi}={(v.\pi,v):v\in V \text{and } v.\pi \neq NIL}
$$

## Steps
1. Visit a vertex $s$
2. Mark $s$ as visited
3. Recursively visit each unvisited vertex attached to $s$

## DFS Strategies
### Pre-order
* Visit source node $s$.
* Successively move left to visit each node ($v$) until a leaf is reached.
* When there are no more children to left of $s$ node.

### In-order **INCOMPLETE**
* Find left-most node in tree and visit.
* Vist the parent of that node.
* Visit right child of this parent node.
    * Find next left-most node.

### Post-Order
* Visit left-most leaf in tree.
* Visit parent and then find second left-most leaf.
* Repeat until the parent is the last node within a branch.

## Pseudocode
```
Initialize an empty stack for storage of nodes, S.
For each vertex u, define u.visited to be false.
Push the root (first node to be visited) onto S.
While S is not empty:
    Pop the first element in S, u.
    If u.visited = false, then:
        U.visited = true
        for each unvisited neighbor w of u:
            Push w into S.
End process when all nodes have been visited.
```

## Python Implementation
### Iterative
```py
def depth_first_search(graph):
    visited, stack = set(), [root]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
```

### Recursive
```py
def depth_first_search_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        depth_first_search_recursive(graph, next, visited)
    return visited
```

## Runtime
If using a adjacency list, $O(V+E)$

# Minimum Spanning Trees (MST)
* **Spanning Tree**
    * An acyclic subset, or tree, $T$ of a graph that connects all vertices from a vertex $u$ to $v$
* **Minimum Spanning Tree**
    * A spanning tree that has the least weight.

## Prim's Algorithm
* Starts from one vertex and grows the rest of the tree one edge at a time until all vertices are included.
* Greedy
	* Repeatedly selects the smallest weight edge at a vertex.
1. Start from a given vertex.
2. With each iteration add a new vertex to the spanning tree.
    1. Always add the lowest-weight edge linking a vertex in the tree to a vertex outside of the tree.
        1. A boolean array tracks whether a vertex has already been added to the tree.

### Pseudocode
```
Prim-MST(G)
  Select an arbitrary vertex s to start the tree from
    while (there are still nontree vertices)
	  Select the edge of minimum weight between a tree and nontree vertex
      Add the selected edge and vertext to the tree T
```

## Kruskal's Algorithm
* More efficient than Prim's on sparse graphs.
