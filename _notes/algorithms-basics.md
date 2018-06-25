---
layout: post
mathjax: true
---

- [Algorithm Design Guidelines](#algorithm-design-guidelines)
    - [Properties of a Good Algorithm](#properties-of-a-good-algorithm)
- [Correctness](#correctness)
    - [Incorrectness](#incorrectness)
- [Computational Problem](#computational-problem)
    - [Problem Statement](#problem-statement)
    - [Instance](#instance)
- [Algorithm Analysis](#algorithm-analysis)
    - [Big-O](#big-o)
    - [Big-$\Omega$](#big-omega)
    - [Big-$\Theta$](#big-theta)
- [Complexity Classes](#complexity-classes)
- [Vocab](#vocab)
- [Greedy Algorithms](#greedy-algorithms)

# Algorithm Design Guidelines

- Always know brute-force approach
  - Will give a baseline runtime analysis
- Avoid computation by saving states
- Simplify by pre-computing
- Divide and Conquer
- Scanning
 
## Properties of a Good Algorithm

* Correctness
* Efficiency
* Easy to Implement

# Correctness

- An algorithm is correct if, for every input instance, it halts with the correct output.

## Incorrectness
- An algorithm is incorrect if there is any instance that produces a counter-example.
    - A counter-example is any instance which yields an incorrect answer.

# Computational Problem

- Algorithms are tools that solve computational problems.
  - Algorithms do so by describing a specific computational procedure for achieving the input/output relationship.

## Problem Statement
1. Set of allowed input instances.
2. Required properties of algorithm's output.

## Instance

- The input needed to compute the solution to a computational problem.

# Algorithm Analysis
## Big-O
$$f(n)=O(g(n))$$
- $c\cdot{g(n)}$ is an upper bound on $f(n)$
- There exists some constant $c$ such that $f(n) \le c\cdot g(n)$, for $n\ge n_0$ for some constant $n_0$

## Big-$\Omega$
$$f(n)=\Omega(g(n))$$
- $c\cdot g(n)$ is a lower bound on $f(n)$
- There exists some constant $c$ such that $f(n)\ge c\cdot g(n)$ for $n\ge n_0$

## Big-$\Theta$
$$f(n)=\Theta(g(n))$$
- $c_1\cdot g(n)$ is an **upper bound** on $f(n)$
- $c_2\cdot g(n)$ is a **lower bound** on $f(n)$
- There exists some constant $c$ such that $f(n)\le c_1\cdot g(n)$ and $f(n)\ge c_2\cdot g(n)$

# Complexity Classes

| Complexity Class      | Function        | Common Cases                                                                                     |
| --------------------- | --------------- | ------------------------------------------------------------------------------------------------ |
| Constant Functions    | $f(n) = 1$      | Adding Constants<br>Printing                                                                     |
| Logarithmic Functions | $f(n) = log(n)$ | Binary search                                                                                    |
| Linear Functions      | $f(n) = n$      | Looking at each item once in an $n$-element array                                                |
| Superlinear Functions | $f(n) = nlg(n)$ | Quicksort<br>Mergesort                                                                           |
| Quadratic Functions   | $f(n) = n^2$    | Looking at all pairs of items in an $n$-element universe<br>Bubble Sort<br>Insertion Sort        |
| Cubic Functions       | $f(n) = n^3$    | Enumerate through 3-tuple or triplets of items in an $n$-element universe<br>Dynamic Programming |
| Exponential Functions | $f(n) = c^n$    | Enumerating all subsets of $n$ items                                                             |
| Factorial Functions   | $f(n) = n!$     | Generating all permutations of $n$ items                                                         |


# Vocab

- Sorting **in place**
    - Only a constant number of array elements are stored outside of the input array at any time.

- Stable
    - A sort is **stable** if two elements with equivalent keys maintain their relative position after the sort.

# Greedy Algorithms

- At a choice within an algorithm, the algorithm makes the best choice at the moment.

> Greedy algorithms make the decision of what to do next by selecting the best local option from all available choices without regard to the global structure. -**Algorithm Design Manual**
