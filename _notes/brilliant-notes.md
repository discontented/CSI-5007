--
layout: post
mathjax: true
--

* For any size 4 input, there will always be 6 comparisons made with two loops

```py
for I in range(n-1):
	for j in range(i+1, n):
		if lst[i] > lst[j]
			lst.switch(I, j)
```

* Comparisons occur at `if lst[i] > lst[j]`
* $\Theta$
