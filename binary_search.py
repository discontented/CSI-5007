def binary_search(array, key, low, high):
    if(low > high):
        return -1
    middle = (low + high)/2
    if(array[middle] == key):
        return middle
    if(array[middle] > key):
        return binary_search(array, key, low, middle-1)
    else:
        return binary_search(array, key, middle+1, high)
