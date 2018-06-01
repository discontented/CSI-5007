def bsearch(a, e):
    m = len(a) // 2
    if(e == a[m]):
        return m
    elif(e < a[m]):
        bsearch(a[:m], e)
    else:
        bsearch(a[m:], e)
