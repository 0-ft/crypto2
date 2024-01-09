## Pohlig-Hellman
- Use SRT to solve some types of discrete log problem:
- for a prime $p$ a generator $g$, and a group member $x=g^a (\mod p)$, find $a$
- FLT: $a^{\phi(n)+1}=a\mod n$, and for primes $a^{p}=a\mod p$ (and so $a^{p-1}=1\mod p$)
	- So $g^{a+(p-1)k}=g^a \mod p$ for any integer $k$ ($k\in \mathbb Z$)
1. We factorise $\phi(p)=p-1$ into prime powers: $p-1=q_1^{e_1}\cdot q_2^{e_2}\cdot\ldots\cdot q_r^{e_r}$, where $q_i$ are prime
	1. Choose one of those factors e.g. $q_r$, and raise $x$ to the power of $\phi(p)/q_r$: $$\eqnarray{x^{\phi(p)/q_r}&=&{(g^a)}^{\phi(p)/q_r}}$$
2. Divide $a$ by $q_r$ and express it as a quotient $c$ and remainder $d$: $$\eqnarray{x^{\phi(p)/q_r}&=&{(g^a)}^{\phi(p)/q_r}\\
   &=&(g^{cq_r+d})^{\phi(p)/q_r}\\
   &=&(g^{cq_r})^{\phi(p)/q_r}\cdot(g^d)^{\phi(p)/q_r}\\
   &=&{(g^{\phi(p)})}^q\cdot g^{d\phi(p)/q_r}\\
   &=&g^{d\phi(p)/q_r}}$$
   4. $g^{d\cdot \phi(p)/q_r}$ is g t


5. For each $q_i$:
	- Write $a=a_0+a_1 q_i + a_2 q_i^2 +\ldots$, with $a_j\in [0, q_i-1]$
	- 


- Then we can find $a\mod (p-1)$ from all the $a\mod q_i^{e_i}$s
-  