---
layout: post
mathjax: true
---

- [The Sorting Problem](#the-sorting-problem)
- [Bubble Sort](#bubble-sort)
    - [Running Time](#running-time)
    - [Loop Invariant](#loop-invariant)
    - [Python Implementation](#python-implementation)
- [Insertion Sort](#insertion-sort)
    - [Steps](#steps)
    - [Invariant](#invariant)
    - [Python Implementation](#python-implementation-1)
    - [Running Time](#running-time-1)
- [Merge Sort](#merge-sort)
    - [Steps](#steps-1)
    - [Python Implementation](#python-implementation-2)
    - [Recurrence](#recurrence)
    - [Running Time](#running-time-2)
- [Heapsort](#heapsort)
    - [Runtime](#runtime)
    - [Class Implementation](#class-implementation)
        - [Python Implementation](#python-implementation-3)
- [Quicksort](#quicksort)
    - [Runtime](#runtime-1)
    - [Steps](#steps-2)
    - [Pivot](#pivot)
    - [Partition Algorithm](#partition-algorithm)
    - [Python Implementation](#python-implementation-4)
- [Bin/Bucket Sort](#binbucket-sort)

# The Sorting Problem

**Input**: A sequence of $n$ numbers $\langle{a_1,a_2,...,a_n}\rangle$

**Output**: A permutation of the sequence in increasing or decreasing order.

- **Ascending**
  - $a\cdot{i} \le a\cdot{i+1}$ for all $1\le i<n$
- **Descending**
  - $a\cdot{i} \ge a\cdot{i+1}$ for all $1\le i<n$

# Bubble Sort

![bubble sort](https://ds055uzetaobb.cloudfront.net/image_optimizer/4f60337caedcc96ffeb08692e4f8d00f5cb3fd58.gif)

Compares each pair of elements in an array and swaps them if they are out of order until the entire array is sorted.

## Running Time

Best Case: $\Theta(n)$

Worst Case: $\Theta(n^2)$

## Loop Invariant

- Enter the for loop on `i` with value `j`, array `a[0...k-1]` contains the `k` smallest elements of the set in sorted order.

## Python Implementation

```py
def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a
```

# Insertion Sort

![insertion sort](https://ds055uzetaobb.cloudfront.net/image_optimizer/5fc8daa9296837453ccbc8c7f9c2494bbd1fcdda.gif)

- Sorts out of place
- Builds a final sorted array one element at a time.
- Finds the place the element belongs and places within the array.
- "Out of place" sorting as it is storing a key in a variable.

## Steps

Variable|Value
---|---
`A`|Array containing values to be sorted.
`j`|Key value index position.
`key`|Value of key, which will be base of comparison.
`i`|Index of item to the left of `key` being compared.

1. Establish your comparison key.
    1. Start at second index (`j`) of an array.
    2. Store the value at `j` as the `key`
        1. `key = A[j]`
2. Decrement through array to the left, or towards the initial index, and compare until all elements to the left have been compared.
    1. Set `i` to the value to the left of the key (`i = j - 1`)
    2. If value to the left (`i`) is greater than the `key`, swap the positions.
        1. `A[i]` is copied to the slot to the right `A[i + 1]`
        2. `i` is decremented to a slot to the left.

## Invariant
* The array to the left of the comparison index is sorted.

## Python Implementation

```py
def insertSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
```

## Running Time

Best Case: $\Theta(n)$

- Numbers are already sorted

Worst Case: $\Theta(n^2)$

# Merge Sort

![merge sort](https://ds055uzetaobb.cloudfront.net/image_optimizer/8c074d46d4c96077d11f9e8cab9ff5d95bdc3da0.gif)

- Merges two pre-sorted arrays so that the resulting array is sorted.
- Merges with an outside merge function.

## Steps
1. If the list has only one element, return the list and terminate.
2. Split the list into two halves
    1. If odd, the first list will be the larger.
3. Sort both lists using mergesort
4. Merge the two sorted lists and return the result.

## Python Implementation

```py
def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        m = floor(len(array) / 2)
   return merge(array[0:m], merge_sort(array[m:]))
```

## Recurrence

$T(n)=2T(\frac{n}{2}) + O(n)$

## Running Time

$\Theta(nlg(n))$



# Heapsort

![heap sort](https://ds055uzetaobb.cloudfront.net/image_optimizer/c1fc9fb4a40d810259ea8291ffde0eef182e7d57.gif)

- A comparison based algorithm
- Sorts in place
- Uses a [binary heap data structure](binaryHeap.md)

## Runtime

$\Theta(nlog(n))$

## Class Implementation

- Uses a **min-heap**

### Python Implementation

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

# Quicksort

![quick sort](https://ds055uzetaobb.cloudfront.net/image_optimizer/904290ba2b43687554b1d074d091367f370a0c08.gif)

- Picks a pivot and then sorts to the left of the pivot and then right.
- Comparison-based
- Uses divide-and-conquer
  - Recursive

## Runtime

Recurrence: $T(n)=2T(\frac{n}{2})+n$

Best Case: $O(nlog(n))$

Worst Case: $O(n^2)$

- Occurs when array is already sorted

Average Case: $O(nlog(n))$

## Steps

1.  If the list is empty, return the list and terminate. (base case)
2.  Choose a pivot element in the list.
3.  Take all of the elements that are less than or equal to the pivot and use quicksort on them.
4.  Take all of the elements that are greater than the pivot and use quicksort on them.
5.  Return the concatenation of the quicksorted list of elements that are less than or equal to the pivot, the pivot, and the quicksorted list of elements that are greater than the pivot.

## Pivot

- Select a random pivot.
- Select the leftmost or rightmost element as the pivot.
- Take the first, middle, and last value of the array, and choose the median of those three numbers as the pivot (Median of Three method)
- Use a median finding algorithm such as the median-of-medians algorithm.

## Partition Algorithm

`a` - array to be sorted
`l` - lower bound
`u` - upper bound

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

## Python Implementation

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

# Bin/Bucket Sort

- Not based on comparisons
- Use knowledge of the data
- Not in-place sorting
