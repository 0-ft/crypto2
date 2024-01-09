# Diffie-Hellman Key Exchange
| Diffie                                                | Public                               | Hellman                                               |
| ----------------------------------------------------- | ------------------------------------ | ----------------------------------------------------- |
| generates secret key ${sk}_D$ and public key ${pk}_D$ |                                      | generates secret key ${sk}_H$ and public key ${pk}_H$ |
|                                                       | ${pk}_D\rightarrow,{pk}_H\leftarrow$ |                                                       |
| generates **shared secret key** $ss$ from ${sk}_D$ and ${pk}_H$                                                      |                                      |          generates **same** ${sk}_S$ from ${sk}_H$ and ${pk}_D$                                            |

- encode $ss$ as a bit string $\in {\{0,1\}}^m$
- Diffie encrypts a message $m \in {\{0,1\}}^m$ as ciphertext $c={sk}_S\xor m$
- Diffie sends $c$ to Hellman over a public channel
- Hellman decrypts $c$ by xoring again - $m=c\xor ss$

In more detail:
- a large prime $p$ and a positive integer $n<p$ are chosen in public
- personal secret keys ${sk}_D,{sk}_H$ are selected uniformly at random such that $0<sk<p-1$
- public keys are generated as $n^{sk}\mod p$
- shared secret key $ss$ is generated as $ss={pk}_H^{{sk}_D}={pk}_D^{{sk}_H}=n^{{sk}_D{sk}_H}\mod p$
	- note that each party is able to generate the same value

## Adversary's Game
Given $p, n, n^d \mod p, n^h \mod p$, find any of $d, h, n^{hd}\mod p$
- Discrete Logarithm Problem


## ElGamal Encryption
### Setup
