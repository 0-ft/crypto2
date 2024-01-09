# Cryptographic Scheme Complexity
The complexity of a $\lambda$-bit scheme is considered in terms of the number of **basic bit operations** required compared to $\lambda$.

Operations are considered easy if the number of basic bit operations is **polynomial** in $\lambda$.

## Multiplication
We want to multiply $p\times q$.

Try the naive approach: add $\ob{q+...+q}{p\text{ times}}$ 
Since we have to perform $p$ additions, and $p$ has $\lambda$ bits so is of the order of $2^\lambda$, this algorithm has exponential complexity

### Double-and-add
1. Write $p=\sum_{i=0}^\lambda {c_i\times 2^i}, c_i\in\{0,1\}$ (write $p$ into binary form)
2. **Compute:** $$
\align{2^0\times q&=q\\
2^1\times q&=q+q&\text{1 addition}\\
2^2\times q&=2^1\times q+2^1\times q&\text{1 addition}\\
...\\
2^\lambda\times q&=2^{\lambda-1}\times q+2^{\lambda-1}\times q&\text{1 addition}\\
}$$Total: $\lambda$ additions
3. Observe that $pq=\b{\sum_{i=0}^\lambda{c_i\times2^i}}\times q=\sum_{i=0}^\lambda{c_i\times(2^i\times q)}$
4. **Add:** 
	```
	ans = 0
	for i in range(lambda):
		if c_i = 1:
			ans += 2**i * q
	```
	This has $\le 2^\lambda$ additions

## Exponentiation mod n
We want to exponentiate $m^e$.

### Square-and-multiply
1. Write $e=\sum_{i=0}^\lambda {c_i\times 2^i}, c_i\in\{0,1\}$ (write $e$ into binary form)
2. Observe  $m^e=m^{\sum_{i=0}^\lambda {c_i\times 2^i}}=\prod_{i=0}^\lambda\b{{m^2}^i}^{c_i}$
3. **Square:** $$
\align{
&m^{2^0}=m\mod n&\text{0 multiplications}\\
&m^{2^1}=m^2\mod n&\text{1 squaring}\\
&m^{2^2}=\b{m^2}^2\mod n&\text{1 squaring}\\
&...\\
&m^{2^\lambda}=\b{m^{2^{\lambda-1}}}^2\mod n&\text{1 squaring}\\
}$$
Total: $\lambda$ squarings

4. **Multiply:**
   ```
	ans = 0
	for i in range(lambda):
		if c_i = 1:
			ans += (m ** (2 ** i)) % n
	```
Total: $\le 2\lambda$ multiplications, $\therefore \le 4\lambda^2$ additions