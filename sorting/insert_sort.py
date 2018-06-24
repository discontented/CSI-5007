def insertSort(A):
    """Sorts the array A by insertion sort.
    
    Arguments:
        A {list} -- List to be sorted
    """
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

a = [3,2,1]
insertSort(a)
print(a)
    