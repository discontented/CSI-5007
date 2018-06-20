import numpy as np
from copy import deepcopy

# local modules
import bruteForce
import firstFit as ff
import timer as t

def tester(funcName, array, w):
    """Array of time test results.
    results[0] - Return of function
    results[1] - Runtime of function
    
    Arguments:
        funcName {function} -- function to be tested.
        array {list} -- items to pass to the function to test.
        w {int} -- max weight
    
    Returns:
        [type] -- [description]
    """

    return t.timer(funcName, array, w)

def randomizedTest(n, w, *funcName):
    array = np.random.randint(50, 100, size= n).tolist()
    # store base array for future comparison
    results = [array]

    for func in funcName:
        # copy array for case of destructive function
        array_cp = deepcopy(array)
        results.append(tester(func, array_cp, w))

    return results

def printTest(n, w):
    results = randomizedTest(n, w, bruteForce.fillBins, ff.firstFit)

    array = results[0]
    brute = results[1]
    heuristic = results[2]

    print("%d | %d bins in %f s| %d bins in %f s" % (len(array), len(brute[0]), brute[1], len(heuristic[0]), heuristic[1]))

def printHeader():
    print("n | Brute Force | Heuristic")

def runTest(n, w, inc=None):
    printHeader()
    if inc:
        for i in range(0, n+1, inc):
                printTest(i, w)
    else:
        for i in range(n+1):
            printTest(i, w)

runTest(25, 200, 5)
