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
	- [Open Addressing](#open-addressing)
		- [Negatives of Open Addressing](#negatives-of-open-addressing)
		- [Probing](#probing)
			- [Linear Probing](#linear-probing)
			- [Quadratic Probing](#quadratic-probing)
			- [Double Hashing](#double-hashing)
- [Load Factor](#load-factor)
- [Good Hash](#good-hash)
	- [Division Method](#division-method)
		- [Values of $m$](#values-of-m)
	- [Multiplication Method](#multiplication-method)
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
$m$|Size of hash table (number of slots)

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

## Open Addressing
* All elements are stored within the hash table itself.
	* No linked lists via chaining.
	* Each table entry either contains an element or `null`
* Load factor $\alpha$ can never equal 1
* Hash table is **probed** until an empty slot is found and the key is inserted.
	* Essentially getting a position through a hash function and if that space is filled, fills next position and returns hash function with additional increment.

### Negatives of Open Addressing
* When reallocating, you must rehash every item because the hash functions depend on the size of the array, $m$

### Probing
#### Linear Probing
$h(k,i)=h'(k)+i mod m$
* $h'(k)$ is one of the hash functions.
* Clustering occurs as it continually checks the next available slot.
	* If a slot is filled it will choose the next.

#### Quadratic Probing
* No clustering

#### Double Hashing
* Use one that is a multiplication hash function and one that is division.
	* $h''(k)$ is either multiplication or division
	* $h'(k)$ is the other

# Load Factor
$$\alpha=\frac{n}{m}$$
* Average number of elements stored in a chain.
* Given a hash table $T$ with $m$ slots that stores $n$ elements, the load factor of $T$ is $\frac{n}{m}$

# Good Hash
* If the keys are random real numbers and uniformly distributed in the range $0\le k\lt 1$ then the hash function $h(k)=\lfloor{km}\rfloor$

## Division Method
* Map key $k$ into one of $m$ slots by taking the remainder of $k$ divided by $m$
$$h(k)=k\mod{m}$$

### Values of $m$
* Shouldn't be a power of 2
	* If $m=2^p$ then $h(k)$ is just the $p$ lowest-order bits of $k$
* Avoid Powers of 10 if dealing with decimals
* Pick a prime far from a power of 2

## Multiplication Method

$$h(k)=\lfloor{m(kA-\lfloor{kA}\rfloor)}\rfloor$$

1. Multiply the key $k$ by a constant $A$ in the range $[0,1]$
	1. Extract the fractional part of $kA$
2. Multiply the fraction of $kA$ by $m$ and take the floor of the result.



# Runtime
* Average runtime for searching for an element is $O(1)$
* **Simple Uniform Hashing**
	* Assumption is that any given element is equally likely to hash.
* Any hash table with chaining $\Theta(1+\alpha)$

# Storage
* $\Theta(\lvert{K}\rvert)$