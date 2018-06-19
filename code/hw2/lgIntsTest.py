import largestIntegers as LI
"""
Tests for largest integers
"""
def printArray(array):
    print("# ", end=' ')
    for el in array:
        print(el, end=' ')
    print(": ", end=' ')

def find(a, k):
    largest = LI.lgInts(a, k)
    for i in (len(largest)):
        print("%d " % largest[i])



find(genSeqArray(5), 2)