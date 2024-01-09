from utils import mod_inverse, is_prime, indent, dedent, print, prime_factors, bigprimes, find_generators, group_order
import math

def pollard_rho(p, g, gta):
    print(f"pollard rho solving discrete log {g}^x = {gta} mod {p}")
    indent()
    assert is_prime(p)
    print(f"{p} is prime ✅")
    l = group_order(g, p)
    print(f"l = order of {g} in Z_{p} = {l}")
    header = f"│ {'i':<4} │ {'Gi':<6} │ {'Gi % 3':<6} │ {'bi':<6} │ {'ci':<6} │"
    print('┌' + '─' * (len(header) - 2) + '┐')
    print(header)
    print('├' + '─' * (len(header) - 2) + '┤')

    ss = [(g, 1, 0)]
    print(f"│ {0:<4} │ {ss[-1][0]:<6} │ {ss[-1][0]%3:<6} │ {ss[-1][1]:<6} │ {ss[-1][2]:<6} │")
    for i in range(1, l):
        opt = ss[-1][0] % 3
        if opt == 0:
            ss.append((
                (ss[-1][0] * g) % p,
                (ss[-1][1]+1) % p,
                (ss[-1][2]) % p
            ))
        elif opt == 1:
            ss.append((
                (ss[-1][0] * gta) % p,
                (ss[-1][1]) % p,
                (ss[-1][2]+1) % p
            ))
        elif opt == 2:
            ss.append((
                (pow(ss[-1][0], 2)) % p,
                (ss[-1][1]*2) % p,
                (ss[-1][2]*2) % p
            ))
        print(f"│ {i:<4} │ {ss[-1][0]:<6} │ {ss[-1][0]%3:<6} │ {ss[-1][1]:<6} │ {ss[-1][2]:<6} │")
        if k := next((k for k in range(i) if ss[k][0] == ss[-1][0]), None):
            print('└' + '─' * (len(header) - 2) + '┘')
            print(f"\nfound collision at G{i} = G{k} = {ss[-1][0]}")
            break

    # print(f"Gi = g^bi * g^(a*c_i)")
    print(f"G{k} = g^b{k} * g^(a*c_{k})")
    print(f"   = {g}^{ss[k][1]} * ({g}^a)^{ss[k][2]})")
    print(f"")
    print(f"G{i} = g^b{i} * g^(a*c_{i})")
    print(f"   = {g}^{ss[i][1]} * ({g}^a)^{ss[i][2]})")
    print(f"")
    print(f"G{i} = G{k}")
    print(f"→ {g}^{ss[i][1]}/{g}^{ss[k][1]} = ({g}^a)^{ss[k][2]}/({g}^a)^{ss[i][2]}")
    print(f"→ {ss[i][1]} - {ss[k][1]} = a * ({ss[k][2]} - {ss[i][2]}) mod {l}")
    print(f"→ {ss[i][1] - ss[k][1]} = a * ({ss[k][2] - ss[i][2]}) mod {l}")
    print(f"→ a = ({ss[i][1] - ss[k][1]}) * ({ss[k][2] - ss[i][2]})^-1 mod {l}")
    a = (ss[i][1] - ss[k][1]) * pow(ss[k][2] - ss[i][2], -1, l) % l
    print(f"→ a = {a} 🏁")

# print(group_order(3, 17))
        
pollard_rho(19, 3, 14)