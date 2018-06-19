import numpy as np

def buildheap(n):
  return [0](n+1)

def insert(a,e):
  a[0] = a[0] + 1
  a[a[0]] = e
  heapfixup(a,a[0])

def heapfixup(a,i):
  while i > 1:
    p = i//2
    if a[p] > a[i]:
      a[p], a[i] = a[i], a[p]
      i = p
    else:
      return -1

def heapfixdown(a,i):
  while 2i <= a[0]:
    c=2*i 
    if c+1 <= a[0]:
      if a[c+1] < a[c]:
        c = c+1
    if a[i] > a[c]:
      a[i],a[c] = a[c],a[i]
      i = c
    else:
      return

def extractmin(a):
  e,a[1],a[0] = a[1], a[a[0]], a[0]-1
  heapfixdown(a,1)
  return e

def klarge(a,k):
  kheap = buildheap(k)
  for i in range(k):
    insert(kheap,a[i])
  for j in range(k,len(a)):
    if a[j] > kheap[1]:
      extractmin(kheap)
      insert(kheap,a[j])
  return kheap[1:]


array = np.random.randint(1000, size=20)
output = klarge(array, 10)

print(array)
print(output)