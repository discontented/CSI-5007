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
1) Insert k elements into the min-heap
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
    if(k <= len(a)):

"""
Class min-heap
Attributes:
    n - size of heap
methods:
    init(n)
        Creates array within object containing all 0s at length n
    peek()
"""
class MinHeap(object):
    def __init__(self, n):
        self.a = [0]*(n)
        self.size = n

    # Inserts into the last available spot and then checks and fixes heap structure
    def insert(e):
        self.size += 1
        self.a[self.size] = e
        self.heapfixup()
    
    def extractsmallest(a):
        e = self.a[0]
        self.a[0] = self.a[self.size]
        self.size =- 1
        heapfixdown()
        return e
    
    def heapfixup(i):
        while i > 1:
            p = i // 2

            if self.a[p] > self.a[i]:
                self.a[p], self.a[i] = self.a[i], self.a[p]
                i = p
            else:
                return
    
    def heapfixdown(i):
        while (2 * i) <= self.size:
            c = 2 * i
            if (c + 1) <= self.size:
                if a[c] < a[c - 1]:
                    c += 1
                if a[i] > a[c - 1]:
                    a[i], a[c - 1] = a[c - 1], a[i]
                    i = c - 1
                else:
                    return
    


    