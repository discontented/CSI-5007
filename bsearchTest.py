import bsearch as bs

a = [0, 1, 2]

def printArray(array):
    for el in array:
        print(el, end=' ')
    print()

printArray(a)

try:
    print("Answer 0: ", end='')
    print(bs.bsearch(a, 0))
except Exception as e:
    print(e)

try:
    print("Answer 1: ", end='')
    print(bs.bsearch(a, 1))
except Exception as e:
    print(e)

try:
    print("Answer 2: ", end='')
    print(bs.bsearch(a, 2))
except Exception as e:
    print(e)

