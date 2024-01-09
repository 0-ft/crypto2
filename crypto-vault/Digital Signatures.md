## ElGamal Signatures
- Choose prime $p$, generator $g$
- Choose a random private key $0<a<p-1$ and make public key $pk=g^a\mod p$
- Choose a message $\mod p-1$ (because the message is in the **exponent** of $g$)
- Sign:
	- Choose a nonce $0<k<p-2$, coprime to $p-1$
	- Compute $r=g^k\mod p$
	- Compute $sig=k^{-1}(m-ar)\mod(p-1)$
	- Publish $(r, sig)$
- Verify:
	- Check $g^m={pk}^r\cdot r^{sig}\mod p$
		- because ${pk}^r\cdot r^{sig} = g^{ar}\cdot g^{k\cdot k^{-1}(m-ar)}$
		- $=g^{ar+m-ar}=g^m$

- Nonce must be kept secret to avoid key recovery ($m$, $r=g^k$, $sig=k^{-1}(m-ar)$ are all public -> $k\cdot sig=k\cdot k^{-1}(m-ar)=m-ar$ -> $a=\frac{m-k\cdot sig}{r}$
- Nonce must not be reused: allows attacker to recover $k$ and therefore $a$


%% - Key recovery without the nonce requires finding $a$ such that:
	- $\frac{g^m}{pk^r}=r^{k^{-1}(m-ar)}$
	-  %%
	- 