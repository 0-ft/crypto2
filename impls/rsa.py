from itertools import islice
import random
from utils import mod_inverse, is_prime, indent, dedent, prime_factors, print, bigprimes, find_generators
import math

class RSA:
    def __init__(self, p=None, q=None, n=None):
        print("initializing RSA")
        indent()
        if n is not None and p is None and q is None:
            facs = prime_factors(n)
            assert len(facs) == 2, "n must have exactly two prime factors (although RSA standard allows for more)"
            p, q = facs
            print(f"found prime factors of {n}: p={p}, q={q} ✅")
        self.p = p
        self.q = q
        if p:
            assert is_prime(p)
            print("p is prime ✅")

            if q:
                assert is_prime(q)
                print("q is prime ✅")
                if n:
                    assert n == p * q
                    self.n = n
                    print(f"n = pq = {n} correct ✅")
                else:
                    self.n = p * q if p and q else None
                    print(f"n = pq = {self.n}")
                self.phi = (p - 1) * (q - 1)
                print(f"phi = (p-1) * (q-1) = {self.phi}")
        
        dedent()
        

    def keypair(self, e):
        print(f"generating RSA keypair with PUBLIC e = {e}")
        indent()
        assert self.phi
        # assert 2 < e < self.phi
        # print(f"e < phi ✅")
        assert math.gcd(e, self.phi) == 1
        print(f"e = {e} is coprime to phi = {self.phi} ✅")

        # d = mod_inverse(e, self.phi)
        d = pow(e, -1, self.phi)
        print(f"d = e^-1 mod {self.phi} = {d} (show inversion?) ❗")
        kp = ((e, self.n), (d, self.n))
        print(f"keypair = (pk, sk) = {kp} 🏁")
        dedent()

        return kp

    def encrypt(self, m, e):
        c = pow(m, e, self.n)
        print(f"RSA encrypted message {m}, c = {m}^{e} mod {self.n} = {c} 🏁")
        return c

    def encrypt_block(self, mm, e):
        cc = [pow(m, e, self.n) for m in mm]
        print(f"RSA encrypted message {mm}, c = {cc} 🏁")
        return cc

    def decrypt(self, c, d):
        m = pow(c, d, self.n)
        print(f"decrypted ciphertext {c}, m = {c}^{d} mod {self.n} = {m} 🏁")
        return m

    def decrypt_block(self, cc, d):
        m = [pow(c, d, self.n) for c in cc]
        print(f"RSA decrypted ciphertext {cc}, m = {m} 🏁")
        return m

    def sign(self, m, d):
        sig = pow(m, d, self.n)
        print(f"RSA signed message {m} with secret key {d}, sig = {m}^{d} = {sig} 🏁")
        return sig
    
    def verify(self, m, sig, e):
        v = pow(sig, e, self.n) == m
        if v:
            print(f"sig^e mod n = m: RSA signature is valid ✅")
        else:
            print(f"sig^e mod n ≠ m: RSA signature is invalid ❌")
        return v

# t = RSA(p=307, q=311)
# pk, sk = t.keypair(247)

# cc = [94755, 87565, 41862, 49231, 34234, 17479, 26771, 87503]


def test_signverif():
    for i in range(100):
        p = random.choice(bigprimes)
        q = p
        while q == p:
            q = random.choice(bigprimes)
        assert p != q
        rsa = RSA(p=p, q=q)
        e = random.choice(list(islice((e for e in range(1, rsa.phi) if math.gcd(e, rsa.phi) == 1), 10)))
        pk, sk = rsa.keypair(e)
        m = random.randrange(1, rsa.n)
        sig = rsa.sign(m, sk[0])
        assert rsa.verify(m, sig, pk[0])
        assert not rsa.verify(m+1, sig, pk[0])
        assert not rsa.verify(m, sig+1, pk[0])
        # assert verify(sign())


# print(prime_factors(91))
# r = RSA(n=91)
# print(r.decrypt(r.encrypt(30, 73), 5))
        
r = RSA(n=2067).keypair(101)

# print(r.keypair(62))

