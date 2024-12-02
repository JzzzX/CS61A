def hailstone(n):
    print(n)
    if n == 1:
        return 
    elif n % 2 == 0:
        return hailstone(n // 2)
    else:
        return hailstone(n * 3 + 1)
    