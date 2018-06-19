def newheap(n):
  return [0]*(n+1)

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
  while 2*i <= a[0]:
    c=2*i 
    if c+1 <= a[0]:
      if a[c+1] < a[c]:
        c = c+1
    if a[i] > a[c]:
      a[i],a[c] = a[c],a[i]
      i = c
    else:
      return

def extractsmallest(a):
  e,a[1],a[0] = a[1], a[a[0]], a[0]-1
  heapfixdown(a,1)
  return e

def lgInts(a, k):
    # Create the min heap with k 0 elements
    n = len(a)
    minheap = newheap(k)

    # create min heap with the first k elements of a
    for i in range(k):
        insert(minheap, a[i])

    for j in range(k, n):
        if a[j] > minheap[1]:
            extractsmallest(minheap)
            insert(minheap, a[j])

    return minheap[1:]


array = [0, 1, 3, 6, 2, 9, 8]
print(lgInts(array, 3))
