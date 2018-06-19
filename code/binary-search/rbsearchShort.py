# not accurate as array is chopped in half with each call

import math

def rbsearch(a, e):
    m = math.floor(len(a) / 2)
    if a[m] == e:
        return m
    if a[m] < e:
        return rbsearch(a[m:], e)
    else:
        return rbsearch(a[:m], e)

            
