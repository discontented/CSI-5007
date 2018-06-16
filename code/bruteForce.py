from itertools import combinations
import numpy as np
import timer as t

def optimalSubset(a, w):
    bestSet = []
    bestSum = 0

    for i in range(len(a)):
        # Generate all subsets and store in combos
        combos = list(combinations(a, i))

        # Search through all the possible subsets for the set equal to, or closest to, W
        for j in range(len(combos)):
            tempSum = sum(combos[j])
            # If we've found a subset equal to weight W, break loop and return subset
            if tempSum == w:
                bestSet = combos[j]
                break
            # If the current subset is closer to W without exceeding, it is the new best option
            elif tempSum < w and tempSum > bestSum:
                bestSum = tempSum
                bestSet = combos[j]
    
    # Best set has been found, now remove those elements by value from the input array
    for k in range(len(bestSet)):
        a.remove(bestSet[k])
    # Return the set
    return bestSet

# Fill bins until the array is empty
def fillBins(a, w):
    bins = []
    while len(a)-1 > 0:
        newBin = optimalSubset(a, w)
        print(newBin)
        bins.append(newBin)