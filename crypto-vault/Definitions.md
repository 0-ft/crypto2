## Security Definitions
$\mathcal{M}$ is the set of plaintext messages
$\mathcal{K}$ is the set of keys
$\mathcal{C}$ is the set of ciphertexts
$Kg$ is a key generation algorithm (probabilistic and outputs a value in $\mathcal{K}$
$E$ is an *enciphering algorithm*, **deterministically** enciphers an input message (from $\mathcal{M}$ *under* a key in $\mathcal{K}$ into a ciphertext in $\mathcal{C}$
$D$ is a deciphering algorithm (the inverse of $+E$)


### Kerckhoff's Principle
(roughly) when devising a security system, always assume that the adversary will know all the details of how the system works


### Security Experiment
Specifies:
- adversary's goal
- how adversary can interact with the system

### Enciphering Scheme
- A triple of algorithms Kg, E and D
	- Kg **randomly generates a key** $k \in K$ 
	- E takes a key k and message $m \in M$ to create a **ciphertext** $c \leftarrow E_k(m) \in C$
		- we are considering cases where $C=M$ i.e. ciphertexts are from the same space as plaintexts
	- D takes $k$ and $c$ and outputs a **purported** deciphered message $m' \leftarrow D_k(c)$
- So **an enciphering scheme is correct iff** for all $k$ and $m$, $D_k(E_k(m))=m$

## Security Goals
- **One-wayness:** recovering the plaintext **in full** from the ciphertext should be hard
- **Perfect secrecy**: the ciphertext should reveal **no information** about the plaintext
	- This is captured by the notion that the distribution over ciphertexts induced by enciphering a random plaintext with a freshly generated key is **independent from the plaintext** (the plaintext doesn't affect the ciphertext distribution, so knowledge of the ciphertext doesn't narrow down the plaintext)
	- i.e. $\forall c\in C, m\in M, P\b{m*=m,m*\leftarrow_\$M|c*=c}=P\b{m*=m}$
		- for all ciphertext-plaintext pairs, the probability that the a uniform-randomly selected plaintext $m*=m$ given that its enciphering $c*=c$ is the same as the unconditional probability $m*=m$
		- so the condition that $c*=c$ doesn't affect the probability of $m$ being any random plaintext $m*$

## Properties
>[!define] Commutativity
>Commutativity is a property of an operation. $*$ is commutative, then $x*y=y*x$.
>^commutativity-def

>[!define] Associativity
>Associativity is a property of an operation. $*$ is associative, then $x*(y*z)=(x*y)*z$
>^associativity-def

>[!define] Injective
>A function is injective if each output is mapped to by **at most one** input.
>^injective-def

>[!define] Surjective
>A function is surjective if every output is mapped to by **at least one** input.
>^surjective-def

>[!define] Bijection
>	A function is bijective if it is both [[#^injective-def|injective]] and [[#^surjective-def|surjective]] - i.e. it is a perfect **one-to-one** mapping.
>^bijection-def

>[!define] Group
>A group $\b{S,+}$ is a combination of a set $S$ and a binary operator $+$ that satisfies certain algebraic properties:
>- existence of identity and inverses
>- [[#^associativity-def|associativity]]
>^group-def

