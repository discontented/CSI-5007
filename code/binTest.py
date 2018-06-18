import numpy as np

# local modules
import bruteForce
import firstFit as ff
import timer as t

def simpleTest(a, w):
    print("Brute Force:")
    print(t.timer(bruteForce.fillBins, a, w))
    print("Heuristic:")
    ff.printBins(ff.firstFit(a, w))


def randomizedTest(w):
    """Generates random array for you.
    
    Arguments:
        w {int} -- Max weight of bin.
    """
    array = np.random.randint(50, 100, size=20).tolist()
    print(str(array) + "\n")
    print(t.timer(bruteForce.fillBins, array, w))
    array = np.random.randint(50, 100, size=20).tolist()
    print(str(array) + "\n")
    ff.printBins(ff.firstFit(array, w))

# a = [1,2,3]
# simpleTest(a, 4)
randomizedTest(200)