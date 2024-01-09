import math
import builtins
from itertools import islice

ilevel = 0
psuppress = False
def indent():
    global ilevel
    ilevel += 1

def dedent():
    global ilevel
    ilevel -= 1

def suppress():
    global psuppress
    psuppress = True

def unsuppress():
    global psuppress
    psuppress = False


def print(s):
    if psuppress:
        return
    global ilevel
    id = '   ' * ilevel
    builtins.print(id + str(s).replace('\n', '\n' + id))
    # builtins.print('   ' * ilevel, end='')
    # builtins.print(*args, **kwargs)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

smallprimes = [n for n in range(2, 400) if is_prime(n)]
bigprimes = [n for n in range(10000, 100000) if is_prime(n)][::100]

def mod_inverse(x, n):
    """
    Compute the modular inverse of x modulo n using the Extended Euclidean Algorithm
    """
    print(f"computing modular inverse of {x} mod {n}")
    indent()
    assert math.gcd(x, n) == 1
    print(f"{x} is coprime to {n} ✅")
    if n == 1:
        return 0
    original_x = x
    original_n = n

    eq = []

    indent()
    while x > 1:
        q = n // x
        m = n % x
        print(f"{n} = {q} * {x} + {m}")
        eq.append((n, q, x, m))

        n = x
        x = m
    dedent()

    print("backsubstituting to solve for a and b")
    indent()
    # a, b = 0, 1
    # aa, bb = "0", "1"
    # for n, q, x, m in eq[::-1]:
    #     a, b = b, a - q * b
    #     aa, bb = f"[{bb}]", f"{aa} - ({q} * {bb})"
    #     # print(f"{m} = {n} - {q} * {x} = {a} * {original_n} + {b} * {original_x}")
    #     print(f"a = {aa} = {a}\nb = {bb} = {b}\n")
        # n, x = x, (n - q * x) % original_n

    # a, b = 1, -eq[0][1]
    # cn, cx = 1, -eq[0][1]
    cc = ((1, eq[-1][0]), (eq[-1][1], eq[-1][2]))
    for (n1, q1, x1, m1) in eq[::-1][1:]:
        print(f"1 = {cc[0][0]} * {cc[0][1]} - {cc[1][0]} * {cc[1][1]}   sub {m1} = {n1} - {q1} * {x1}")
        print(f"  = {cc[0][0]} * {cc[0][1]} - {cc[1][0]} * ({n1} - {q1} * {x1})")
        print(f"  = ({cc[0][0]} + {cc[1][0]} * {q1}) * {cc[0][1]} - {cc[1][0]} * {n1}")
        print(f"  = {cc[0][0] + cc[1][0] * q1} * {cc[0][1]} - {cc[1][0]} * {n1}")
        cc = ((-cc[1][0], n1), (-(cc[0][0] + cc[1][0] * q1), cc[0][1]))
    a, b = cc[0][0], -cc[1][0]
    # print(f"cn = {cn}, cx = {cx}")
    dedent()

    assert a * original_n + b * original_x == 1
    print(f"solved ax + bn = 1: {a} * {x} + {b} * {n} = 1, a = {a}, b = {b} ✅")

    if a < 0:
        print(f"negative a, a+n={a+original_n}")
        a += original_n
    if b < 0:
        print(f"negative b, b+n={b+original_n}")
        b += original_x

    inv = pow(original_x, -1, original_n)

    assert (original_x * inv) % original_n == 1
    print(f"modular inverse of {original_x} mod {original_n} is {inv} 🏁")
    dedent()
    return inv
    
def double_and_add(a, b):
    print(f"computing {a} * {b} using double and add algorithm")
    indent()    
    # Initialize the accumulator and the count of addition operations
    accumulator = 0
    addition_count = 0

    # Convert a and b to binary representations of the same length
    # b_binary = bin(b)[2:].zfill(len(bin(a)[2:]))
    # # a_binary = bin(a)[2:]
    b_binary = bin(b)[2:]
    

    # Display the binary forms of a and b
    print(f"b = {b} = {b_binary}\n")

    # Print the header for the table
    header = f"│ {'i':<6} │ {'2^i':<10} │ {'a*2^i':<10} │ {'b bit':<6} │ {'Accumulator':<12} │ {'Operation':<24} │"
    print('┌' + '─' * (len(header) - 2) + '┐')
    print(header)
    print('├' + '─' * (len(header) - 2) + '┤')

    # Iterate over each bit in the binary representation of b
    for i, bit in enumerate(b_binary[::-1]):
        step = i
        if step > 0:
            operations = ["Double a"]
            addition_count += 1
        else:
            operations = []
        two_i = 2 ** step
        a_doubled = a * two_i

        # If the bit is 1, add 'a' to the accumulator and increment the addition count
        if bit == '1':
            accumulator += a_doubled
            addition_count += 1  # One for doubling 'a', one for addition to accumulator
            operations += ["Add to Accum"]

        # Print the current step details
        print(f"│ {step:<6} │ {two_i:<10} | {a_doubled:<10} │ {bit:<6} │ {accumulator:<12} │ {', '.join(operations):<24} │")

    # Print the closing line of the table
    print('└' + '─' * (len(header) - 2) + '┘')

    # Print the final result and the count of addition operations
    assert accumulator == a * b
    print(f"\nResult: {accumulator}")
    print(f"Total addition operations: {addition_count}")
    dedent()
    return accumulator


def square_and_multiply(base, exponent, modulus=None):
    print(f"Computing {base} ^ {exponent} using square and multiply algorithm")
    indent()

    # Initialize the accumulator and the count of multiplication operations
    accumulator = 1
    multiplication_count = 0

    # Convert the exponent to binary representation
    exponent_binary = bin(exponent)[2:]

    # Display the binary form of the exponent
    print(f"exponent = {exponent} = {exponent_binary}\n")

    # Print the header for the table
    header = f"│ {'i':<6} │ {'2^i':<10} │ {'Base^2^i':<12} │ {'Exp bit':<8} │ {'Accumulator':<12} │ {'Operation':<24} │"
    print('┌' + '─' * (len(header) - 2) + '┐')
    print(header)
    print('├' + '─' * (len(header) - 2) + '┤')

    # Iterate over each bit in the binary representation of the exponent
    base_squared = base
    for i, bit in enumerate(exponent_binary[::-1]):
        step = i

        if step > 0:
            operations = [f"({base_squared}^2={base_squared**2}) mod {modulus} = {pow(base_squared, 2, modulus)}" if modulus else f"{base_squared}^2={base_squared**2}"]
            base_squared = pow(base_squared, 2, modulus)
            multiplication_count += 1
        else:
            operations = []

        # If the bit is 1, multiply the accumulator with the base
        if bit == '1':
            operations += [
                f"({accumulator}*{base_squared}={accumulator*base_squared}) mod {modulus} = {(accumulator*base_squared)%modulus}"
                if modulus else f"{accumulator}*{base_squared}={accumulator*base_squared}"]
            accumulator *= base_squared
            if modulus:
                accumulator %= modulus
            multiplication_count += 1

        # Print the current step details
        print(f"│ {step:<6} │ {2 ** step:<10} │ {base_squared:<12} │ {bit:<8} │ {accumulator:<12} │ {', '.join(operations):<24} ")

    # Print the closing line of the table
    print('└' + '─' * (len(header) - 2) + '┘')

    # Print the final result and the count of multiplication operations
    assert accumulator == pow(base, exponent, modulus)
    print(f"\nResult: {accumulator}")
    print(f"Total multiplication operations: {multiplication_count}")
    dedent()
    return accumulator

# for tt in range(t.n):
#     if t.encrypt(tt, pk[0]) == 94755:
#         print(tt)
# mod_inverse(11, 17)

def prime_factors(n, return_powers=False, return_power_pairs=False):
    factors = []
    N = n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n ** 0.5 + 1), 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    powers = [(f, factors.count(f)) for f in set(factors)]
    # print(f"{N} = {' * '.join([f'{f}^{p}' for f, p in powers])}")
    if return_powers:
        return [b**e for b,e in powers]
    elif return_power_pairs:
        return [(b,e) for b,e in powers]
    return factors

def group_order(g, p):
    for i in range(1, p):
        if pow(g, i, p) == 1:
            return i
    assert False, "no order found"
    # phi = p - 1
    # factors = prime_factors(phi)
    # print(f"phi = {phi}")
    # print(f"factors = {factor

def is_generator(g, p):
    # print(f"{g, p}")
    phi = p - 1
    factors = prime_factors(phi)

    for f in factors:
        if pow(g, phi//f, p) == 1:
            # print(f"not a generator: {g}^{phi//f} mod {p} = 1")
            return False
    
    return True
    # if all(pow(g, phi//f, p) != 1 for f in factors):
    #     print("cand")
    #     return True
    
    # return False

def find_generators(p):
    assert is_prime(p)
    for g in range(2, p):
        if is_generator(g, p):
            yield g

def solve_modular_system(equations, modulo):
    def add_row(row1, row2, factor):
        return [(a + factor * b) % modulo for a, b in zip(row1, row2)]

    def scale_row(row, factor):
        return [a * factor % modulo for a in row]

    def get_inv(num):
        return pow(num, -1, modulo)

    n = len(equations)
    matrix = [eq[1] + [eq[0]] for eq in equations]

    # Forward elimination
    for i in range(n):
        inv = get_inv(matrix[i][i])
        matrix[i] = scale_row(matrix[i], inv)
        for j in range(i + 1, n):
            matrix[j] = add_row(matrix[j], matrix[i], -matrix[j][i])

    # Backward substitution
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            matrix[j] = add_row(matrix[j], matrix[i], -matrix[j][i])

    return [row[-1] for row in matrix]

# # Example usage:
# modulo = 7
# equations = [(3, [1, 2]), (2, [3, 1])]
# print(solve_modular_system(modulo, equations))

mod_inverse(18, 65)