
def newheap(n):
    return [0]*(n+1)

def insert(a, e):
    a[0] = a[0] + 1
    a[a[0]] = e
    heapfixup(a,a[0])

def extractsmallest(a):
    e = a[1]
    a[1] = a[a[0]]
    a[0] = a[0] - 1
    heapfixdown(a, 1)
    return e

def heapfixup(a,i):
    while i > 1:
        p = i // 2
        if a[p] > a[i]:
            a[p], a[i] = a[i], a[p]
            i = p
        else:
            return

def heapfixdown(a, i):
    while (2 * i) <= a[0]:
        c = 2 * i
        if (c + 1) <= a[0]:
            if a[c + 1] < a[c]:
                c += 1
            if a[i] > a[c]:
                a[i], a[c] = a[c], a[i]
                i = c
            else:
                return

"""
Find the largest integers in an array.
Parameters:
    a - array of integers
    k - number of largest integers to find
Precondition: k <= len(a)
Return: an array containing the k largest elements of array a
Running Time: O(nlog(k))

Method:
min-heap
Insert k elements into the min-heap
    For each element of the array
        if element is < min element of min-heap
            toss the element
        else if element > min element of min-heap
            pop min element from min-heap
            insert element from array into min-heap
    return all elements of the min-heap

The min heap will contain k elements, all of which will be the largest.
"""

def lgInts(a, k):
    # Create the min heap with k 0 elements
    n = len(a)
    minheap = newheap(k)

    if k < n:
        # create min heap with the first k elements of a
        for i in range(k):
            insert(minheap, a[i])
        
        for i in range(k+1, n):
            if a[i] > minheap[1]:
                insert(minheap, a[i])
                extractsmallest(minheap)
        return minheap
    else:
        return "k is larger than array"