---
layout: post
mathjax: true
---

- [Hash Function](#hash-function)
	- [Actual Hash Function](#actual-hash-function)
	- [Collisions](#collisions)
		- [Chaining](#chaining)

# Hash Function
* A mathematical function that maps keys to integers.
* Return value of a hash function is the index of an array of pointers.
	* The item associated with a key is referenced by the pointer at the index.
		* Thinking of it as a pointer makes it easier later for Chaining Resolution.
		* If it makes it easier, think of the value array as the items themselves, or objects.
	* The process:
		* key (a string) -> hash function -> index integer -> pointer located at index -> object in memory the pointer pointed to
* $\alpha$
	* The size of an alphabet which a string $S$ is written.
* `char(c)`
	* A function that maps each symbol of the alphabet, $a$, to a unique integer from 0 to $a-1$

## Actual Hash Function
$H(S)=\sum_{i=0}^{|S|-1}\alpha^{|S|-(i+1)}\times char(s_i)$

* $m$ - Number of slots in the hash table.
* Since the hash function will generate a large integer, which would require a large array to map the index accurately, the function must reduce the number to an integer between 0 and $m-1$
	* Use modulus to take the remainder of $H(S) mod m$ to assign and index.
	* The ideal table size of $m$ is a large prime not close to $2^{i}-1

## Collisions
* Two distinct keys that hash to the same value.

### Chaining

