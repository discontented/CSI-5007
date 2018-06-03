import bSearchFirst as bsf

def printArray(array):
    print("Array Elements:", end=' ')
    for el in array:
        print(el, end=' ')
    print()

def findFirst(array, element):
    try:
        print("Index of %d is %d" % (element, bsf.bSearchFirst(array, element)))
    except (TypeError):
        print("%d not found" % element)
    
a = [0,0,1,1]
findFirst(a, 0)
findFirst(a, 1)
findFirst(a, 2)