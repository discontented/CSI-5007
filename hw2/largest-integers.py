"""
Find the largest integers in an array.
Parameters:
    a - array of integers
    k - number of largest integers to find
Precondition: k <= len(a)
Return: an array containing the k largest elements of array a
Running Time: O(nlog(k))
"""
def lgInts(a, k):
    if(k <= len(a)):