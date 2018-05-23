

# Sorting
# Bubble Sort

Compares each pair of elements in an array and swaps them if they are out of order until the entire array is sorted.

### Running Time
$\Theta(n^2)$

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

Best Case:

$$
\Theta(n)
$$

Worst Case: $$\Theta(n^2)$$

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

# Searching
## Binary Search

### Python Implementation
* `array` must be sorted.
* `low` and `high` are indexes not values.
* `key` is the value being searched for.

```py
def bsearch(array, key):
    low, high = 0, len(array)-1
    while low <= high:
        middle = math.floor((low + high) / 2)
        if array[middle] == key:
            return middle
        if array[middle] < key:
            low = middle + 1
        else:
            high = middle - 1
    return -1
```

### Loop Invariant
* If the `key` is in the array, it is in `a[1,...,high]`
* The midpoint is determined by dividing the array in half.
    * `middle = math.floor((low + high) / 2)`
* The element `array[middle]` at the midpoint is compared with the `key`
    * If it matches, the index of the middle is returned.
* If the `key` is larger than `array[middle]`, then the `key` must be in the lower half.
    * `high` is set then to one less than the middle index.
    * `high = middle - 1`
* If the `key` is smaller than `array[middle]`, then the `key` must be in the upper half.
    * `low` is set then to one above the middle index.
    * `low = middle + 1`

### Running Time
$\Theta(lgn)$

# Resources
[Brilliant Sorting Algorithms](https://brilliant.org/wiki/sorting-algorithms/)

[Big-O Cheatsheet](http://bigocheatsheet.com/)