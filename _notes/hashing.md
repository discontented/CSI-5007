---
layout: post
mathjax: true
---

- [Direct Address Table](#direct-address-table)
- [Hash Table](#hash-table)
- [Hash Function](#hash-function)
	- [Notation](#notation)
	- [Properties](#properties)
	- [Process](#process)
- [Collisions](#collisions)
	- [Chaining](#chaining)
- [Load Factor](#load-factor)
- [Runtime](#runtime)
- [Storage](#storage)

Symbol|Meaning
---|---
$h$|Hash Function
$h(k)$|Hash Value (slot)
$U$|Universe of Keys
$k$|Key
$K$|Set of keys
$T$|Table (Hash or Direct Address)
$m$|Size of hash table

# Direct Address Table
* An array $T[0,...,m-1]$ where each slot corresponds to a key in the universe $U=\{0,1,...,m-1\}$
* An element with key $k$ is stored in slot $k$

# Hash Table
* An element with key$k$ is stored in slot $h(k)$
	* $h(k)$ is the [hash function](#hash-function)
* Any data type can be inserted in a dynamic language.
* No ordering
	* Slots in hash table are assigned by hash function, which varies by the input.

# Hash Function
* A mathematical function that maps keys to integers.
	* Keys can be strings, objects, etc.

## Notation
$$h: \{1, 2, ...,\lvert U\rvert\}\rightarrow\{0,...,m-1\}$$

## Properties

* Return value of a hash function is the index of an array of pointers.
	* The item associated with a key is referenced by the pointer at the index.
* Size of the hashtable is typically much less than $\lvert{U}\rvert$
* Since the hash function will generate a large integer, which would require a large array to map the index accurately, the function must reduce the number to an integer between 0 and $m-1$
* Use modulus to take the remainder of $h(S) mod\ m$ to assign and index.
* The ideal table size of $m$ is a large prime not close to $2^{i-1}$
* Must be deterministic
	* An input $k$ must always produce the same output $h(k)$

## Process	
key $k$ (a string) -> hash function -> index integer -> pointer located at index -> object in memory the pointer pointed to

# Collisions
* Two distinct keys that hash to the same value.
* By the pigeonhole principle, because $\lvert{U}\rvert >m$, there must be at least two keys that have the same hash value.

## Chaining
* All elements assigned to the same slot are placed in the same linked list.
	* If $h(k)\equiv h(j)$ then they would be placed in the same linked list with the head being whichever element was placed first.

# Load Factor
* Average number of elements stored in a chain.
* Given a hash table $T$ with $m$ slots that stores $n$ elements, the load factor of $T$ is $\frac{n}{m}$

# Runtime
* Average runtime for searching for an element is $O(1)$
* Average case of hashing depends on how well the hash function distributes the set of keys to be stored among the $m$ slots.
	* **Simple Uniform Hashing**
		* Assumption is that any given element is equally likely to hash.

# Storage
* $\Theta(\lvert{K}\rvert)$