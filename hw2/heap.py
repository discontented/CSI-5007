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
    def insert(self, e):
        self.size += 1
        self.a[self.size] = e
        self.heapfixup()
    
    def extractsmallest(self, a):
        e = self.a[0]
        self.a[0] = self.a[self.size]
        self.size =- 1
        self.heapfixdown()
        return e
    
    def heapfixup(self, i):
        while i > 1:
            p = i // 2

            if self.a[p] > self.a[i]:
                self.a[p], self.a[i] = self.a[i], self.a[p]
                i = p
            else:
                return
    
    def heapfixdown(self, i):
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
    def peek():
        return a[0]
    
    def pop():
        