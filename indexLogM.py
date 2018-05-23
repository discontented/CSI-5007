"""
def indexLogM(symbolArray, start, end):
    if(symbolArray[start] == 0 & symbolArray[end] == 0):
        return indexLogM(symbolArray, end, min(2*end, symbolArray.length))
    if (symbolArray[start] == 0 & symbolArray[end] == 1):
        return
"""
def indexLogM(array, start, end):
    if(start <= end):
        # find middle index of array
        middle = (start + end) // 2
        print(middle)
        if (array[middle] == 1) & (start == end):
            # return position of first 1 encountered
            return middle
        elif array[middle] == 0:
            # encountered a zero in the middle so a 1 must be after.
            # start recursion at next possible middle position to end.
            indexLogM(array, middle + 1, end)
        else:
            indexLogM(array, start, middle)

# Test Code
zeroOne = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
length = len(zeroOne)
print(indexLogM(zeroOne, 1, 12))