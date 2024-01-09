from utils import is_prime, indent, dedent, print, is_generator, smallprimes, bigprimes, find_generators, mod_inverse, suppress, unsuppress
import math
import random
from itertools import islice

class ElGamal:
    def __init__(self, p, g):
        print("initializing ElGamal")
        indent()
        self.p = p
        self.g = g
        assert is_prime(p)
        # assert is_generator(g, p)
        print("p is prime ✅")
        assert g < p
        print("g < p ✅")
        assert g > 0
        print("g > 0 ✅")
        dedent()
        print(f"ElGamal intialised with parameters p = {p}, g = {g} 🏁")

    def pubkey(self, d):
        print(f"generating ElGamal pubkey with d = {d}")
        indent()
        assert d < self.p
        print(f"d < p ✅")
        assert d > 0
        print(f"d > 0 ✅")
        pkD = pow(self.g, d, self.p)
        print(f"pkD = g^d mod p = {self.g}^{d} mod {self.p} = {pkD} 🏁")
        dedent()
        return pkD

    def encrypt(self, m, h, pkD):
        print(f"ElGamal encrypting message {h} with pkD = {pkD}")
        indent()
        assert h < self.p
        print(f"h < p ✅")
        assert h > 0
        print(f"h > 0 ✅")

        pkH = pow(self.g, h, self.p)
        print(f"pkH = g^h mod p = {self.g}^{h} mod {self.p} = {pkH}")

        
        ss = pow(pkD, h, self.p)
        print(f"ss = pkD^h mod p = {pkD}^{h} mod {self.p} = {ss}")

        c = m * ss
        print(f"c = m * ss = {m} * {ss} = {c} 🏁")

        dedent()
        return (pkH, c)

    def decrypt(self, c, pkH, d):
        print(f"ElGamal decrypting ciphertext {c} with pkH = {pkH} and d = {d}")
        indent()
        ss = pow(pkH, d, self.p)
        print(f"ss = pkH^d mod p = {pkH}^{d} mod {self.p} = {ss}")

        inv = pow(ss, -1, self.p)
        print(f"inv = ss^-1 mod p = {ss}^-1 mod {self.p} = {inv}")

        m = c * inv % self.p
        print(f"m = c * inv mod p = {c} * {inv} mod p = {m} 🏁")

        dedent()
        return m

    def recover_ss(self, m, c):
        print(f"recovering ElGamal shared secret from message {m} and ciphertext {c}")
        indent()
        m_inv = pow(m, -1, self.p)
        print(f"m^-1 mod p = {m}^-1 mod {self.p} = {m_inv}")
        ss = c * m_inv % self.p
        print(f"ss = c * m^-1 mod p = {c} * {m_inv} mod p = {ss} 🏁")
        dedent()
        return ss
    
    def sign(self, m, d, k):
        print(f"ElGamal signing message {m} with d = {d}, nonce k = {k}")
        indent()

        assert 0 < d < (self.p - 2)
        print(f"0 < d < p-2 ✅")

        assert 0 < k < self.p - 1
        print(f"0 < k < p-1 ✅")

        assert math.gcd(k, self.p - 1) == 1
        print(f"k is coprime to p-1 ✅")

        assert 0 < m < (self.p - 1)
        print(f"0 < m < p-1 ✅")

        r = pow(self.g, k, self.p)
        print(f"r = g^k mod p = {self.g}^{k} mod {self.p} = {r}")
        k_inv = pow(k, -1, (self.p-1))
        sig = (k_inv * (m - d*r)) % (self.p-1)
        print(f"sig = k^-1 * (m - d*r) mod (p-1) = {k_inv} * ({m} - {d}*{r}) mod {self.p-1} = {sig} 🏁")
        print(f"signature = (r, sig) = ({r}, {sig})")
        dedent()
        return (r, sig)
    
    def verify(self, m, sigpair, pk):
        r, sig = sigpair
        print(f"verifying ElGamal signature ({r}, {sig}) on message {m} with pk = {pk}")
        indent()

        assert 0 < r < self.p
        print(f"0 < r < p ✅")
        assert 0 < sig < self.p-1
        print(f"0 < sig < p-1 ✅")

        lhs = pow(self.g, m, self.p)
        print(f"g^m mod p = {self.g}^{m} mod {self.p} = {lhs}")
        rhs = (pow(pk, r) * pow(r, sig)) % self.p
        print(f"pk^r * r^sig mod p = {pk}^{r} * {r}^{sig} mod {self.p} = {rhs}")
        if lhs == rhs:
            print("g^m = pk^r * r^sig: ElGamal signature is valid ✅")
        else:
            print("g^m ≠ pk^r * r^sig: ElGamal signature is invalid ❌")
        dedent()
        return lhs == rhs
    
    @staticmethod
    def nonce_reuse_attack(p, m1, sigpair1, m2, sigpair2):
        print(f"recovering ElGamal private key d from messages {m1} and {m2} with signatures {sigpair1}, {sigpair2}")
        assert sigpair1[0] == sigpair2[0]
        r, sig1 = sigpair1
        _, sig2 = sigpair2
        print(f"r1 = r2 = {r} ✅")
        indent()
        print(f"step 1: recover nonce")
        indent()
        print(f"sig1 = k^-1(m1 - d * r) mod (p-1)")
        print(f"  → d * r= m1 - sig1 * k mod (p-1)")
        print(f"sub into sig2: sig2 = k^-1 * (m2 - d * r) mod (p-1) → sig2 = k^-1 * (m2 - (m1 - sig1 * k)) mod (p-1)")
        print(f"  → sig2 = k^-1 * (m2 - m1 + sig1 * k) mod (p-1)")
        print(f"  → sig2 = k^-1 * (m2 - m1) + sig1 mod (p-1)")
        print(f"  → k = (m2 - m1) / (s2 - s1) mod (p-1)")
        k = ((m2 - m1) * pow(sig2 - sig1, -1, p-1)) % (p-1)
        print(f"k = (m2 - m1) / (s2 - s1) mod (p-1)")
        print(f"  = ({m2} - {m1}) * ({sig2} - {sig1})^-1 mod {p-1}")
        print(f"  = {(m2 - m1)} * {pow(sig2 - sig1, -1, p-1)} mod {p-1}")
        print(f"  = {k} ✅")
        dedent()
        print(f"step 2: recover ElGamal private key")
        indent()
        print(f"sig1 = k^-1 * (m1 - d * r) mod (p-1)")
        print(f"  → d*r = m1 - sig1 * k mod (p-1)")
        print(f"  → d = (m1 - sig1 * k) * r^-1 mod (p-1)")
        print(f"d = (m1 - sig1 * k) * r^-1 mod (p-1)")
        print(f"  = ({m1} - {sig1}*{k})*{r}^-1 mod {p-1}")
        print(f"  = ({m1 - sig1*k}) * {pow(r, -1, p-1)} mod {p-1}")
        d = (m1 - sig1*k) * pow(r, -1, p-1) % (p-1)
        print(f"  = {d} 🏁")
        dedent()

        print(f"step 3: verify")
        indent()
        print(f"find generator g such that r = g^k")
        print(f"  → g = r^(k^-1) mod p")
        print(f"  = {r}^({k}^-1) mod {p}")
        g = pow(r, pow(k, -1, p-1), p)
        print(f"  = {g} ✅")
        print(f"test signing with p = {p},g = {g}, d = {d}, k = {k}")
        suppress()
        t = ElGamal(p, g)
        r1v, sig1v = t.sign(m1, d, k)
        r2v, sig2v = t.sign(m2, d, k)
        unsuppress()
        assert r1v == r and sig1v == sig1
        print(f"sign({m1}, {d}, {k}) = ({r1v}, {sig1v})✅")
        assert r2v == r and sig2v == sig2
        print(f"sign({m2}, {d}, {k}) = ({r2v}, {sig2v}) ✅")
        dedent()
        print(f"\nElGamal private key d = {d} 🏁")
        dedent()





def test_signverif():
    for i in range(100):
        p = random.choice(bigprimes)
        g = random.choice(list(islice(find_generators(p), 10)))
        d = random.randrange(1, p-2)
        k = random.choice(list(islice((k for k in range(1, p-1) if math.gcd(k, p-1) == 1), 10)))
        m = random.randrange(1, p-1)
        print(f"testing ElGamal signing with p = {p}, g = {g}, d = {d}, k = {k}, m = {m}")
        t = ElGamal(p, g)
        pk = t.pubkey(d)
        sig = t.sign(m, d, k)
        assert t.verify(m, sig, pk)
        assert not t.verify(m+1, sig, pk)
        assert not t.verify(m, (sig[0], sig[1]+1), pk)
    # t = ElGamal(37, 2)
    # pkD = t.pubkey(7)

    # sig = t.sign(17, 7, 5)
    # t.verify(17, sig, pkD)

# print(list(find_generators(103)))

# el = ElGamal(103, 5)
# print(el.decrypt(86, 94, 59))

# nss = el.recover_ss(52, 70)
# c4 = nss * 4 % 103
# print(nss)
# print(c4)



# print(list(find_generators(227)))
# el = ElGamal(227, 5)
# ElGamal.nonce_reuse_attack(227, 100, (171, 154), 11, (171, 3))
