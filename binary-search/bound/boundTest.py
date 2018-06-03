import boundsearch as bs

def printArray(array):
    print("Array Elements:", end=' ')
    for el in array:
        print(el, end=' ')
    print()

def findOccurrence(array, element):
    try:
        occurrence = bs.boundSearch(array, element)
        print("%d occurs %d time(s) in %s" % (element, occurrence, array))
    except (TypeError):
        print("%d not found" % element)
    
a = [0,0,1,1]
findOccurrence(a, 0)
findOccurrence(a, 1)
findOccurrence(a, 2)