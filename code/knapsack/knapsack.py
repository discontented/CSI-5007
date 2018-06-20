def knapSack(W, wt, n):
    """[summary]
    
    Arguments:
        W {int} -- Capacity of knapsack
        wt {list} -- Weight of n items
        n {list} -- Items to be inserted
    
    Returns:
        [type] -- [description]
    """

    K = [[0 for x in range(W+1)] for x in range(n+1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(wt[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]