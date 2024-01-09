[Learning Schedule](https://cryptpad.fr/sheet/#/2/sheet/edit/W-5sl+6pXAMpN0Okz4W8Lej+/)

# One-Time Ciphers

# Perfect Secrecy


Considering schemes where $M=C$


## Key Recovery
Key recovery security experiment:
$$
\align{Exp&_E^{kr-pas}(\ob{A}{\text{adversary}}) \\\\
&k\leftarrow Kg \\\\
&\hat{k}\leftarrow A()}
$$
$A$ wins if $\hat{k}=k$ (the guessed key is correct)


- The **advantage** of an adversary in passively recovering the key is defined as the probability that their guess is correct:$$\ob{Adv_E^{kr-pas}(A)}{\text{advantage of A}}=Pr[Exp_E^{kr-pas}(A):\hat{k}=k]$$
- We say that $E$ is $(t,\epsilon)-kr-pas$ secure if for any adversary $A$ that runs in time $\le t$, the *advantage* of $A$ is bounded by $\epsilon$.
- If the adversary has no information about the system, the best they can do is guess the key: $$\align{A_{\text{guess}}()&\\&k\leftarrow Kg\\&return k}$$
- In this case, the running time of the adversary $t=t_{Kg}$, and the advantage $\epsilon=\frac{1}{\abs{\mathcal{K}}}$ (one over the size of the keyspace).

>[!note] Bits of Security
>- currently, 80 bits is considered enough for security
>- 128 bits is considered secure for next 10 years
>- 256 bits is recommended

### One-Time Known Ciphertext Attack
Key is generated, adversary is given the scheme and one generated ciphertext
$$\align{Exp&_E^{\text{kr-1kca}}(A)\\
&k\leftarrow Kg\\
&m\leftarrow \mathcal{M}\\
&c\leftarrow E_k(m)\\
&\hat{k}\leftarrow A(c)
}
$$
### One-Time Known Plaintext Attack
Key is generated, adversary is given the scheme, one plaintext and its corresponding ciphertext
$$\align{Exp&_E^{\text{kr-1kca}}(A)\\
&k\leftarrow Kg\\
&m\leftarrow \mathcal{M}\\
&c\leftarrow E_k(m)\\
&\hat{k}\leftarrow A(m,c)
}
$$



## Theorems
- OTP satisfies perfect security
- Shannon's Theorem:
	- Scheme $E=(Kg, E, D)$ is only **perfectly secure** iff Kg draws from K uniformly at random, and for all (m,c) pairs there is exactly one unique key k such that $E_k(m)=c$
	- OTP is the **only enciphering scheme** with perfect security
- An enciphering scheme has perfect secrecy if and only if it has perfect **indistinguishability**
- 

## Indistinguishability
- A scheme E satisfies perfect indistinguishability iff for all c and m, the probability that m enciphers to c with a random key k is $1/\abs C$, i.e. the encipherings are evenly distributed over the ciphertext space.
	- $\forall c \in C, m \in M,\ \Pr[c^* = c | m^* = m] = |C|^{-1}$
	- Given a particular message m* and its resulting ciphertext c* (when encrypted with a randomly selected key from K), the distribution of c* over C is uniformly random, so the probability that it equals some particular ciphertext c is $1/\abs C$
	- No particular ciphertext is more likely than any other, making it impossible for an observer to gain any information about the plaintext by looking at the ciphertext
- In game-based terms, we can consider a game where the attacker tries to distinguish two different experiments:
  ![[Pasted image 20231219161611.png]]
	- in each game, a key is randomly chosen and the attacker provides a message $m$.
	- in one game, the ciphertext is produced by encrypting $m$, and in the other, it is selected randomly from $C$
	- then the attacker must try to decide whether the ciphertext is correct (i.e. returning some boolean $\hat b$ when provided $c*$)
	- The advantage of the attacker in *one-time distinguishing E from random* is $$\text{Adv}_{E}^{\text{ind}}(A) = \text{Pr}[\text{Exp}_{E}^{\text{ind-real}}(A) : \hat{b} = 1] - \text{Pr}[\text{Exp}_{E}^{\text{ind-ideal}}(A) : \hat{b} = 1]
$$
	- i.e. the difference in probabilities that A will return 1 for each experiment
	- If the difference is positive, the attacker can (somewhat) distinguish real ciphertexts of $m$ from randomly generated ones.
	- So a **perfectly indistinguishable** scheme has $\text{Adv}_{E}^{\text{ind}}(A) = 0$

## Blockciphers
- A blockcipher with block length $l$ is a **symmetric enciphering scheme** with $M=C=\set{0,1}^l$
	- i.e. the message and cipher space are all permutations of $l$ binary bits
- A blockcipher is effectively a *permutation* as it maps every possible plaintext block onto a unique ciphertext block, and $M=C$ so it's effectively a permutation, (a reordering, a mapping)

### Key Recovery
- Consider a game where we generate a key and then the adversary can repeatedly request encryption of a plaintext with that key and receive the ciphertext ![[Pasted image 20231220124158.png]]
- They can brute-force (exhaustively search) the key space:
	- Choose some random plaintext $m$
	- Iterate through all $\hat k\in K$:
		- Encipher $m$ with $\hat k$ to get $\hat c$
		- Request enciphering of $m$ from us to receive $c$
		- Compare $c$ with $\hat c$, if they are equal the key matches ours
- In this context the advantage is $$\text{Adv}_{E}^{\text{kr-cpa}}(A) = \text{Pr}[\text{Exp}_{E}^{\text{kr-cpa}}(A) : \hat{k} = k^*]$$
	- The probability that the adversary guesses the correct key
	- We say E is $(t,q,\epsilon)$-secure if the advantage is $\le\epsilon$ for an adversary running in time at most $t$ and with at most $q$ queries from the *oracle* for encipherings

### Indistinguishability (Pseudorandomness)
- With block ciphers, indistinguishability is called pseudorandomness
	- I guess like "fake-random", like you can't tell if it's random, rather than it's trying to actually be random
- ![[Pasted image 20231220124144.png]]
- In this game, the attacker tries to distinguish between the two experiments
- Crucially, the attacker **cannot make repeat queries** with the same input as then they would observe that one experiment produces different $c$ for the same $m$ (as it's in fact random, rather than real enciphering), giving the game up
- The advantage is: $$\text{Adv}_{E}^{\text{ind}}(A) = \text{Pr}[\text{Exp}_{E}^{\text{ind-real}}(A) : \hat{b} = 1] - \text{Pr}[\text{Exp}_{E}^{\text{ind-ideal}}(A) : \hat{b} = 1]$$
	- The diff in probability that it gives 1 for the correct experiment vs the wrong one
#### Birthday Bound
- An adversary that makes $q$ queries to a random permutation (the "fake" experiment) will find a collision with probability apprx $\frac{q\times(q-1)}{2\times\abs C}$ 
- This "birthday bound" places a constraint on the block length $l$ of the blockcipher, requiring it be above some minimum level to reduce collision probability to a desirable level
- Birthday bound reverse: $n=\sqrt{2N\ln(\frac{1}{1-p}})$
