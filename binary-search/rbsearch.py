def rbsearch(array, key, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if(low > high):
        return -1

    middle = (low + high) // 2

    if(array[middle] == key):
        return middle

    if(array[middle] > key):
        return rbsearch(array, key, low, middle-1)
        
    else:
        return rbsearch(array, key, middle+1, high)
