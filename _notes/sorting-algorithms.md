---
mathjax: true
layout: post
---

- [Bubble Sort](#bubble-sort)
    - [Running Time](#running-time)
    - [Loop Invariant](#loop-invariant)
    - [Python Implementation](#python-implementation)
- [Insertion Sort](#insertion-sort)
    - [Running Time](#running-time)
    - [Python Implementation](#python-implementation)
- [Merge Sort](#merge-sort)
    - [Python Implementation](#python-implementation)
    - [Running Time](#running-time)
- [Heap Sort](#heap-sort)
    - [`min-heap` property](#min-heap-property)
    - [Python Implementation](#python-implementation)
    - [Runtime](#runtime)

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

### Python Implementation
```py
def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        m = floor(len(array) / 2)
        return merge(array[0:m], merge_sort(array[m:]))
```

### Running Time
$\Theta(nlgn)$

## Heap Sort

### `min-heap` property

$a[\lfloor{i/2}\rfloor]\leq{a[i]}$

### Python Implementation

```py
def heapsort(x):
    n = len(x)
    a = newheap(n)
    for i in range(n):
        insert(a, x[i])
    for i in range(n):
        x[i] = extractsmallest(a)
    return x
```

### Runtime
$\Theta(nlogn)$