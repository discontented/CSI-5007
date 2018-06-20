# Problem Statement
Consider a (large) set of size $n$ of items. Each item has a weight $(0 \le w_i \le W)$. Your job is to fit all these items in containers. All containers are identical and can hold up to weight $(W)$.

# Brute Force Approach

## Correctness

## Runtime

# Heuristic Approach
1. Sorts objects from max to min
2. Insert each object into first bin which has room for it.
    1. If no room in bin, create a new one.
```py
def firstFit(a, w):
    """
    Arguments:
        a {list[int]} -- Element values are the item's weight.
        w {int} -- The max weight of all bins.
    """

    a.sort(reverse = True)

    # Contains all bins. Initializes empty bin of bins.
    bins = []

    # iterate through all items in original array
    for item in a:
        # Iterate through all bins. Breaks when item is inserted.
        for bin in bins:
            if (item <= bin.capacity()):
                bin.insert(item)
                break
        # Iterates through all bins and cannot find a fit. Create new bin.
        else:
            bins.append(Bin(w, item))
    
    return bins
```

## Runtime
* Items to be inserted (`a`) are sorted in $O(nlog(n))$ time.
* The number of bins is dependent on $W$, or the max capacity of each bin, and the weights ($w_i$) of each individual item.

# Test Results
n | Brute Force | Heuristic
---|---|---
0 | 0 bins in 0.000002 s| 0 bins in 0.000004 s
5 | 3 bins in 0.000067 s| 3 bins in 0.000197 s
10 | 5 bins in 0.000792 s| 5 bins in 0.000365 s
15 | 6 bins in 0.018118 s| 6 bins in 0.000587 s
20 | 9 bins in 0.664633 s| 9 bins in 0.000735 s
25 | 11 bins in 23.846549 s| 11 bins in 0.001773 s