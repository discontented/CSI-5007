import numpy as np

def knapSack(W, wt):
  n = len(wt)
  minW=min(wt)
  s = [[]]*(W+1)
  K = [[0 for x in range((W+1))] for x in range(n+1)]

  for i in range(n+1):
    for w in range(W+1):
      if wt[i-1] <= w:
          if wt[i-1] + K[i-1][w-wt[i-1]] >  K[i-1][w]:
              K[i][w] = wt[i-1] + K[i-1][w-wt[i-1]]
              s[w]=s[w-wt[i-1]] + [i]
          else:
            K[i][w] = K[i-1][w]
      else:
          K[i][w] = K[i-1][w]

  return list(set(s[len(s)-1]))

def ksBin(a, W):
  bins = [[] for x in range(len(a))]
  j=0
  binCount = 0

  while len(a) > 0: 
      bindices = knapSack(W, a)
      ##WEIRD THING GOING ON HERE... INDEX RETURN IN KNAPSACK FUNCTION PLACES 0TH ELEMENT AT END OF LIST... NEXT LINE IS SLOPPY FIX
      a.insert(0, a.pop())
      n = len(bindices)

      ##HUGE WASTE OF TIME CALCULATING SUM EVERY TIME
      if(sum(a) < W):
        bins[j] = a.copy()
        a.clear()
      else:
        for i in range(n-1,-1,-1):
          ##WISH I DIDNT HAVE TO DO THIS, DON'T KNOW WHY WE GET INDEXES GREATER THAN ARRAY LENGTH
          if bindices[i] >= len(a):
            bindices.pop(i)
          else:
            bins[j].append(a.pop(bindices[i]))
            binCount = binCount+1

      j = j+1

  rBins = []
  for bin in bins:
    if len(bin) != 0:
      rBins.append(bin)
  
  return rBins
