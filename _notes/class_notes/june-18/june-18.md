$x_{1,j}=1$ - Demand
$x_{i,n}=1$ - Supply

Two families of methods: simplex methods or interior-point methods
# Simplex Methods
"Standard Form"
* Decide to always maximize
To convert an equality into an inequality:
$$ax_1+bx_2=5\equiv {ax_1+bx+2\le 5, ax_1+bx_2\ge 5}$$
Then convert $ax_1+bx+2\ge 5$ to $-ax_1-bx_2\le -5$

# P vs NP
## Runtime
* Before $n$ was defined loosely as the size of the input (number of elements in array)
* An algorithm running in polytime, $n$ is the number of bits of input.
* Need to be polynomial in size of the input.

### Example
* Knapsack Problem
* Runtime: $O(nW)$
* Size of the input:
	* In bits: $O(128\bullet n\bullet logW)$
		* The size of the input = $128\bullet n$
		* The number of bits for an integer is $log(integer)$

## Deterministic Turing Machine
* A Turing machine is a tape with R/W head.
	* Reads from the tape then moves a step ahead and writes.
* "Deterministic"
	* There are no parallel threads.

# The class $P$
* A problem P is in the class $P$ if there is an algorithm running in time $P$
* Sorting
* Searching
* Matrix Multiplication

# The class $NP$
* Does not mean "not polynomial"
* If you take an instance of some problem and some additional data, you can answer Yes or No.
	* "Is there ______ that would equal ______"
	* Must provide data that would equal that condition so it can be answered as Yes or No
* Problem:
	* Problem to be solved.
* Certificate:

$P\subset NP$
* Proves "not polynomial" as that would read "polynomial is a subset of not polynomial"
$P\subsetall NP$
* To disprove find one problem that is P and prove that it is not in NP
	* Proving that it is not in NP is not possible to show.

$P=NP$
* Need to show that all problems in $P$ are in $NP$

# The class Co-$NP$
* Give me a problem, give me an instance, you can answer "No in polytime"

# Problems in Co-$NP\cap NP$
* $\all P$

Every problem instance with this type of certificate.
## Examples
### SAT Problem
* Given a Boolean is there a true solution?
* Certificate to verify Yes: the solution itself.
	* The certificate is a solution.
* The problem class of SAT is therefore in $NP$

### Tautology
* Given a boolean is it always true?
* You cannot give a certificate to verify yes.
* You can give a certificate to verify no.
* This problem class is in Co-$NP$
* You don't care about solving the problem, you are verifying a solution that is given.
	* If you can verify the solution in polytime, then it is in $NP$

# Reducability
* A problem instance can be reduced to another problem instance.
* If it was possible to reduce the original problem instance to another problem instance, the answer can be extracted to the original problem instance.

# The Class $NP$-Complete
* A problem $P$ is in class $NP$-complete if it is in $NP$ and if all other problems in $NP$ can be reduced to $P$

