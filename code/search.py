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