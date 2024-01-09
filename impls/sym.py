from sympy import Mod, Sum, symbols, solve, Eq
def solve_equations_mod(equations, mod):
    syms = symbols(f'c0:{len(equations)}')
    eqs = [
        Mod(sum(c * s for c, s in zip(coeffs, syms)) - res, mod)
        for res, coeffs in equations
    ]
    print(eqs)
    sol = solve(eqs, syms)
    print(sol)

# a, b, c = symbols('a b c')
# print(solve(Mod(b + 2 * c - 2, 106)))

# solve_equations_mod([(2, [0, 1, 2]), (6, [0, 4, 0]), (9, [2, 0, 1])], 106)
solve_equations_mod([(2, [0, 1, 2]), (6, [0, 4, 0]), (9, [2, 0, 1]), (11, [1, 0, 0])], 106)

# sol = solve(Mod(4 * b - 6, 106))
# print(sol)