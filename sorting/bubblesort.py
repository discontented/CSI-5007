def bubble(A):
    
    for i in range(len(A)):
        for j in range(i, len(A)):
            # swap elements
            A[i], A[j] = A[j],A[i]
    return A
