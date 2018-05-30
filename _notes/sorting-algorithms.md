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
    - [Binary Heap Data Structure](#binary-heap-data-structure)
    - [`max-heap` property](#max-heap-property)
    - [`min-heap` property](#min-heap-property)
    - [Heapsort Algorithm](#heapsort-algorithm)
        - [Python Implementation](#python-implementation)
    - [Runtime](#runtime)
- [Quicksort](#quicksort)
    - [Steps](#steps)
    - [Pivot](#pivot)
    - [Partition Algorithm](#partition-algorithm)
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

* A comparison based algorithm
* Sorts in place
* Uses a binary heap data structure

### Binary Heap Data Structure
* Uses an array
  * Book uses an array object `A`
  * Object has two attributes
    * `A.length`
      * Gives number of elements in the array.
    * `A.heapsize`
      * Number of elements in the heap stored in array `A`
* Root is stored in position 1

The parent of a node at index $i$ is $\lfloor{i/2}\rfloor$

```py
def parent(i):
	return math.floor(i / 2)
```

The left child of a node at index $i$ is $2i$

```py
def leftChild(i):
	return 2 * i
```

The right child of a node at index $i$ is $2i+1$

```py
def rightChild(i):
	return (2 * i) + 1
```

### `max-heap` property

* A node cannot have a greater value than its parent.
* The largest element is the root.
* The minimum elements are the leaves.

`A[parent(i)] >= A[i]`

### `min-heap` property

* A parent node cannot have a greater value than its children.
* The minimum element is the root.
* The max elements are the leaves.

`A[parent(i)] <= A[i]`

### Heapsort Algorithm
1. Build a maxheap
2. Sort

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
        p = floor(i/2)
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

### Runtime
$\Theta(nlogn)$

## Quicksort
* Comparison-based
* Uses divide-and-conquer
* Picks a pivot point.

### Steps

1. If the list is empty, return the list and terminate. (base case)
2. Choose a pivot element in the list.
3. Take all of the elements that are less than or equal to the pivot and use quicksort on them.
4. Take all of the elements that are greater than the pivot and use quicksort on them.
5. Return the concatenation of the quicksorted list of elements that are less than or equal to the pivot, the pivot, and the quicksorted list of elements that are greater than the pivot.

### Pivot

* Select a random pivot.
* Select the leftmost or rightmost element as the pivot.
* Take the first, middle, and last value of the array, and choose the median of those three numbers as the pivot (Median of Three method).[2]
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
def quicksort(a):

```

### Runtime

Best Case: $O(nlogn)$

Worst Case: $O(n^2)$

Average Case: $O(nlogn)$
