---
layout: post
mathjax: true
---

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

#### Testing
```py
def testCases(n):
    # empty test case
    a = []
    findFirst(a, 0)

    # single element
    a = [0]
    findFirst(a, 0)

    # 3 different elements
    a = [0] * 3
    for i in range(3):
        a[i] = i
    for i in range(3):
        findFirst(a, i)

    # all same elements
    a = [0] * n
    findFirst(a, 0)

    # 1/3 elements the same. 2/3 another integer
    third = n // 3
    a[:third] = [0] * third
    a[third:] = [1] * (2 * (third))
    findFirst(a, 0)
    findFirst(a, 1)
```

##### Output

```sh
#  :  0 not found
#  0 :  First occurence of 0 is at 0
#  0 1 2 :  First occurence of 0 is at 0
#  0 1 2 :  First occurence of 1 is at 1
#  0 1 2 :  First occurence of 2 is at 2
#  0 0 0 0 0 0 :  First occurence of 0 is at 0
#  0 0 1 1 1 1 :  First occurence of 0 is at 0
#  0 0 1 1 1 1 :  First occurence of 1 is at 2
```

### Question 19
> Omitted

### Question 20
> Write a function (in pseudo-code or your favority language) which, given an array of numbers as input, returns the smallest and largest element of the array.  Argue its correctness and runtime.  You are **not** allowed to call any external routine except **sort**.

```py
def findHighLow(a):
    n = len(a)
    if(n > 0):
        low = a[0]
        high = a[0]
        for i in range(0, len(a)):
            if(a[i] < low):
                low = a[i]
            if(a[i] > high):
                high = a[i]
        return high, low
    else:
        return -1
```

#### Testing
```py
def testCases(n):
    # empty test case
    a = []
    find(a)

    # single element
    a = [0]
    find(a)

    # 3 different elements
    a = [0] * 3
    for i in range(3):
        a[i] = i
    for i in range(3):
        find(a)

    # all same elements
    a = [0] * n
    find(a)

    # 1/3 elements the same. 2/3 another integer
    third = n // 3
    a[:third] = [0] * third
    a[third:] = [1] * (2 * (third))
    find(a)
```

```sh
#  :  empty array
#  0 :  largest = 0, smallest = 0
#  0 1 2 :  largest = 2, smallest = 0
#  0 1 2 :  largest = 2, smallest = 0
#  0 1 2 :  largest = 2, smallest = 0
#  0 0 0 0 0 0 :  largest = 0, smallest = 0
#  0 0 1 1 1 1 :  largest = 1, smallest = 0
```

#### Correctness
* Loop Invariant
    * The variables `high` and `low` store the highest and lowest values, respectively, in the array from `a[0]` to `a[i]`
    * Once `i` increments, the values of `low` and `high` are compared with the current elements.
        * Each variable is replaced if a lower or higher variable is found.
    * After each exit of the loop, `low` and `high` store the lowest and highest values from `a[0]` to `a[i]`.

#### Runtime Analysis

$$
T(n) = 2\sum_{i=0}^{n}1 = 2(n-0+1)= 2n + 2
$$

$$
T(n) = \Theta(n)
$$
