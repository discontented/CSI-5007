from Bin import Bin

def firstFit(a, w):
    """First-Fit Decreasing Implementation
    1. Sorts objects from max to min
    2. Insert each object into first bin which has room for it.
        a. If no room in bin, create a new one.
    Arguments:
        a {array[int]} -- Element values are the item's weight.
        w {int} -- The max weight of all bins.
    """

    a.sort(reverse = True)

    # Contains all bins.  Initializes first empty bin in first position.
    bins = [Bin(w)]

    # iterate through all items in original array
    for i in range(len(a)):
        # Iterate through all bins
        for j in range(len(bins)):
            if (a[i] <= bins[j].capacity()):
                bins[j].insert(a[i])
                break
            else:
                bins.append(Bin(w, a[i]))
                break
    
    return bins

def printBins(bins):
    for bin in bins:
        print('Weight: %d' % bin.weight)
        print('Contents: %s' % bin.contents)

printBins(firstFit([1,2,3,4,1,2], 4))