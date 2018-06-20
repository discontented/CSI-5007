from Bin import Bin

def firstFit(a, w):
    """First-Fit Decreasing Implementation
    1. Sorts objects from max to min
    2. Insert each object into first bin which has room for it.
        a. If no room in bin, create a new one.
    Arguments:
        a {list[int]} -- Element values are the item's weight.
        w {int} -- The max weight of all bins.
    """

    a.sort(reverse = True)

    # Contains all bins.  Initializes empty bin of bins.
    bins = []

    # iterate through all items in original array
    for item in a:
        # Iterate through all bins. Breaks when item is inserted.
        for bin in bins:
            if (item <= bin.capacity()):
                bin.insert(item)
                break
        # Iterates through all bins and cannot find a fit.  Create new bin.
        else:
            bins.append(Bin(w, item))
    
    return bins

def printBins(bins):
    for bin in bins:
        print('Weight: %d' % bin.weight)
        print('Contents: %s' % bin.contents)


