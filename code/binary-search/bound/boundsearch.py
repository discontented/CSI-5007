"""
Counting occurrences of a character in a presorted array.
All searches are unsuccessful since there is no equality test.
Whenever an identical array element is found, the search proceeds to the right half (else statement)
After the recursion terminates, the search repeats for the left boundary.
Counts in O(lgn)
"""

def boundSearch(array, key, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if(low > high):
        # returns low index on each unsuccessful search
        return low

    middle = (low + high) // 2

    if(array[middle] > key):
         return boundSearch(array, key, low, middle-1)     
    else:
         return boundSearch(array, key, middle+1, high)
