---
layout: post
mathjax: true
---

- [Basics](#basics)
	- [Graph Symbols](#graph-symbols)
	- [Runtime Analysis](#runtime-analysis)
	- [Principle of Optimality](#principle-of-optimality)
- [Graph Representations](#graph-representations)
	- [Adjacency Matrix](#adjacency-matrix)
		- [When to use Adjacency Matrix](#when-to-use-adjacency-matrix)
	- [Incidence Matrix](#incidence-matrix)
		- [Weighted Graph Representation](#weighted-graph-representation)
	- [Adjacency List](#adjacency-list)
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
	- [Properties](#properties-1)
	- [Stack](#stack)
	- [Predecessor Graph](#predecessor-graph)
	- [Steps](#steps-1)
	- [DFS Strategies](#dfs-strategies)
		- [Pre-order](#pre-order)
		- [In-order **INCOMPLETE**](#in-order-incomplete)
		- [Post-Order](#post-order)
	- [Pseudocode](#pseudocode)
	- [Python Implementation](#python-implementation)
		- [Iterative](#iterative)
		- [Recursive](#recursive)
	- [Runtime](#runtime-1)
- [Union-Find Data Structure](#union-find-data-structure)
	- [Methods](#methods)
- [Minimum Spanning Trees (MST)](#minimum-spanning-trees-mst)
	- [Prim's Algorithm](#prims-algorithm)
		- [Pseudocode](#pseudocode-1)
	- [Kruskal's Algorithm](#kruskals-algorithm)
		- [Pseudocode](#pseudocode-2)
- [Shortest Path](#shortest-path)
	- [Properties](#properties-2)
	- [Input](#input)
	- [Shortest Path Problem](#shortest-path-problem)
	- [Predecessor Graph](#predecessor-graph-1)
	- [Relaxation](#relaxation)
	- [Dijkstra's Algorithm](#dijkstras-algorithm)
		- [Process](#process)
		- [Runtime](#runtime-2)
	- [Bellman-Ford](#bellman-ford)
		- [Efficiency](#efficiency)
		- [Algorithm](#algorithm)
	- [Floyd-Warshall Algorithm](#floyd-warshall-algorithm)
		- [Runtime](#runtime-3)
	- [Topological Sort](#topological-sort)
		- [Runtime](#runtime-4)

# Basics

* Graph $G=(V,E)$ contains $n$ vertices and $m$ edges
	* Vertices are also called **nodes**
* **Directed Graph**
	* AKA di-graph
	* $(u,v)\ne (v,u)$
* **Weighted graph**
	* Each edge of a graph has an associated weight.
	* Weight is given by a weight function $w:E\rightarrow \mathbb{R}$

## Graph Symbols

Symbol|Meaning
---|---
$G$|Graph
$V$|Set of vertices
$E$|Set of edges
$u$ or $v$|Vertex/Node
$(u,v)$|Edge
$w(u,v)$|Weight of edge
$s$|Source Vertex
$v.\pi$|Predecessor
$G_\pi =(V_\pi ,E_\pi)$|Predecessor Subgraph
$p=\langle{v_0,v_1,...v_k}\rangle$| Path
$c=\langle{v_i,v_{i+1},...,v_j}\rangle, v_i=v_j$| Cycle
$G'=(V',E')$|Shortest-Paths Tree

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
![adjacency matrix](https://process.filestackapi.com/cache=expiry:max/dTLEaB3Q3GVvB0buaLp3)

* $G$ is represented by a $\lvert{V}\rvert \times \lvert{V}\rvert$ matrix $M_{i,j}$
* $1$ represents an edge between vertex $i$ and $j$
* $0$ represents no edge between vertices.

$$
M[i,j]=
\begin{cases}
1 & \text{if $(i,j)$ is an edge of $G$} \\
0 & \text{if $(i,j)$ is not an edge of $G$}
\end{cases}
$$

$$
M[i,j]=
\begin{array}{} j\\
i
\begin{bmatrix}
0 & 1\\
1 & 0
\end{bmatrix}
\end{array}
$$

* $i$ - Source Vertex
* $j$ - Destination Vertex

### When to use Adjacency Matrix
* Pros
	* Rapid search for edges in graph
	* Rapid update to edge insertion and deletion
* Cons
	* Uses excessive space for graphs with many vertices and few edges

## Incidence Matrix
* A directed graph with no self-loops.
* Matrix $B=\lvert{V}\rvert\times\lvert{E}\rvert$

$$
b_{i,j}=\begin{cases}
-1 & \text{if edge $j$ leaves vertex $i$} \\
1 & \text{if edge $j$ enters vertex $i$} \\
0 & \text{otherwise}
\end{cases}
$$

### Weighted Graph Representation
* `adj[i][j] = w`
		* Weighted graphs represented in an adjacency matrix displays the weight instead of 1 for an edge


## Adjacency List
![adjacency list](https://process.filestackapi.com/cache=expiry:max/Ah1Snl5rTECuaVKfU951)

* Pros
	* More efficiently stores sparse graphs
* Cons
	* Slower to find edge as it is necessary to search from head of linked list to find edge.

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
	* Stores discvored by not processed vertices in FIFO order.
		* Explore the oldest unexplored vertices first.
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
	* Backs up when surrounded by previously discovered vertices.
* Continues until all vertices $v$ that are reachable from the original source vertex $s$ have been discovered.
* Algorithm repeats process until it has discovered very vertex.

## Stack
* Stores discovered but not processed vertices.
* LIFO 

## Predecessor Graph
* Whenever a DFS discovers a vertex $v$ during a scan of an already discovered vertex $u$, it sets $v$'s predecessor attribute $v.\pi$ to $u$
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

# Union-Find Data Structure

## Methods
* `init(a)`
	* Create the data structure of $n$ elements
* `find(v)`
	* Returns head of tree containing $v$
* `union(u,v)`
	* Attach the tree of $u$ to the tree of $v$

* Checking if two vertices are part of seperate trees is simple.
* This method is used in Kruskal's algorithm when creating and joining trees.
```
if find(v) == find(u)
	v and u are part of the same tree
elif find(v) != find(u)
	v and u are part of different trees
```

# Minimum Spanning Trees (MST)
* Works on a connected, weighted, undirected graph
* **Spanning Tree**
	* An acyclic subset, or tree, $T$ of a graph that connects all vertices from a vertex $u$ to $v$
* **Minimum Spanning Tree**
	* **Unweighted Graph**
		* Tree that minimizes the number of edges.
	* **Weighted Graph**
		* Tree that minimizes the weights of edges

## Prim's Algorithm
* Starts from one vertex and grows the rest of the tree one edge at a time until all vertices are included.
* [Greedy](algorithms-basics.md#greedy-algorithms)
	* Repeatedly selects the smallest weight edge at a vertex.

1. Start from a given vertex $s$
	1. This is root of a spanning tree $T$
2. With each iteration add a new vertex to the spanning tree $T$.
	1. Always add the lowest-weight edge linking a vertex in the tree to a vertex outside of the tree.

### Pseudocode
```
Prim-MST(G)
  Select an arbitrary vertex s to start the tree from
	while (there are still nontree vertices)
	  Select the edge of minimum weight between a tree and nontree vertex
	  Add the selected edge and vertext to the tree T
```

## Kruskal's Algorithm
* The safe edge added to $A$ is always a least-weight edge in the graph that connects two distinct components.
* Greedy
	* At each step it adds to the forest an edge of least possible weight.
* More efficient than Prim's on sparse graphs.

### Pseudocode
```
MST-Kruskal(Graph, weight):
	A = []
	for each vertex (v) in Graph.vertices
		MakeSet(v)
	sort edges of G.E into non-decreasing order by weight
		if FindSet(u) != FindSet(v):
			A = A.append{(u, v)}
			Union(u,v)
	return A
```

# Shortest Path
* Given a weighted, directed graph, find the shortest path from a given **source** vertex.
	* $s\in V$

## Properties
* Edges have weights.
	* [Dijkstra's](#dijkstras-algorithm) does not work with negative weights.
	* Edges can be directed or undirected.

## Input
* $G$ - Graph
	* Made up of a set of vertices $V$ and set of edges $E$.
* $s$ - Source vertex
* $t$ - Destination vertex

## Shortest Path Problem
* Given two points, $s$ and $t$, what is the shortest path between them.

## Predecessor Graph
* $v.\pi$ represents the predecessor vertex of $v$
	* Its value is either another vertex or `null`
	* Represented by `v.p` in code

## Relaxation
* $v.d$
	* Upper bound on the weight of the shortest path from source $s$ to $v$
	* Known as the **shortest-path estimate**

```
Relax(u,v,w)
	if v.d > u.d + w(u,v)
		v.d = u.d + w(u,v)
		v.p = u
```

## Dijkstra's Algorithm
* Greedy
* Does not work with negative weights

### Process
1. Select a root node $s$ that forms a tree $T$
2. $s.d[]$ is the array of distances of every node to $s$
3. While $T$ does not span $G$
	1. Pick a node $v$ of minimum distance in $d$
		1. $v = min\{s.d\}$
	2. Add node $v$ to $T$
	3. Update the distance vector $s.d$ of neighbors of $v$ if the distance can be lowered from its previous value.

### Runtime
$O(\lvert{V}\rvert^2)$

## Bellman-Ford
* Works with edges with negative weights.
* Graph is directed.
* Uses a boolean to check if a negative-weight cycle is reachable from the source.
	* If so, there is no solution.
	* If there is no cycle, the algorithm returns the shortest paths and their weights.

### Efficiency
$O(|V|^3)$

### Algorithm
* Decreases estimates of $v.d$ on the weight of the shortest path from the source $s$ to each vertex $v\in V$ until the actual shortest-path is found.

## Floyd-Warshall Algorithm
* Dynamic Programming
* Works with negative weights.

### Runtime
$O(|V|^3)$

## Topological Sort
* For directed acyclic graphs (DAGs)
* Ordering of all vertices such that for each edge $(u,v)\in E$, $u$ comes before $v$

### Runtime
$O(n)$