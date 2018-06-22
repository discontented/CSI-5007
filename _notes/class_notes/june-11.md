---
layout: post
mathjax: true
---

# Must Know Algorithms
Prim, Kruskal, Dijkstra

# Hashmap
* No ordering

## Objectives
* Any data types.
* Average Runtime
	* $O(1)$
* Array is fixed length with fixed element size.

## Assumptions
* A universe of $U$ keys
* Map keys to ${1, 2, ..., \lvert U\rvert }$
* A string has a mapping to an integer so that each character has an integer.
	* Allows converting from string to integer.

## Hash Function
* Input: a big number
${1,2,...,\lvert U\rvert }$
* Output: An integer which is a position in the array.
${1,...,n-1}$

### Collision
* Two keys that map to same place
* Unavoidable if universe of keys is larger than array.
	* Pigeonhole principle
* Resolved by **chaining**
	* An index that contains two objects will be a linked list.
	* First element is head of list and points to other pointers with same hashmap key.
		* Affects runtime as must iterate through linked list.

* `Chained-Insert(H,x)`
	* Insert at head of linked list
	* $O(1)$
* `Chained-Search(H,k)`
	* Search for element with key `k`
	* $O(l)$
		* $l$ is list length

### Runtime
* Based on load factor

$\Theta(1+\alpha)$ on average
#### Example
* If you have 10x the elements of total positions in the array, you would have 10 items in each slot.
	* This only gives $\alpha = 10$ so it is close to $\Theta(1)$

## Load Factor
$\alpha = \frac{n}{m}$
* Could be as small as 0
* No upper bound

* Keep the load factor low to keep runtime $O(1)$
	* Reallocate to a new array to keep the number of slots high.

# Hash Functions
## Collision
### Division Method
$h(k)=k mod m$
* Don't want m to be power of 2
* Needs to use all the bits of the key
	* Use primes

### Multiplicative Method
* Faster than division
1. Pick a fraction between 0 and 1
$h(k)=\lfloor m(kA-\lfloor kA\rfloor)\rfloor$
* Want m to be a power of 2.
	* Multiplication by 2 is a shift.
	* Store $kA$ as it is calculated twice.

## Open Addressing
* No linked list
* All elements stored in array of length $m$
* Never let load factor get to 1
* Uses a probe sequence to find empty slots

### Probing
#### Linear Probing
$h(k,i)=h'(k)+i mod m$
* $h'(k)$ is one of the hash functions.
* Clustering occurs as it continually checks the next available slot.
	* If a slot is filled it will choose the next.

#### Quadratic Probing
* No clustering

#### Double Hashing
* Use one that is a multiplication hash function and one that is division.
	* $h''(k)$ is either multiplication or division
	* $h'(k)$ is the other

### Negatives of Open Addressing
* When reallocating, you must rehash every item because the hash functions depend on the size of the array, $m$

# Dynamic Programming
`H.get(str([p,n]), None)`
* Look up a string in a hashmap.  If it does not exist, return `None`

* Bottom-up
	* `A3` code example

# Really Hard Problems
## Travelling Salesman
* All solutions are cycles.
* Multiple permutations may be the same cycle.
	* $(0,1,2)\equiv (2,0,1)$
	* These are only shifted by 1 position.

### Search Space
* $n$ Permutations $=n!$

1. Find all essential tours.

```
def calc_cost(p, D):
```
* `p` is a permutation
* `D` is distance matrix
	* Throughout all TSP implementations in this course, it is using a matrix.
	* If the existing graph is not complete, it is "made complete" by setting each nonexisting edge to $\infty$

### Tree Walking
```
def visit_0(v,n)
```
* k - current length
* v - starts empty
	* A vector of permutation.

#### Runtime
1. Empty array
	1. Complement is every other array.

| Call                          | Runtime |
| ----------------------------- | ------- |
| `[]`                          | 1       |
| `[0],[1],...[n-1]`            | $n$     |
| `[2]->[2,0],[2,1],...[2,n-1]` | $n-1$   |

Runtime: $O(n!)$

#### Change Code for More efficiency
```
if you're at a leaf node
compute the cost and compare to your current best.
```
* Same permutations
	* If they are shifted or backwards
	* Shifting solved by setting the starting node to `[0]`
		* Improves runtime by factor of $n$
		* Now runtime is $(n-1)!$
	* Backwards may be solved by a comparison
		* Improves runtime by halving
		
* Do minimum amount of work
	* Assumption: You have current best.
		* If you know your minimum best, then approx. the future best and avoid that branch.
		* achieved by `if cost < best`

## Extension Bound
* Calculates best possible extension bound.
$\sum_{i=0}^{i=l-1}c[v_i, v_{i+1}$
_markdown error


