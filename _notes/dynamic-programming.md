---
layout: post
mathjax: true
---
- [Elements of Dynamic Programming](#elements-of-dynamic-programming)
    - [Optimal Substructure](#optimal-substructure)
        - [Finding the Optimal Substructure](#finding-the-optimal-substructure)
- [Running Time](#running-time)
    - [Subproblem Graph](#subproblem-graph)
    - ["Bottom-Up"](#bottom-up)
- [Memoized DP Algorithm](#memoized-dp-algorithm)
    - [Runtime](#runtime)
    - [Fibonacci](#fibonacci)
        - [Runtime Analysis](#runtime-analysis)
        - [Pseudocode](#pseudocode)

# Elements of Dynamic Programming
* For dynamic programming to apply, an optimization problem must have:
    * Optimal substructure
    * Overlapping subproblems

## Optimal Substructure
* Characterizing the structure of an optimal solution.
* An optimal solution is built from optimal solutions to subproblems.
* **Optimal Substructure**
    * An optimal solution of a problem contains within it optimal solutions to subproblems.

### Finding the Optimal Substructure
* Keep the space as simple as possible and then expand it as necessary.
1. Show that a solution to a problem consists of making a choice.  This choice leaves one or more subproblems to be solved.
2. Suppose for the given problem, you are given the choice that leads to the optimal solution.
    1. Given the choice, determine which subproblems ensue and how to best characterize the subproblems.
    2. Show that solutions to the subproblems are themselves optimal.
        1. Suppose that each of the subproblem solutions are not optimal and then derive a contradiction.

# Running Time
* Depends on the product of **the number of subproblems overall** and **how many choices we look at for each subproblem**

## Subproblem Graph
* An alternative way of analysis
* Each vertex corresponds to a subproblem.
* Choices are edges incident from that subproblem.

## "Bottom-Up"
* Optimal solutions to subproblems are found first.
* Involves making a choice among subproblems as to which we will use in solving the problem.
* The cost of the problem is the cost of the subproblem plus the cost of the choice itself.

# Memoized DP Algorithm
Recursion + memoization
* Remember solutions and reuse solutions to subproblems that help solve the problem.
    * "Memo" comes from the idea of using a scratch pad or memo to log results (as you would in calculating an equation without memory) and using those answers to find the final answer.
## Runtime
* time = # of subproblems * the amount of time you spend per subproblem

## Fibonacci
```
memo = {}
fib(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        f = 1
    else:
        f = fib(n-1)+fib(n-2)
        memo[n]=f
    return f
```

1. Create empty `memo` dictionary
2. Check if `fib(n)` is already in the dictionary (it has already been computed)
    1. If not, comput the fib number
3. Store `fib(n)` into `memo[n]` and return `f`

### Runtime Analysis
* Only making recursive calls the first time `fib(k)` it's called.
    * The memoized calls are constant time ($\Theta(1)$)
* The number of non-memoized calls is $n$ since `fib(k)` is done the first time and only done once for each number $<= n$

Runtime = $\Theta(n)$

### Pseudocode
* Uses a hash table for look up instead of function calls

```py
fib = {}
for k in range(1, n+1):
    if k <= 2:
        f = 1
    else:
        f = fib[k-1] + fib[k-2]
    fib[k] = f
return fib[n]
```
* Answers to subproblems are stored in a dictionary of $1...n$
* The only answer cared about is `fib[n]` which is returned.