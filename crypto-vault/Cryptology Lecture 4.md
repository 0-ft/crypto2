## Diffie Hellman Key Exchange
- prime $p$ and nonzero $g$ are chosen publicly
- A and B each generate a keypair by choosing an integer $d$ and determining $g^d \mod p$
- A and B trade their public keys $g^d$, $g^h$
- Then they raise the received public key to their own private key, so both end up with the shared secret $g^{dh} \mod p$

## Security Parameter
- Some $\lambda$ that is the key determining factor in a computation's runtime
- A computation might be "fast" e.g. polynomial in $\lambda$
	- i.e. you can define an upper bound for the number of basic operations needed as a polynomial in $\lambda$
- Or "slow" e.g. exponential or subexponential in $\lambda$
	- e.g. we might want the number of operations to be **lower**-bounded by $O(2^\lambda)$ (exponential) or  $O(\lambda^\alpha \log_2(\lambda)^{1-\alpha}), \alpha \in (0,1)$ (subexpontial)
- We can increase $\lambda$ to a size where polynomial algs are still fast (e.g. ms) and subexponential algs would take years
- In Diffie-Hellman, if $\lambda=\log_2(p)$, exponentiation $\mod p$ (for generation of keypair and computation of shared secret) should be polynomial in $\lambda$
	- But the inverse, computing the $d^{th}$ roots $\mod p$ (the *discrete logarithm problem*), should be slower (subexponential)

## ElGamal Encryption
- Setup:
	1. Diffie chooses a prime $p$ and a generator $g$ of $\mathbb{Z}/p\mathbb{Z} - \{0\}$.
	2. Diffie chooses a random secret $d \in \{1,\ldots,p - 1\}$ and computes $pk_D = g^d \mod p$.
	3. Diffie sends his public key $(p, g, pk_D)$ to Hellman.
- Encryption:
	1. Hellman chooses a random secret $h \in \{1,\ldots,p - 1\}$ and computes $pk_H = g^h \mod p$.
	2. Hellman computes the shared secret $ss = pk_D^h \mod p$.
	3. Hellman computes the encrypted message $enc_m = m \cdot ss$.
	4. Hellman sends the ciphertext $(pk_H, enc_m)$ to Diffie.
- Decryption:
	1. Diffie computes the shared secret $ss = pk_H^d \mod p$.
	2. Diffie computes the ciphertext $m = enc_m \cdot ss^{-1} \mod p$, which simplifies to $m = enc_m \cdot pk_H^{p-1-d} \mod p$.

- Note:
	- The inverse of the shared secret, $ss^{-1}$, is ${g^h}^{p-1-d}$ i.e. $pk_H^{p-1-d}$
	- If an attacker has both plaintext and ciphertext, they can recover the shared secret $ss$. 
		- So a new random per-message secret $h$ should be used for each message

### RSA
- Keygen:
	1. Pick two $\lambda$-bit primes $p\ne q$
	2. Compute $n=pq$ and $\phi(n)=(p-1)(q-1)$
	3. Pick $e$ coprime to $\phi(n)$
	4. Compute $d=e^{-1} \mod \phi(n)$, the inverse of $e$
	5. Keypair $pk, sk = (e,n),(d,n)$ 
- Encrypt:
	- Message is $m\in \mathbb{Z}_{[0,n-1]}$
	- Ciphertext is $c=m^e\mod n$
- Decrypt:
	- $m=c^d \mod n$
- #todo: more understanding

- We want:
	- Fast keygen steps 2 and 4 i.e. fast  multiplication and fast inverse finding
	- Attacker not to be able to find $d$ from $(e,n)$
		- Since $d$ can be found quickly as $e^{-1}\mod\phi(n)$, we need it to be slow to find $\phi(n)$ from $n$, as $n$ is public 
		- Since $n=pq$, finding $\phi(n)$ basically involves determining $n$'s two prime factors
	- Encrypt should be fast (exponentiation $\mod n$)
	- Recovering $m$ from $c$ to be hard
		- This could theoretically be done since $e,n$ are public, and $c=m^e\mod n \therefore m=c^{1/e} \mod n$
		- So we need computing $e$'th roots $\mod n$ to be hard/slow

#### Fast Multiplication: Double-and-Add
- To multiply $pq$
- Write $q$ in binary as $\sum_{i=0}^\lambda q_i\times 2^i$
- So $pq = \sum_{i=0}^\lambda q_i\times 2^i\times p$
- Compute the $2^i\times p$ terms by simply repeatedly doubling $p$ - only one addition per iteration
	- For a $\lambda$-bit number, this costs $\lambda$ additions (polynomial)
- Then just iterate the bits of $q$ and sum the $2^i\times p$ terms for which $q_i=1$
	- This costs at most $\lambda$ additions
- So overall at most $2\lambda$ additions

#### Fast Exponentiation: Square-and-Multiply
- $m^e=\prod_{i=0}^\lambda(m^{2^i})^{e_i}$
- Product of those $m^{2^i}$ terms where $e_i$ is 1
- We can make $m^{2^i}$ by repeatedly squaring $m$, each time takes 1 multiplication i.e. $2\lambda$ basic operations, and there are $\lambda$ squarings so overall $2\lambda^2$ basic ops
	- note the $\mod n$ here is important as otherwise you'd run out of memory fast
- Taking the product of those terms takes at most $\lambda$ multiplications, depending on the number of $1$ bits in $e$
	- So at most $2\lambda^2$ basic ops
- So square-and-multipy takes $\le 4\lambda^2$ ops


### Discrete Log Problem
- Given $g\mod p, g^d \mod p$, find $d \in [0,p-1]\mid$ 
- We want this to be hard
- In Diffie-Hellman, we usually choose a $g$ which is a generator of the group $(\mathbb{Z}/p\mathbb{Z})^**$
	- This means that private keys $g^d\mod p$ take $p-1$ different values, i.e. there are no collisions where $g^d\mod p$ is the same for two different values of $d$ with $1\le d\le p-1$
	- So the key space is maximised: the private key $d$ can correspond to any value in the group, avoiding reducing entropy

#### Order
- The *order* of an **element** is the minimum $d$ such that $g^d$ (or $g*g*\ldots*g$ $d$ times) $=id$ (the identity of the group
	- A generator necessarily has order $p-1$ because if it reached the identity before $p-1$ elements it would repeat itself, missing some elements
- If $g$ is a generator and $l$ divides $p-1$, then $g^\frac{p-1}{l}\mod p$ has order $l$
	- if $p-1=kl$, $g^\frac{p-1}{l}=g^\frac{kl}{l}=g^k$
	- order of $g^k=\frac{p-1}{k}=l$

- Problem: find int $a$ such that $2^a=17\mod 37$. We are told $2$ is a generator of the group.
- [ ] #todo: understand end of WS 4
- [ ] 