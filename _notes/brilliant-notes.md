---
layout: post
mathjax: true
---

## Comparisons
* For any size 4 input, there will always be 6 comparisons made with two loops

```py
for i in range(n-1):
	for j in range(i+1, n):
		if lst[i] > lst[j]
			lst.switch(i, j)
```

* Comparisons occur at `if lst[i] > lst[j]`
* Two loops with the inner loop having a lower bound of 1 above the outer loop's counter (`i + 1`) results in every pair within the list is being compared.

$ |a| = \binom{4}{2} = 6$

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

print(fibonacci(10))
```

## Calculate Total Recursions

```py
def num_operations_fibonacci(n):
    if n in [1, 2]:
        return 0

    else:
        return 1 + num_operations_fibonacci(n-1) + num_operations_fibonacci(n-2)

print(num_operations_fibonacci(10))
```