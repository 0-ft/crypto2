## Electronic Codebook (ECB)
![[Pasted image 20231228143415.png]]
- **Insecure** because no **diffusion**: identical plaintext blocks have identical ciphertext blocks, revealing patterns

## Nonce-Based Counter (CTR)
![[Pasted image 20231230134144.png]]
- Combine the nonce with a counter incremented for each block, and encipher the combination with $k$ using the blockcipher 
- Use the resulting set of pseudorandom ciphertexts as OTPs for the message blocks
- If the blockcipher used (E) is pseudorandom (indistinguishable), then CTR with E is nonce-based secure
- 

## Cipher Block Chaining (CBC)
![[Pasted image 20231230134201.png]]
- Insecure when nonces are reused
