# accumulate.py

def accumulate(fuse, start, n, term):
    """Return the result of fusing together the first n terms in a sequence 
    and start.  The terms to be fused are term(1), term(2), ..., term(n). 
    The function fuse is a two-argument commutative & associative function.
    """
    result = start
    for i in range(1, n + 1):
        result = fuse(result, term(i))
    return result

#alternative solution 1
def accumulate(fuse, start, n, term):
    total, k = start, 1
    while k <= n:
        total, k = fuse(total, term(k)), k + 1
    return total

#alternative solution 2
def accumulate_reverse(fuse, start, n, term):
    total, k = start, n
    while k >= 1:
        total, k = fuse(total, term(k)), k - 1
    return total


# 示例函数 add 和其他帮助函数
def add(x, y):
    return x + y

def identity(x):
    return x

def square(x):
    return x * x

def mul(x, y):
    return x * y