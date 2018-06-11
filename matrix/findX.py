"""
Finds first x in an n x m matrix, H
H is sorted.
"""

def rows(matrix):
    return len(matrix)

def columns(matrix):
    return len(matrix[0])

# brute force
def findX(H, x):
    n = rows(H)
    m = columns(H)
    for i in range(n):
        for j in range(m):
            if x == H[i][j]:
                return i, j

# iterative
def iFindX(H,x):
    n = rows(H)
    m = columns(H)
    while i < n:
        while j < m:
            return i, j

def rFindX(H, x, n = None, m = None):
    if n == None:
        n = rows(H)
    if m == None:
        m = columns(H)

    if x == H[i][j]:
        return i, j
    else:
        if x < H[i][j]:
            print("[%d, %d]: %d - %d" % (i, j, H[i][j], x))
            rFindX(H, x, n-1, m-1)
        elif x > H[i][j]:
            rFindX(H, x, n+1, m+1)

def displayMatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            print("%d" % matrix[i][j], end='')
        print()

def totalItems(matrix):
    t = sum(len(field) for field in matrix)
    return t

matrix = [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

print(rFindX(matrix, 1))

