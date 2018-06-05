# Finds highest and lowest values in function.
def findHighLow(a):
    n = len(a)
    if(n > 0):
        low = a[0]
        high = a[0]
        for i in range(0, len(a)):
            if(a[i] < low):
                low = a[i]
            if(a[i] > high):
                high = a[i]
        return high, low
    else:
        return -1

def printArray(array):
    print("Array Elements:", end=' ')
    for el in array:
        print(el, end=' ')
    print()

def find(array):
    #array must be sorted
    printArray(array)
    try:
        if(findHighLow(array) != -1):
            high, low = findHighLow(array)
            print("The largest value is %d" % high)
            print("The smallest value is %d" % low)
        elif(findHighLow(array) == -1):
            print("empty array")
    except Exception as e:
        print(e)

a = []
find(a)
a = [0,1]
find(a)
a = [0,0,0]
find(a)
a = [0,1,2]
find(a)