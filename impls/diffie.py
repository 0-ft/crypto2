from utils import is_prime, indent, dedent, print

class DiffieHellman:
    def __init__(self, p, g):
        print("initializing Diffie-Hellman")
        indent()
        self.p = p
        self.g = g
        assert is_prime(p)
        print("p is prime ✅")
        assert g < p
        print("g < p ✅")
        assert g > 0
        print("g > 0 ✅")
        dedent()

    def keypair(self, d):
        print(f"generating keypair with d = {d}")
        indent()
        y = pow(self.g, d, self.p)
        print(f"g^d mod p = {y}")
        kp = (y, d)
        print(f"keypair = {kp} 🏁")
        dedent()
        return kp
    
    def shared_secret(self, pk, d):
        s = pow(pk, d, self.p)
        print(f"shared secret = pk^d mod p = {pk}^{d} mod {self.p} = {s} 🏁")
        return s


# t = DiffieHellman(37, 2)
# ss = t.shared_secret(5, 6)

# print(ss)
    
d = DiffieHellman(59, 2)
kpA = d.keypair(9)