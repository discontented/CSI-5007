import timer as t
import bruteForce
from firstFit import firstFit
import numpy as np

def simpleTest(a, w):
    print("Brute Force:")
    print(t.timer(bruteForce.fillBins, a, w))
    print("Heuristic:")
    print(t.timer(firstFit, a, w))

def randomizedTest(a, w):
    array = np.random.randint(50, 100, size=20).tolist()
    print(str(array) + "\n")
    print(t.timer(bruteForce.fillBins, a, w))
    print(t.timer(firstFit, a, w))

a = [1, 2, 3]
simpleTest(a, 4)
randomizedTest(a, 4)