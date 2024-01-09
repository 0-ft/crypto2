from itertools import islice
import random
from utils import mod_inverse, is_prime, indent, dedent, print, prime_factors, is_generator, find_generators
import math

# (divisor, remainder) pairs
def crt_combine(modpairs, N):
    print(f"solving system of congruences mod {N} using CRT")
    indent()
    assert len(modpairs) > 0
    assert all([a == b or math.gcd(a, b) for a, _ in modpairs for b, _ in modpairs])
    print("all pairs are coprime ✅")
    assert math.prod([n for n, _ in modpairs]) == N
    print(f"product of moduli = {N} ✅")
    yz = []
    for i, (n, a) in enumerate(modpairs):
        print(f"x = {a} mod {n}")
        indent()
        yi = N // n
        print(f"y = N / {n} = {yi}")
        # zi = mod_inverse(yi, n)
        zi = pow(yi, -1, n)
        print(f"z = y^-1 = {zi}")
        yz.append((yi, zi))
        dedent()
    print(f"solution = sum(y * z * a) = {' + '.join([f'({y} * {z} * {a})' for (y, z), (_, a) in zip(yz, modpairs)])}")
    sol = sum([y * z * a for (y, z), (_, a) in zip(yz, modpairs)])

    for (n, a) in modpairs:
        assert sol % n == a

    print(f"solution = {sol} = {sol % N} mod {N} 🏁")
    dedent()
    return sol % N

def pohlig_hellman(p, g, a):
    print(f"solving discrete log {g}^x = {a} mod {p} using Pohlig-Hellman")
    indent()
    assert is_prime(p)
    print(f"{p} is prime ✅")
    assert is_generator(g, p)
    print(f"{g} is a generator of {p} ✅")
    facs = prime_factors(p - 1, return_powers=True)
    modpairs = []
    for f, rest in [(facs[i], facs[:i]+facs[i+1:]) for i in range(len(facs))][::-1]:
        print(f"factor f = {f}")
        indent()
        frp = math.prod(rest)
        frps = '*'.join(f'{f}' for f in rest)
        print(f"{a}^({frps}) = ({g}^({frps}))^r mod {p}")
        afrp = pow(a, frp, p)
        print(f"{a}^{frp} = {afrp} = {g}^({frp}r) mod {p}")
        indent()
        for r in range(f):
            gfrprp = pow(g, frp * r, p)
            print(f"r = {r}: {g}^({frp}*{r}) mod {p} = {g}^{frp*r} mod {p} = {gfrprp}{'✅' * (gfrprp == afrp)}")
            if gfrprp == afrp:
                break
        dedent()
        print(f"x = {r} mod {f}")
        modpairs.append((f, r))
        dedent()
    sol = crt_combine(modpairs, p-1)
    assert pow(g, sol, p) == a
    print(f"{g}^{sol} mod {p} = {a} ✅")
    print(f"x = {sol} 🏁")
    dedent()
    return sol

# gens = find_generators(37)
mps = pohlig_hellman(2*3*5*7*11*13*17*19*23*29*31+1, 79, 17)
# mps = pohlig_hellman(569, 492, 507)
# mps = pohlig_hellman(569, 6, 7531)
