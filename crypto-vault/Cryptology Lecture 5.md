- So far we haven't stopped adversaries from **modifying** messages
	- Most schemes we have looked at allow a predictable change in plaintext by modifying ciphertext (? length i guess)

## Message Authentication Codes
- We produce an auth tag from the key and message that can be used to verify they weren't modified since the tag was computed
- A MAC scheme looks like (Kg, Tag, Vfy) where:
	- Kg() -> k: key randomly generates a key
	- Tag(k: key, m: message) -> t: tag $\in T$
	- Vfy(k: key, (m: message, t: tag)) -> valid: boolean
- MAC scheme is **correct** iff for all k and m: Vfy(k, (m, Tag(k, m))) = T
	- Note no bidirectional certainty - there can be collisions
- Usually Vfy just recomputes and compares the tag
- Some attacks:![[Pasted image 20231223184527.png]]
	- **Existential unforgeability under chosen message**
		- Easier for attacker
		- Attacker can get a tag for chosen messages, then has to try to tag a new one
		- Question is whether they can create **a** (i.e. at least one) valid (message, tag) pair, without the key
		- $$\text{Adv}_{\text{MAC}}^{\text{euf-cma}}(\mathcal{A}) = \text{Pr}[\text{Exp}_{\text{MAC}}^{\text{euf-cma}}(\mathcal{A}) : \text{Vfy}_{k}(\tilde{m}, \tilde{t}) = \top \land \tilde{m} \text{ is fresh}]$$
		- The probability that the attacker produces a correct (m, t) pair, and they've never queried the oracle for the tag of that message before (fresh)
	- **Universal unforgeability under chosen message**
		- Harder for attacker
		- Question is whether they can correctly tag **any/all message they are given**
		- $$\text{Adv}_{\text{MAC}}^{\text{uuf-cma}}(\mathcal{A}) = \text{Pr}[\text{Exp}_{\text{MAC}}^{\text{euf-cma}}(\mathcal{A}) : \text{Vfy}_{k}(m^*, \tilde{t}) = \top]$$
		- ? so why is it "under chosen message"
			- because they can get tags for **chosen messages** from the oracle
	- Existential freshness requires that the message $\hat m$ has not been queried to the oracle. Universal freshness requires that the message $m^*$ does not get queried to the oracle.
	- Existential forgery is a **weaker security goal** because the criteria for success are broader than for UUF. UUF-CMA security therefore implies EUF-CMA. We can make a reduction from EUF to UUF.

### CBC-MAC
![[Pasted image 20231223191641.png]]
- MAC based on using a blockcipher in CBC mode, retaining only the last block of ciphertext as the mac
- XOR each plaintext block with previous ciphertext block before being encrypted
	- So each ciphertext block depends on all plaintext blocks before it

### Padding
- Want to turn a string of bits into a string of blocks, invertibly
- e.g. 10*: add a 1, then as many 0s as needed to hit block length

## Hashes
- $H_k(m\in M): d\in D$, and $\abs M > \abs D$ (**compression**)
- Often talking about **keyed** hash functions $H_k$
- Security notions
	- Collision resistance: probability (per try) that an attacker produces a pair of non-identical messages that have the same hash
	- Preimage resistance: probability (per try) attacker can produce a message which gives a hash chosen by us, given that hash
	- Second preimage resistance: probability (per try) attacker can produce a message with the same hash as a message chosen by us, given that message (and by extension able to determine the hash of it

## Authenticated Encryption
- Nonce-Based Authenticated Encryption schem E = (Kg, Enc, Dec)
	- Kg generates key
	- Enc takes key, nonce and message and outputs ciphertext
	- Dec takes key, nonce and ciphertext and outputs plaintext **OR $\false$, representing decryption failure**
	- Correct iff Dec(k, n, Enc(k, n, m)) = m
- ![[Pasted image 20231227153143.png]]
	- AE-security
	- Attacker tries to distinguish between experiment with real AE oracles and one where ciphertexts are randomly generated and decryption always fails

### (N)-IND-CCA
![[Pasted image 20231227154219.png]]
- $$\text{Adv}_{\text{Enc}}^{(n)\text{ind-cca}}(\mathcal{A}) = \text{Pr}[\text{Exp}_{\text{Enc}}^{(n)\text{ind-cca-real}}(\mathcal{A}) : \hat{b} = 1] - \text{Pr}[\text{Exp}_{\text{Enc}}^{(n)\text{ind-cca-ideal}}(\mathcal{A}) : \hat{b} = 1]$$
- 
### Constructing AE
- Can construct an AE-secure scheme from a nonce-based indistinguishability-secure **encryption** scheme and an EUF-CMA-secure **MAC scheme**
- 3 typical ways to do this: ![[Pasted image 20231227153646.png]]
	- mac-then-encrypt, encrypt-then-mac, encrypt-and-mac