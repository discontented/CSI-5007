---
layout: post
mathjax: true
---

# Problem Statement
Find subset $\bar{S}\subseteq{S}$ that maximizes the value of $\sum_{i\in\bar{S}}v_i$ given that all items fit in a knapsack of size $W$

# Input
A set of items $S={1,...,n}$
* item $i$ has size $s_i$ and value $v_i$

# Integer Partition
* AKA "Price-Per-Pound" Knapsack problem, subset sum
* A subset of items must add up to the capacity of the knapsack $W$
* Partition the elements of $S$ into two sets $A$ and $B$
* Ideal: $\sum_{a\in{A}}a = \sum_{b\in B}$
	* Alternative: make the difference as small as possible.

### Runtime
Time: $O(nC)$

Space: $O(C)$


