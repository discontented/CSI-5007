# Backtracking
* Backtracking is a systematic way to iterate through all possible configurations of a **search space**
* Each step in a backtracking algorithm extends a given partial solution $a = (a_1, a_2, ..., a_k)$ by adding another element at the end.
* After extension, check to see if the found partial solution is the solution.
	* If it is not, check if the partial solution is extendable and extend.
* Constructs a tree of partial solutions.
	* Each vertex represents a partial solution.
	* Finding a solution is then a depth-first search.

## Applications
* Find all possible permutations.
* Enumerating all spanning trees of a graph.

## Pseudocode
Backtrack-DFS(A, k):
	if $A = (a_1, a_2, ..., a_k)$ is a solution
		report it
	else
		$k = k + 1$
		compute $S_k$
		while $S_k \ne \emptyset$ do
			$a_k =$ an element in $S_k$
			$S_k = S_k - a_k$
			Backtrack-DFS(A, k)

### Correctness
* Enumerates all possibilities.

### Efficiency
* Never visits a state more than once.
