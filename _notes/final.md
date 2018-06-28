---
layout: post
mathjax: true
---

- [Notation](#notation)
    - [Example](#example)
- [Runtime Computations](#runtime-computations)
- [Solving a Recurrence](#solving-a-recurrence)
- [Sorting](#sorting)
- [Heap](#heap)
- [How to Search](#how-to-search)
- [DP](#dp)
- [Graph Algorithms](#graph-algorithms)
    - [Minimum Spanning Trees](#minimum-spanning-trees)
    - [Shortest Path](#shortest-path)
- [P vs NP](#p-vs-np)
    - [Review on Problems](#review-on-problems)
    - [Definitions](#definitions)
    - [Polynomial](#polynomial)
    - [$NP$](#np)
        - [Simple Explanation](#simple-explanation)
    - [NP-Complete](#np-complete)
- [Co-NP](#co-np)
- [Greedy Algorithms](#greedy-algorithms)
- [Divide and Conquer](#divide-and-conquer)

# Notation

| Symbol      | Meaning                                                                      |
| ----------- | ---------------------------------------------------------------------------- |
| $\subset$   | Subset - All elements in $A$ are in $B$ but $B$ may have elements not in $A$ |
| $\subseteq$ | Proper Subset - All elements in $A$ are in $B$ and vice versa                |

## Example

# [Runtime Computations](algorithms-basics.md#algorithm-analysis)
- Big-O
- Big-$\Omega$
- Big-$\Theta$

# Solving a Recurrence

# [Sorting](sorting-algorithms.md)

| Algorithm      | Complexity    |
| -------------- | ------------- |
| Bubble Sort    | $O(n^2)$      |
| Insertion Sort | $O(n^2)$      |
| Merge Sort     | $O(n\log{n})$ |
| Heap Sort      | $O(n\log{n})$ |
| Quick Sort     | $O(n\log{n})$ |

# [Heap](binary-heap.md)

# [How to Search](searching-algorithms.md)

# [DP](dynamic-programming.md)

# [Graph Algorithms](graph-algorithms.md)

| Algorithm      | Works On                             | Type          | Implementation | Running Time                             |
| -------------- | ------------------------------------ | ------------- | -------------- | ---------------------------------------- |
| BFS            | Connected Graph                      | Connection    | Queue          | $O(\lvert{V}\rvert + \lvert{E}\rvert)$   |
| DFS            | Connected Graph                      | Connection    | Stack          | $O(\lvert{V}\rvert + \lvert{E}\rvert)$   |
| Prim           | Weighted, Undirected                 | MST           | Greedy         | $O(\lvert{V}\rvert^2)$                   |
| Kruskal        | Weighted, Undirected                 | MST           | Geedy          | $O(E\log{V})$                            |
| Dijkstra       | Directed/Undirected, Postive Weights | Shortest Path | Greedy         | $O(\lvert{V}\rvert^2 + \lvert{E}\rvert)$ |
| Bellman-Ford   | Directed/Undirected, +/- Weights     | Shortest Path |                | $O(\lvert{V}\rvert^3)$                   |
| Floyd-Warshall | Directed/Undirected, +/- Weights     | Shortest Path | DP             | $O(\lvert{V}\rvert^3)$                   |

- [BFS](graph-algorithms.md#breadth-first-search)
- [DFS](graph-algorithms.md#depth-first-search)

## Minimum Spanning Trees
- [Prim](graph-algorithms.md#prims-algorithm)
- [Kruskal](graph-algorithms.md#prims-algorithm)
- [Floyd-Warshall](graph-algorithms.md#floyd-warshall-algorithm)
- [Bellman-Ford](graph-algorithms.md#bellman-ford)

## Shortest Path
- [Dijkstra](graph-algorithms.md#dijkstras-algorithm)
- [Bellman-Ford](graph-algorithms.md#bellman-ford)
- [Floyd-Warshall](graph-algorithms.md#floyd-warshall-algorithm)

# P vs NP

## Review on Problems
* A computational problem has a specified input and possibly desired output.
* An algorithm is the tool that **solves** computational problems.
* Solving a problem is different than verifying an instance of a problem.
    * An instance is a specific input needed to compute the solution to a computational problem.

## Definitions

* **Tractable**
    * Problems that are solvable in polynomial time.
* **Intractable**
    * Problems that require superpolynomial time.
    * These problems are still solvable but not in $O(n^k)$ time.

## Polynomial
* Algorithm is $O(n^k)$ where $k$ is some positive integer and $n$ is the number of bits of input.
* A problem `P` is in class $P$ if there is an algorithm running in polytime to solve `P`
* All problems in $P$ are also in $NP$ because the problem could be solved in polynomial time without needing a certificate.
    * This means $P\subseteq{NP}$
    * $P\subset{NP}$ (or a proper subset) is still an open question.

## $NP$
* A problem `P`, that can be answered with either Yes or No, is in the class $NP$ if there is a method, given a problem instance and a certificate, to verify in polytime that the answer **Yes** is correct.
    * **Certificate**
        * A solution to the given problem.
* Consists of problems that are verifiable in polynomial time.
    * **Verifiability**
        * Given a certificate(solution), can the problem be solved in polytime with the same solution as the certificate?
            * If it is verified that the certificate is correct in polytime, then the problem is verifiable in polytime.
            * If not true, it does not prove that the problem is not verifiable in polytime, as there could be a different certificate solvable in polytime.

### Simple Explanation
* Not about solving a problem in polytime but verifying it in polytime.
* If the problem is $\ge\Omega(n^k)$ (takes greater than $n^k$ time to solve) but can be verified in $n^k$ time, then it is part of $NP$
    * If the problem cannot be verified 

## NP-Complete
* A problem `P` is in class $NP$-complete if it is in $NP$ and if all other problems in $NP$ can be reduced to $P$
* Status is unknown.
* No polytime algorithm has been discovered for an $NP$-Complete problem, nor proven that no polytime algorithm can exist for any one of them.
    * The $P\ne NP$ Question
* If any $NP$-complete problem can be solved in polytime, then every problem in $NP$ has a polytime solution ($P=NP$)

# Co-NP
* A problem `P` that can be answered with either Yes or No is in the class co-$NP$ if there is a method, given a problem instance and a certificate, to verify in polytime that the answer **No** is correct.

# Greedy Algorithms
- [Prim](graph-algorithms.md#prims-algorithm)
- [Kruskal](graph-algorithms.md#prims-algorithm)
- [Dijkstra](graph-algorithms.md#dijkstras-algorithm)

# Divide and Conquer

- [Merge Sort](sorting-algorithms.md#merge-sort)
- [Binary Search](searching-algorithms.md#binary-search)
- [Heapsort](sorting-algorithms.md#heapsort)