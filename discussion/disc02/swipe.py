def swipe(n):
    if n < 10: # 定义递归条件
        return (n)
    else:
        print(n % 10)
        swipe(n // 10)
        print(n % 10)