import bsearch as bs

# Test empty array
try:
    empa = [0,1,1]
    bs.bsearch(empa, 0)
except Exception as e:
    print(e)

