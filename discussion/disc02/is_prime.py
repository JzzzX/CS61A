# def is_prime(n):
#     assert n > 1
#     i = 2
#     while i < n:
#         if n % i == 0:
#             return False
#         i = i + 1
#     return True

def is_prime(n):
    def f(i):
        if n % i == 0:
            return False
        elif i * i > n:
            return True
        else:
            return f(i + 1)
    return f(2)