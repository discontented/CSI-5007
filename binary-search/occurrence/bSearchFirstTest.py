import bSearchFirst as bsf

def printArray(array):
    print("# ", end=' ')
    for el in array:
        print(el, end=' ')
    print(": ", end=' ')

def findFirst(array, element):
    printArray(array)
    try:
        result = bsf.bSearchFirst(array, element)
        if(result != -1):
            print("First occurence of %d is at %d" % (element, result))
        elif(result == -1):
            print("%d not found" % element)
    except TypeError as e:
        print(e)

def testCases(n):
    """
    Tests empty array, array of single element, array of all same elements, array of all different elements
    n is max number of array to test.
    """
    # empty test case
    a = []
    findFirst(a, 0)

    # single element
    a = [0]
    findFirst(a, 0)

    # 3 different elements
    a = [0] * 3
    for i in range(3):
        a[i] = i
    for i in range(3):
        findFirst(a, i)

    # all same elements
    a = [0] * n
    findFirst(a, 0)

    # 1/3 elements the same. 2/3 another integer
    third = n // 3
    a[:third] = [0] * third
    a[third:] = [1] * (2 * (third))
    findFirst(a, 0)
    findFirst(a, 1)
    
testCases(6)