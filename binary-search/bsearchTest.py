import bsearch as bs

a = [0, 1, 2]

def printArray(array):
    print("Array Elements:", end=' ')
    for el in array:
        print(el, end=' ')
    print()

def findInArray(array, element):
    try:
        print("Index of %d is %d" % (element, bs.bsearch(array, element)))
    except (TypeError):
        print("%d not found" % element)

printArray(a)
findInArray(a, 0)
findInArray(a, 1)
findInArray(a, 2)

