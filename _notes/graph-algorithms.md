## Basics

* graph $G=(V,E)$ contains $n$ vertices and $m$ edges

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

## Adjacency Lists

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
* Finding optimal solution out of available options.
* Branch away from a point by progressively searching every point near the original point and then expanding away from increasing distances from original point.

## Psuedocode
```
BFS(G, s)
	for each vertex $u\in V[G] - {s} do
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
* `p[*]` represents parent of vertex
* A vertex is **discovered** the first time it is visited.
* A vertex is **processed** after all outgoing edges from it have been traversed.

## Runtime
$O(n + m)$
