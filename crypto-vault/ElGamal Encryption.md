## Setup
1. A chooses a prime $p$ and an integer $n, 0<n<p-1$
2. A chooses a random secret key $sk_a, 1 \le sk_a \le p-2$
3. A computes a public key $pk_a=n^{sk_a}\mod p$
4. A sends $(p, n, pk_a)$ to B

## Encryption
5. B chooses a random secret key $sk_b, 1 \le sk_b \le p-2$
6. B computes a public key $pk_b=n^{sk_b}\mod p$
7. B computes the shared secret $ss=pk_a^{sk_b}\mod p$
8. B encodes a message as an integer $\mod p$
9. B encrypts the message using ${enc}_m=m\times ss\mod p$
10. B sends $({enc}_m, pk_b)$ to A

## Decryption
11. A computes the shared secret $ss=pk_b^{sk_a}\mod p$
12. A decrypts the message via $m=ss^{-1}\times{enc}_m\mod p$