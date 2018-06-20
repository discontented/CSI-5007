from Bin import Bin
import timer as t

def recursiveForce(a, w):
    a.sort(reverse = True)

    bins = []

    for bin in bins:
        for item in a:
            if(item <= bin.capacity):
                optimizeCapacity(bin, item, w)        
    else:
        bins.append(Bin(w))
    return bins

def optimizeCapacity(Bin, item, w):
    if item == w:
        Bin.insert(item)
    else:
        optimizeCapacity(Bin, item, w-1)
