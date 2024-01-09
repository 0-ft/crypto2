from utils import mod_inverse, is_prime, indent, dedent, print, prime_factors, bigprimes, find_generators, group_order
import math

def bsgs(p, g, gta):
    print(f"baby-step giant-step solving discrete log {g}^x = {gta} mod {p}")
    indent()
    assert is_prime(p)
    print(f"{p} is prime ✅")
    l = group_order(g, p)
    print(f"l = order of {g} in Z_{p} = {l}")
    m = math.ceil(math.sqrt(l))
    print(f"ceil(sqrt(l)) = {m}")

    print(f"computing bi = g^i mod p for i = 0 - {m}")

    header = f"│ {'i':<4} │ {'bi':<6} |"
    print('┌' + '─' * (len(header) - 2) + '┐')
    print(header)
    print('├' + '─' * (len(header) - 2) + '┤')
    bis = [pow(g, i, p) for i in range(m + 1)]
    print("".join(f"│ {i:<4} │ {bis[i]:<6} |\n" for i in range(m + 1)))
    print('└' + '─' * (len(header) - 2) + '┘')

    inv_g = pow(g, -1, p)
    print(f"g^-1 = {inv_g} mod {p}")

    gtmm = pow(inv_g, m, p)
    print(f"g^(-sqrt(l)) = {gtmm} mod {p}")

    header = f"│ {'j':<4} │ {'cj':<6} |"
    print('┌' + '─' * (len(header) - 2) + '┐')
    print(header)
    print('├' + '─' * (len(header) - 2) + '┤')

    for j in range(m + 2):
        ci = gta * pow(gtmm, j, p) % p
        print(f"│ {j:<4} │ {ci:<6} │")
        if k := next((k for k in range(m+1) if bis[k] == ci), None):
            print('└' + '─' * (len(header) - 2) + '┘')
            print(f"\nfound collision at b{j} = c{k} = {ci}")
            break
    print(f"c{j} = b{k}")
    print(f"→ {g}^a * g^({-m}*{j}) = {g}^{k} mod {p}")
    print(f"→ a = {k} + {m*j} = {k + m*j} 🏁")
    dedent()

#bsgs(101, 3, 37)
bsgs(101, 9, 17)