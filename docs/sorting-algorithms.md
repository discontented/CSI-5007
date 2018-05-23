## Bubble Sort

Compares each pair of elements in an array and swaps them if they are out of order until the entire array is sorted.

### Running Time
$\Theta(n^2)$

### Loop Invariant
* Enter the for loop on `i` with value `j`, array ``a[0...k-1]` contains the `k` smallest elements of the set in sorted order.

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

### Running Time
$\Theta(nlgn)$



# Resources
[Brilliant Sorting Algorithms](https://brilliant.org/wiki/sorting-algorithms/)

[Big-O Cheatsheet](http://bigocheatsheet.com/)