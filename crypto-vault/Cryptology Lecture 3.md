## Euclid's Algorithm
- If $d=gcd(a, b)$, then there exist integers $m,n$ such that $am+bn=d$
	- If $a,b\in \mathbb{Z}, \gcd(a,b)=d$ then $\exists m,n\in \mathbb{Z} \mid am+bn=d$.
- Useful for finding inverses by setting $d=1\therefore am+bn=1$
	- Only works if they have gcd of 1 (coprime)
- $a$ is invertible $\mod n$ iff $\gcd{(a,n)}=1$
- Find $m,n$ using the iterative remainders approach
- Corrol
## Groups
- A group is a pair of (set $G$, operation $*$) where $*$ maps a pair of elements in $G$ to another element in $G$
- $(G, *)$ is a group (or "$G$ defines a group under $*$") if the *group axioms* are satisfied:
	- It has an **identity**: $\exists e|\forall g \in G, g*e=e*g=g$
	- Every element has an **inverse**: $\forall g \in G, \exists h\ |\ g * h = h * g = e$
	- The operation is **associative**: $(a*b)*c=a*(b*c)$
- For any prime $p$, the set $\set{1\mod p, 2\mod p, \ldots,(p-1)\mod p}$ **is a group under multiplication**
- We call the set of integers mod n from 0 to n: $\mathbb Z/n\mathbb Z$
- and $(\mathbb Z/n\mathbb Z)^*$ is the set of **invertible elements** in $\mathbb Z/n\mathbb Z$
	- if $n$ is prime, then all elements are invertible under multiplication (so it forms a group)
- If the mod is a prime $p$, the group is *cyclic*: it can be *generated* using a number $g$ as the sequence $g \mod p, g^2 \mod p, \ldots, g^{p-1} \mod p$
	- i.e. $g$ generates $(\mathbb Z/p\mathbb Z)^*$
- ![[Pasted image 20231221132110.png]]

## Fermat's Little Theorem
- Euler $\phi$ function: count how many integers $0<m<n$ are coprime with $n$
	- $\phi(p) = p-1$ for $p$ prime
	- $\phi(pq)=(p-1)(q-1)$ for $q,p$ both prime
	- 
- FLT: for every integer $a$ and **squarefree** $n\in\mathbb Z_{>1}$ (squarefree = no square factors other than 1, i.e. no repeated prime factors)
	- $a^{\phi(n)+1}\equiv a \mod n$
	- if $n$ is prime, then this means $a^{n-1}\equiv 1 \mod n$
		- because there are n-1 coprime integers (every integer between 1 (inclusive) and the prime (exclusive)), so $\phi(n)=n-1$
		- and $a^{\phi(n)+1}\equiv a \mod n$ means $a^{\phi(n)}\equiv 1 \mod n$
		- 

## Sun-Tzu's Remainder Theorem
- n, m are coprimes > 1
- a, b are integers
- there exist c, d so that cm + dn = 1, and:
- x = bcm + adn mod mn uniquely satisfies x mod m = a and x mod n = b

- we might want to solve a problem like x = 2 mod 3, x = 2 mod 4
- this requires that the mods are coprime
- so we can find c, d using euclid's alg 

## Sets
- $\mathbb{N}$ - natural numbers. This includes all positive integers starting from 1. In some definitions, it also includes 0.

- $\mathbb{Z}$ - integers. It includes all positive and negative whole numbers, including 0.

- $\mathbb{Q}$ - rational numbers. These are numbers that can be expressed as a fraction of two integers, where the denominator is not zero.

- $\mathbb{R}$ - real numbers. This includes all rational and irrational numbers, but not complex numbers.

- $\mathbb{I}$ - irrational numbers. These are numbers that cannot be expressed as a simple fraction of two integers.

- $\mathbb{C}$ - complex numbers