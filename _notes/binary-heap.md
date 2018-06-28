---
layout: post
mathjax: true
---

- [Review](#review)
  - [Terms](#terms)
  - [Binary Trees](#binary-trees)
    - [Full Binary Trees](#full-binary-trees)
    - [Complete Binary Trees](#complete-binary-trees)
    - [Binary Heap Data Structure](#binary-heap-data-structure)
    - [`max-heap` property](#max-heap-property)
    - [`min-heap` property](#min-heap-property)

# Review

## Terms
**Height**
* Number of edges on the longest path from the root node to a leaf.

## Binary Trees
* Each node can have up to two children, a **left child** and a **right child**
* Each node has exactly one **parent node** (except for the root)

### Full Binary Trees
* Every leaf has the same depth and every non-leaf has two children.

### Complete Binary Trees
* At the deepest level, all the nodes are as far left as possible.
* A complete binary tree of depth $n$ has a max number of leaves of depth $2^n$

| Operation   | What it does         |
| ----------- | -------------------- |
| $d$         | depth                |
| $2^d$       | Max Number of Leaves |
| $2^{d+1}-1$ | Max Number of Nodes  |

### Binary Heap Data Structure
* Uses an array object.
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

$A[parent(i)] \ge A[i]$

* A node cannot have a greater value than its parent.
* The largest element is the root.
* The minimum elements are the leaves.

### `min-heap` property

$A[parent(i)] \le A[i]$

* A parent node cannot have a greater value than its children.
* The minimum element is the root.
* The max elements are the leaves.


