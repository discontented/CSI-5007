def bSearchFirst(a, e, l=0, h=(len(a)-1):
        m = len(a) // 2
        if(e == a[m] & l == h):
            return m
        elif(e == a[m]):
            bSearchFirst(a, e, m+1, h)
        else:
            bSearchFirst(a, e, l, m-1)

# Test


