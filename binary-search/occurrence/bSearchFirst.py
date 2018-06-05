def bSearchFirst(array, key, low=0, high = None):
    if high is None:
        high = len(array) - 1

    if (low > high):
        return -1

    middle = (low + high) // 2

    if(key == array[middle] and (middle == 0 or key != array[middle - 1])):
        return middle

    elif(key > array[middle]):
        return bSearchFirst(array, key, middle + 1, high)

    else:
        return bSearchFirst(array, key, low, middle - 1)