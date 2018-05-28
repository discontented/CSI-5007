---
mathjax: true
layout: post
---

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
