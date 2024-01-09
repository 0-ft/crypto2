## Baby-Step-Giant-Step
- Discrete log: we have a group $\mathbb{F}_p^*$, element $g$ of order $l$ (i.e. $g^l=1$) and $g^a$, and we need to find $a$
- Alg:
	1. For i from 0 to $\sqrt{l}$, compute $b_i=g^i$
	2. For j from 0 to $\sqrt l+1$, compute $c_j=g^a\cdot g^{-j \sqrt l}$, break if you find $c_j=b_i$
	3. Return $a=i+\sqrt l \cdot j$
- Costs at most $2\sqrt l$ multiplications, plus some setup costs (inversion and an exponentiation to $\sqrt l$'th power, these become negligible), so it is called $O(\sqrt l)$

## Index Calculus
