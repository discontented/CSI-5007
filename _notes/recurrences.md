---
layout: post
mathjax: true
---

# Recurrence
* A **recurrence** is an equation or inequality that describes a function in termsof its value on smaller inputs.

## Recurrence Problem Forms
* Subproblems are divided by a constant fraction.
$$T(n)=T(\frac{n}{2}+\Theta(n))$$

* Subproblems are not necessarilly constrained to being a constant fraction of the original problem size.
$$T(n)=T(n-1)+\Theta(1)$$

## Solving a Recurrence
