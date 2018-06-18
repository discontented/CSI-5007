---
layout: post
mathjax: true
---

- [Runtime Analysis](#runtime-analysis)
    - [Comparisons](#comparisons)
    - [Swaps](#swaps)
    - [General Solution](#general-solution)
- [Recursion](#recursion)
    - [Recursive Algorithms](#recursive-algorithms)
        - [Fibonacci Sequence](#fibonacci-sequence)
    - [Calculate Total Recursions](#calculate-total-recursions)
- [Dynamic Programming](#dynamic-programming)
    - [Steps](#steps)

# Runtime Analysis

## Comparisons
* For any size 4 input, there will always be 6 comparisons made with two loops

```py
for i in range(n-1):
	for j in range(i+1, n):
		if lst[i] > lst[j]
			lst.switch(i, j)
```

* Comparisons occur at `if lst[i] > lst[j]`
* Inner loop having a lower bound of 1 above the outer loop's counter (`i + 1`) results in every pair within the list being compared.

$\mid a \mid = \binom{4}{2} = 6$

## Swaps
* Count how many swaps occur per comparison.
* Here, at most, one swap occurs per comparison.
* The number of swaps to sort a size 4 array with the above code depends on how the original array is ordered and the resulting order.
* The best way is to get an upper bound on the worst case scenario, which would occur here when sorting a reverse-sorted array.

## General Solution
* Use pigeon-hole principle

# Recursion

## Recursive Algorithms

### Fibonacci Sequence
```py
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

## Calculate Total Recursions

```py
def num_operations_fibonacci(n):
    if n in [1, 2]:
        return 0

    else:
        return 1 + num_operations_fibonacci(n-1) + num_operations_fibonacci(n-2)
```

# Dynamic Programming
* Induction
    * Small smaller case and iterate through larger cases until the original, complex problem is solved.

## Steps
1. Sort the data (if necessary) so that it lends itself to a dynamic approach. 
2. Solve for the simplest case (Often $n=0$ and/or $n=1$). 
3. Recognize patterns for small  to see how they depend on smaller $n$. 
4. Come up with a recursive way to derive all values based on values that come before them.

