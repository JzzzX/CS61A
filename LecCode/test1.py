#our first python source file

from operator import floordiv,mod

def divide_exact(n, d):
    return floordiv(n, d), mod(n, d)
q,r = divide_exact(2024,10)
print('Quotient', q)
print('Remainder', r)
