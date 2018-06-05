# Midterm Corrections

## Multiple Choice

### Question 1
> Consider the following code:
```py
def f(n, p):
    for i in range(n):
        for j in range(i, p):
            for k in range(n*p):
                dosomething(i, j, k) / do something(j, i, k)
```

#### Answer
C. $\sum_{i=0}^{n-1}\sum_{j=i}^{p-1}\sum_{k=0}^{np-1}2$

### Question 2
> Same code as above.  The number of calls to dosomething is in

#### Answer
E. $\Theta(n^2p^2)$

### Question 3
> Consider a runtime defined as
> $$ T(n)=\sum_{i=0}^n(2+\sum_{j=i}^{n-1}3) $$

#### Answer
E. None of the above

### Question 4
> The loop invariant of Insertion sort is **Enter the outer loop with loop index at value $k$**

#### Answer
C.  The sub-array in the first $k$ positions contains the first $k$ elements of the array in sorted order

### Question 5
> The runtime of accessing an element in a linked-list of length $n$ is in the set

#### Answer
A. $\Theta(n)$

### Question 6
Consider the following code:
```py
def f(n):
    if n <= 0:
        return 42
    elif n == 1:
        return 43
    else:
        return f(n-1) + f(n-2)
```
> Let $T(n)$ be the runtime of the function when given parameter $n$ ( a non-negative integer).  Write the definition of $T(n) as a recurrence, but do not solve it.

#### Answer
C. 
$$
T(n)=\begin{cases}
1 & n\le1 \\
T(n-1)+T(n-2) & \text{otherwise}
\end{cases}
$$

### Question 7
What is the solution to the following recurrence

$$
T(n)=\begin{cases}
1 & n\le5 \\
1 + 2T(\frac{n}{2}) & \text{otherwise}
\end{cases}
$$

#### Answer
B. $\Theta(n)$

### Question 8
What is the solution to the following recurrence

$$
T(n)=
\begin{cases}
3 & n\le5 \\
3+T(\frac{n}{4}) & \text{otherwise}
\end{cases}
$$

#### Answer
E. None of the above

### Question 9
What is the solution of the following recurrence

$$
T(n)=
\begin{cases}
1 & n\le5 \\
n+2T(\frac{n}{2}) & \text{otherwise}
\end{cases}
$$

#### Answer
C. $\Theta(nlog(n))$

### Question 10
> True or False $2n^3-n\in O(n^3)$

#### Answer
A. True

### Question 11
> True or False $2^{n-1}\in \Omega(2^n)$

#### Answer
A. True

### Question 12
> True or False $O(nlogn)\subseteq O(logn)$

#### Answer
B. False

### Question 13
> True or False $O(logn)\subseteq O(2^n)$

#### Answer
A. True

### Question 14
> True or False $O(n^{3.1}\subseteq O(n^3))$

#### Answer
B. False

### Question 15
> Bubble sort and Insertion sort have the same worst-case asymptotic runtime.

#### Answer
A. True

## Handwritten Part

### Question 16
#### Base Case
$n = 1$
$\sum_{i=1}^{1}i^2=1^2=\dfrac{1(1+1)(2(1)+1)}{6}=\frac{6}{6}=1$

#### Induction Step
Assume $\sum_{i=1}^{k}i^2=\dfrac{k(k+1)(2k+1)}{6}$ is true for all $k$, then it must be shown $\sum_{i=1}^{k+1}i^2=\dfrac{(k+1)((k+1)+1)(2(k+1)+1)}{6}$

<hr>

$$
\sum_{i=1}^{k+1}i^2=\dfrac{(k+1)((k+1)+1)(2(k+1)+1)}{6}
=\dfrac{(k^2+3k+2)(2k+3)}{6}
=\dfrac{2k^3+9k^2+13k+6}{6}
$$

<hr>

$$
\sum_{i=1}^{k+1}i^2=\sum_{i=1}^{k}i^2+\sum_{i=k+1}^{k+1}i^2=\dfrac{k(k+1)(2k+1)}{6}+(k+1)^2
$$

$$
\dfrac{(k^2+k)(2k+1)}{6}+\dfrac{6(k+1)^2}{6}=\dfrac{2k^3+k^2+2k^2+k}{6}+\dfrac{6(k^2+2k+1)}{6}
$$

$$
\dfrac{(2k^3+3k^2+k)}{6}+{6k^2+12k+6}{6}=\dfrac{2k^3+9k^2+13k+6}{6}
$$

<hr>

$$
\therefore\sum_{i=1}^{n}i^2=\dfrac{n(n+1)(2n+1)}{6},n\ge 1\blacksquare
$$

### Question 17
> Omitted

### Question 18
> In your favorite language or pseudo-code write a binary search for the first occurrence of element `e` in a sorted array `a` of integers.

```py
def bSearchFirst(array, key, low = 0, high = None):
    if high is None:
        high = len(array) - 1
    
    if (low > high):
        return -1
    
    middle = (low + high) // 2

    if (key == array[middle] and (middle == 0 or key != array[middle - 1])):
        return middle
    elif (key > array[middle]):
        return bSearchFirst(array, key, middle + 1, high)
    else:
        return bSearchFirst(array, key, low, middle - 1)
```

### Question 19
> Omitted

### Question 20

