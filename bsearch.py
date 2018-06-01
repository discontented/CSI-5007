def bsearch(a, e):
    m = len(a) // 2
    if(e == a[m]):
        print("middle: %d" % m)
        return m
    elif(e < a[m]):
        print(m)
        bsearch(a[:m], e)
    else:
        print(m)
        bsearch(a[m:], e)
