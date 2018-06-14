---
layout: post
mathjax: true
---
# Problem
Consider a (large) set of size $n$ of items. Each item has a weight $(0 \le w_i \le W)$. Your job is to fit all these items in containers. All containers are identical and can hold up to weight $(W)$.

## Objectives
* Fit into as few containers as possible.
* Write up a brute force algorithm to get a baseline.
* Consider an approximation algorithm called "first-fit": This algorithm repeatedly traverses the list of items and inserts into the last bin the first item that fits into it. If no item fits, it opens a new bin and goes through the list again until all items are gone.
    * Code this algorithm and contrast it to your brute force. You should see that it runs much faster, but the solution could be much worse. Try to quantify how bad it can be.
* Finally, write a dynamic programming solution (either exact or approximate).
* Test your various algorithms on random data of various sizes and plot the runtimes.

# Brute Force Methods

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
|Symbol|Meaning|
|---|---|
|$w$|Bin Max Capacity|

$ W \equiv Total Array Weight $

* If $W$, or max bin capacity, is equal to the sum of the array, all items should fit into the bin.
