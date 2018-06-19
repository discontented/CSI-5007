#by trevor karty
import math

def indexSearch (arr):
    n = len(arr)
    if n >= 1:
        m = int(1 + math.floor(n/2))
 
        if arr[m] == 0:
            if arr[m+1] == 1:
                return m+1
            else:
                return indexSearch(arr[m+1:])

        if arr[m] == 1:
            if arr[m-1] == 0:
                return m
            else:
                return indexSearch(arr[:m])
    else:
        return -1
 
arr = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
 
result = indexSearch(arr)
 
if result != -1:
    print("Element is present at index %d" % result)
else:
    print("No index!")