def f(p, t):
    m = len(p)
    n = len(t)

    for i in range(0, n-m):
        j = 0
        while j < m and t[i+j] ==  p[j]:
            # print(t[i+j], p[j])
            j += 1
        if m == j:
            return i
    return -1

ar1 = [0, 1, 2]
ar2 = [0, 1, 2, 3]

print(f(ar1, ar2))