import search as fhl

def printArray(array):
    print("# ", end=' ')
    for el in array:
        print(el, end=' ')
    print(": ", end=' ')

def find(array):
    #array must be sorted
    printArray(array)
    try:
        if(fhl.findHighLow(array) != -1):
            high, low = fhl.findHighLow(array)
            print("largest = %d, smallest = %d" % (high, low))
        elif(fhl.findHighLow(array) == -1):
            print("empty array")
    except Exception as e:
        print(e)

def testCases(n):
    """
    Tests empty array, array of single element, array of all same elements, array of all different elements
    n is max number of array to test.
    """
    # empty test case
    a = []
    find(a)

    # single element
    a = [0]
    find(a)

    # 3 different elements
    a = [0] * 3
    for i in range(3):
        a[i] = i
    for i in range(3):
        find(a)

    # all same elements
    a = [0] * n
    find(a)

    # 1/3 elements the same. 2/3 another integer
    third = n // 3
    a[:third] = [0] * third
    a[third:] = [1] * (2 * (third))
    find(a)
    find(a)

testCases(6)