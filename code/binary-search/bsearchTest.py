import rbsearchShort as bs

def printArray(array):
    print("Array Elements:", end=' ')
    for el in array:
        print(el, end=' ')
    print()

def findInArray(array, element):
    try:
        print("Index of %d is %d" % (element, bs.rbsearch(array, element)))
    except (TypeError):
        print("%d not found" % element)

a = [0, 1, 2]

printArray(a)
findInArray(a, 0)
findInArray(a, 1)
findInArray(a, 2)