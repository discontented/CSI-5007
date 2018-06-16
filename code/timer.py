"""
Time tests
"""
import timeit as t

def timer(methodToRun, *args):
    start = t.default_timer()
    results = methodToRun(*args)
    stop = t.default_timer()
    return results, stop - start