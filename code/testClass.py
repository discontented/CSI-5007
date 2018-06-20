import numpy as np
from copy import deepcopy
import timeit as t
import bruteForce
import firstFit as ff

"""
Test(functions[], n, w)
Optional Test(function[], [1,2,3], w) // Custom array to test.

functions[] - an array of functions
n - Number of items to test up to
w - Max capacity of bins

for i in range(n):
	for function in functions:
		testFunction(a[:n], w) // test function with weight

Format
Optimality
input items | bruteForce output | heuristic output | dynamic output |

Runtime
# of input items | bruteforce time | heuristic time | dynamic time |

Method:
Add results to 2 different arrays and then iterate through.
"""

class Tester():
	def __init__(self, n, w, *funcName):
		self.n = n
		self.w = w
		
		self.functions = []
		for func in funcName:
			self.functions.append(func)

		self.items = np.random.randint(50, 100, size=n).tolist()
		
		self.results = []

	def randomizedTest(self):
		"""Adds to results array the time output of each function test.
		"""

		for func in self.functions:
			# copy list for case of destructive function
			array_cp = deepcopy(self.items)
			self.results.append(self.timer(func, array_cp, self.w))

	def timer(self, methodToRun, *args):
		"""Runs a function and computes its runtime
		
		Arguments:
			methodToRun {function} -- Function to be tested
		
		Returns:
			list -- [0] - Output of function, [1] Runtime
		"""	

		start = t.default_timer()
		results = methodToRun(*args)
		stop = t.default_timer()

		return results, stop - start

	def printTests(self):
		
		for i in range(self.n):
			self.randomizedTest()
			print("%d | %d bins in %d s | %d bins in %d s" % (len(self.items), len(self.results[0][0]), len(self.results[0][1]), len(self.results[1][0], len(self.results[1][1]))))

	def printHeader():
		print("n | Brute Force | Heuristic")
test = Tester(3, 200, bruteForce.fillBins ,ff.firstFit)
test.randomizedTest()
test.printTests()