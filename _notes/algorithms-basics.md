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
- $f(n)=O(g(n))$ means $c\bullet{g(n)}$ is an upper bound on $f(n)$
    - There exists some constant $c$ such that $f(n)$ is always $\le c\bullet g(n)$, for large enough $(n)$ ($n\ge n_0$ for some constant $n_0$)
- $f(n)

# Vocab

- Sorting **in place**
    - Only a constant number of array elements are stored outside of the input array at any time.

- Stable
    - A sort is **stable** if two elements with equivalent keys maintain their relative position after the sort.

# Greedy Algorithms

- At a choice within an algorithm, the algorithm makes the best choice at the moment.

> Greedy algorithms make the decision of what to do next by selecting the best local option from all available choices without regard to the global structure. -**Algorithm Design Manual**
