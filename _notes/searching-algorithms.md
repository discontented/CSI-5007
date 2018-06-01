---
layout: post
mathjax: true
---

## Binary Search

### Iterative Implementation

* `array` must be sorted.
* `low` and `high` are indices not values.
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


### Explanation
*from slides*
At the start the interval `[l,h]` encompasses the whole array and it is reduced at every step. Therefore, the algorithm terminates.

#### Loop Invariant
If element `e` is in the array, it is in `a[l,..,h]`. The algorithm considers the mid-point and compares its element with the target `e`. If the element is too large, the target must be in the lower half and reduces `h`. If the element is too small, the element must be in the upper half and increases `l`. It stops when it finds `e` or when the array is exhausted.

### Loop Invariant
*interpreted explanation*
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

### Recursive Implementation

```py
def rbsearch(a, e, l, h):
    if l > h:
        return -1
    else:
        m = (l+h)//2
        if a[m] == e:
            return m
        if a[m] < e:
            return rbsearch(a, e, m+1, h)
        else:
            return rbsearch(a, e, l, m-1)
```


### Running Time

$\Theta(lgn)$
