---
layout: post
mathjax: true
---
- [Bubble Sort](#bubble-sort)
    - [Running Time](#running-time)
    - [Loop Invariant](#loop-invariant)
    - [Python Implementation](#python-implementation)
- [Insertion Sort](#insertion-sort)
    - [Running Time](#running-time)
    - [Python Implementation](#python-implementation)
- [Merge Sort](#merge-sort)
    - [Running Time](#running-time)
    - [Python Implementation](#python-implementation)
- [Selection Sort](#selection-sort)
    - [Python Implementation](#python-implementation)
- [Heap Sort](#heap-sort)
    - [Runtime](#runtime)
    - [Book Implementation](#book-implementation)
    - [Class Implementation](#class-implementation)
        - [Python Implementation](#python-implementation)
- [Quicksort](#quicksort)
    - [Runtime](#runtime)
    - [Steps](#steps)
    - [Pivot](#pivot)
    - [Partition Algorithm](#partition-algorithm)
    - [Python Implementation](#python-implementation)

## Bubble Sort

Compares each pair of elements in an array and swaps them if they are out of order until the entire array is sorted.

### Running Time
Best Case: $\Theta(n)$

Worst Case: $\Theta(n^2)$ 

### Loop Invariant
* Enter the for loop on `i` with value `j`, array `a[0...k-1]` contains the `k` smallest elements of the set in sorted order.

### Python Implementation
```py
def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a
```

## Insertion Sort

* Builds a final sorted array one element at a time.
* Iterates through an input array and removes one element per iteration
* Finds the place the element belongs and places within the array.

### Running Time

Best Case: $\Theta(n)$

Worst Case: $\Theta(n^2)$

### Python Implementation
```py
def insertion_sort(array):
    for slot in range(1, len(array)): 
        value = array[slot]
        test_slot = slot - 1
        while test_slot > -1 and array[test_slot] > value:
            array[test_slot + 1] = array[test_slot]
            test_slot = test_slot - 1
        array[test_slot + 1] = value
    return array
```

## Merge Sort

* Recursive
* Merges two pre-sorted arrays so that the resulting array is sorted.
* Merges with an outside merge function.

### Recurrence
$T(n)=2T(n/2) + O(n)$

### Running Time
$\Theta(nlgn)$

### Python Implementation
```py
def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        m = floor(len(array) / 2)
   return merge(array[0:m], merge_sort(array[m:]))
```
## Selection Sort
* Class uses `abstractSort(a)`

### Python Implementation
```py
abstractSort(array):
	n, na = len(array), []
	for i in range(n):
		smallest = extraSmallestAndDelete(array)
		na.append(smallest)
	return na

```

## Heap Sort

* A comparison based algorithm
* Sorts in place
* Uses a [binary heap data structure](binaryHeap.md)

### Runtime
$\Theta(nlogn)$

### Book Implementation

### Class Implementation
* Uses a **min-heap**

#### Python Implementation

```py
def newheap(n):
    return [0]*(n+1)

def insert(a, e):
    a[0] = a[0] + 1
    a[a[0]] = e
    heapfixup(a,a[0])

def heapfixup(a,i):
    while i > 1:
        parent = floor(i/2)
        if a[p] > a[i]:
            a[p], a[i] = a[i], a[p]
            i = p
        else:
            return

def heapsort(x):
    n = len(x)
    a = newheap(n)
    for i in range(n):
        insert(a, x[i])
    for i in range(n):
        x[i] = extractsmallest(a)
    return x
```

## Quicksort
* Comparison-based
* Uses divide-and-conquer
* Picks a pivot point.

### Runtime

Best Case: $O(nlogn)$

Worst Case: $O(n^2)$

Average Case: $O(nlogn)$

### Steps

1. If the list is empty, return the list and terminate. (base case)
2. Choose a pivot element in the list.
3. Take all of the elements that are less than or equal to the pivot and use quicksort on them.
4. Take all of the elements that are greater than the pivot and use quicksort on them.
5. Return the concatenation of the quicksorted list of elements that are less than or equal to the pivot, the pivot, and the quicksorted list of elements that are greater than the pivot.

### Pivot

* Select a random pivot.
* Select the leftmost or rightmost element as the pivot.
* Take the first, middle, and last value of the array, and choose the median of those three numbers as the pivot (Median of Three method)
* Use a median finding algorithm such as the median-of-medians algorithm.

### Partition Algorithm
```py
def partition(a, l, u):
    t = a[l]
    m = l
    for i in range(l+1, u+1):
        if a[i] < t:
            m = m + 1
            a[i] = a[m]
            a[m] = a[i]
        a[m] = a[l]
        a[l] = a[m]
    return m
```

### Python Implementation
```py
def quicksort(a, l=0, u=None):
    if u is None:
        u = len(a) - 1
    if l < u:
        m = partition(a, l, u)
        quicksort(a, l, m-1)
        quicksort(a, m+1, u)
    return a
```

