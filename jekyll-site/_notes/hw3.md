---
layout: post
mathjax: true
---
- [Problem](#problem)
    - [Objectives](#objectives)
- [The Bin Packing Problem](#the-bin-packing-problem)
    - [One-Dimensional Bin Packing](#one-dimensional-bin-packing)
    - [Online](#online)
    - [Offline](#offline)
        - [Offline Heuristics Insertion Rules](#offline-heuristics-insertion-rules)
    - [Optimal Heuristic](#optimal-heuristic)
        - [Runtime](#runtime)
- [Brute Force Methods](#brute-force-methods)
    - [Insert as Encountered](#insert-as-encountered)
    - [Largest Items in Separate Bins](#largest-items-in-separate-bins)
    - [Recursion](#recursion)
        - [Base Case](#base-case)
        - [Recursive Case](#recursive-case)
- [Approximation](#approximation)
    - [First-Fit](#first-fit)
- [Test Scenarios](#test-scenarios)
    - [Calculate Total Array Weight](#calculate-total-array-weight)

# Problem
Consider a (large) set of size $n$ of items. Each item has a weight $(0 \le w_i \le W)$. Your job is to fit all these items in containers. All containers are identical and can hold up to weight $(W)$.

## Objectives
* Fit into as few containers as possible.
* Write up a brute force algorithm to get a baseline.
* Consider an approximation algorithm called "first-fit": This algorithm repeatedly traverses the list of items and inserts into the last bin the first item that fits into it. If no item fits, it opens a new bin and goes through the list again until all items are gone.
    * Code this algorithm and contrast it to your brute force. You should see that it runs much faster, but the solution could be much worse. Try to quantify how bad it can be.
* Finally, write a dynamic programming solution (either exact or approximate).
* Test your various algorithms on random data of various sizes and plot the runtimes.

# The Bin Packing Problem
## One-Dimensional Bin Packing
* Each object's size is an integer.
* A special case of the Knapsack Problem

## Online
* Know the size as they arrive.

## Offline
* Know the complete set of objects at the beginning of the job.
* Best solution is to sort the objects from largest to smallest

### Offline Heuristics Insertion Rules
1. Select first and leftmost bin the object fits in.
2. Select the bin with the most room
3. Select the bin that provides the tightest fit
4. Select a random bin

## Optimal Heuristic
__first-fit decreasing__
* Sort objects in decreasing order of size.
* Insert each object one by one into the first bin that has room for it.
* If no bin has room, create another bin.

### Runtime
$n$ - Number of items
$m$ - Number of bins
$b$ - Number of bins actually used

$O(nlg(n)+bn), where b\le min(n,m)$
* Faster runtim is $O(nlg(n))$ if using a binary tree to keep track of remaining space in each bin.

# Brute Force Methods
## Pseudocode

```py
"""
a - input array of n items
w - max weight of bin
"""
def bruteForce(a, w):
    # sort from max to min
    MaxToMin(a)

    # Separate all large items that would not fit together.
    createBins(a, w)

    x = calculateSpace(bin)

    for remaining items in a:
        optimizeCapacity(item, x)

"""
Fills bin based on remaining empty space (x).
"""
def optimizeCapacity(item, x):
    if item.weight == x
        insert item into bin
        remove item from a
    elif item.weight < x
        optimizeCapacity(item, x-1)

"""
Creates all needed bins for items that are over half the value of the max weight (w)
"""
def createBins(a, w)
    for item in a:
        if item.weight > w:
            create new bin
            insert item into bin
```

## Insert as Encountered
* $k$ is some item within the total size of the input.
    * $0\le k \le n$
* Say the array of the input is $A[]$
* Insert items into a bin until it has reached max capacity.
    * $A[0...k-1]$ are the items that will fit.
    * As $A[k]$ must either be attempted to fit or guessed to fit by its size, it must either:
        * Be removed from the bin and saved for the next.
        * Position $k$ maintained for the next iteration.

## Largest Items in Separate Bins
1. Sort the input array from max to min sizes.
2. If an item is more than half the size of the max capacity $(W)$, insert it into its own bin.
    1. `half = w // 2`
3. Iterate through each bin, placing the next items in the array into the bin until it is filled.
    1. These items should be successively the largest as the array is sorted.
    2. If the item doesn't fit, continue onto the next bin.
4. Iterate through each bin until the array is emptied.

## Recursion

### Base Case
* If $A[i].weight \equiv \lfloor w\rfloor$
    * remove and return $A[i]$

### Recursive Case
* The array can continue to be divided in two.
    * $\lfloor\frac{w}{2}\rfloor\ne0$
    * The original array still has items to be removed.

# Approximation
## First-Fit
* Iterates through the list for the best fit for the next bin.
* Must keep a difference between the max capacity and current load in bin.
* Must compare between an item's value and this capacity difference.

# Test Scenarios
## Calculate Total Array Weight

| Symbol | Meaning          |
| ------ | ---------------- |
| $w$    | Bin Max Capacity |

$ W \equiv Total Array Weight $

* If $W$, or max bin capacity, is equal to the sum of the array, all items should fit into the bin.
