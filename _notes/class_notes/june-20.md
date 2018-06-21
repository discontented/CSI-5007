---
layout: post
mathjax: true
---

$m(u)$ - Optimal number of containers for $u$
* $u$ is a vector of size $u$
* $u_1$ is the number of elements of $w_1$, etc.

$$
m(u)=\begin{cases}
0 & u=[0,...,0] \\
1 & u\in{V} \\
1+min\{1 + m(u-a) | a\in{V}\}
\end{cases}
$$

The optimal solution is 1 if it fits in the container
* If the input is 0, you have 0 containers

* Each $V$ fits in a container
    * $min$ means optimal solution
    * $min(m)$ is the minimum number of bins over all configurations.
* If it doesn't fit in a container, 
* $a\in{V}$ is every possible configuration you can extract.