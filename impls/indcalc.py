from utils import group_order, is_prime, indent, dedent, prime_factors, print, is_generator, smallprimes, bigprimes, find_generators, mod_inverse, solve_modular_system, suppress, unsuppress
import math


class IndexCalculus:
    def __init__(self, p, g, factor_base):
        print(f"initializing index calculus with p = {p}, g = {g}, factor_base = {factor_base}")
        indent()
        assert is_prime(p)
        print(f"{p} is prime ✅")
        assert is_generator(g, p)
        print(f"{g} is generator of Z_{p} ✅")

        self.p = p
        self.g = g
        self.base_logs = []
        # self.gta = gta
        self.factor_base = factor_base
        self.compute_base_logs()
        dedent()

    def solve_set(self, equations):
        coeffs = [
            [sum(p[1] for p in e[1] if p[0] == fac) for fac in self.factor_base]
            for e in equations
        ]
        system = list(zip((e[0] for e in equations), coeffs))
        print(f"attempting to solve simultaneous equations {system}")
        try:
            solutions = solve_modular_system(system, self.p-1)
            return solutions
        except:
            # print("solution not found")
            return None

    def compute_base_logs(self):
        print(f"computing logs for p = {self.p}, g = {self.g}, base factors = {self.factor_base}")
        indent()
        equations = []
        # while len(equations) < len(self.factor_base):
        for j in range(1, 40):
        # for i in range(20):
            gtj = pow(self.g, j, self.p)
            subfacs = prime_factors(gtj, return_power_pairs=True)
            if any(f[0] not in self.factor_base for f in subfacs):
                continue
            print(f"found {self.g}^{j} mod {self.p} = {gtj} = {' * '.join(f'{f[0]}^{f[1]}' for f in subfacs)}")
            print(f"  → {j} = {' + '.join(f'{f[1]} * log_{self.g}({f[0]})' for f in subfacs)} mod {self.p-1}\n")
            equations.append((j, subfacs))
            if len(equations) >= len(self.factor_base):
                if sols := self.solve_set(equations):
                    print(f"solution found: {', '.join(f'log_{self.g}({b}) = {s}' for b, s in zip(self.factor_base, sols))} (mod {self.p-1}) 🏁")
                    self.base_logs = dict(zip(self.factor_base, sols))
                    break
                else:
                    print(f"unable to find solution, removing first equation and retrying ❌")
                    equations.pop(0)
        dedent()

    def compute_log(self, gta):
        assert self.base_logs
        print(f"computing log_{self.g}({gta}) mod {self.p} with index calculus")
        indent()
        print(f"using base factors {', '.join(f'log_{self.g}({b}) = {s}' for b, s in self.base_logs.items())}")
        for j in range(20):
            gj_gta = pow(self.g, j, self.p) * gta % self.p
            subfacs = prime_factors(gj_gta, return_power_pairs=True)
            if any(f[0] not in self.factor_base for f in subfacs):
                print(f"{self.g}^{j} * {gta} = {pow(self.g, j)} * {gta} = {gj_gta} mod {self.p} = {' * '.join(f'{f[0]}^{f[1]}' for f in subfacs)} ❌")
                continue
            break
        print(f"\n{self.g}^{j} * {gta} = {pow(self.g, j)} * {gta} = {gj_gta} mod {self.p} = {' * '.join(f'{f[0]}^{f[1]}' for f in subfacs)} ✅")
        # print(f"found {gta} * {self.g}^{j} mod {self.p} = {gj_gta} = {' * '.join(f'{f[0]}^{f[1]}' for f in subfacs)}")
        print(f"  → {j} + log_{self.g}({gta}) = {' + '.join(f'{f[1]} * log_{self.g}({f[0]})' for f in subfacs)} mod {self.p-1}")
        print(f"  → {j} + log_{self.g}({gta}) = {' + '.join(f'{f[1]} * {self.base_logs[f[0]]}' for f in subfacs)} mod {self.p-1}")
        print(f"  → log_{self.g}({gta}) = {' + '.join(f'{f[1]*self.base_logs[f[0]]}' for f in subfacs)} - {j} mod {self.p-1}")
        a = (sum(f[1]*self.base_logs[f[0]] for f in subfacs) - j)
        print(f"  → log_{self.g}({gta}) = {a} = {a % (self.p-1)} mod {self.p-1} 🏁")
        return a % (self.p-1)
            # return sum(s * log for (_, s), (_, log) in zip(subfacs, self.base_logs)) % (self.p-1)
        # solve_equations(zip((e[0] for e in equations), coeffs), self.p-1)
        # l = group_order(self.g, self.p)
        # print(f"l = order of {self.g} in Z_{self.p} = {l}")
        # print(f"factor base = {self.factor_base}")
        # print(f"computing logs for primes in factor base")
        # logs = {}
        # for p in self.factor_base:
        #     print(f"computing log for {p}")
        #     indent()
        #     logs[p] = self.log(p)
        #     dedent()
        # print(f"logs = {logs}")
        # dedent()
        # return logs

# ix = IndexCalculus(107, 17, [2,3,5])
ix = IndexCalculus(19, 14, [2,3,5])
# ix.compute_log(91)