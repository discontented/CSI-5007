# Memoized DP Algorithm
Recursion + memoization
* Remember solutions and reuse solutions to subproblems that help solve the problem.
    * "Memo" comes from the idea of using a scratch pad or memo to log results (as you would in calculating an equation without memory) and using those answers to find the final answer.
## Runtime
    * time = # of subproblems * the amount of time you spend per subproblem

## Fibonacci
```
memo = {}
fib(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        f = 1
    else:
        f = fib(n-1)+fib(n-2)
        memo[n]=f
    return f
```

1. Create empty `memo` dictionary
2. Check if `fib(n)` is already in the dictionary (it has already been computed)
    1. If not, comput the fib number
3. Store `fib(n)` into `memo[n]` and return `f`

### Runtime Analysis
* Only making recursive calls the first time `fib(k)` it's called.
    * The memoized calls are constant time ($\Theta(1)$)
* The number of non-memoized calls is $n$ since `fib(k)` is done the first time and only done once for each number $<= n$http://josh-corneille.com/CSI-5007/

Runtime = $\Theta(n)$

## Bottom-up DP Algorithm
* A recursive algorithm starts at the top and works its way down.

### Pseudocode
* Uses a hash table for look up instead of function calls

```py
fib = {}
for k in range(1, n+1):
    if k <= 2:
        f = 1
    else:
        f = fib[k-1] + fib[k-2]
    fib[k] = f
return fib[n]
```
* Answers to subproblems are stored in a dictionary of $1...n$
* The only answer cared about is `fib[n]` which is returned.

