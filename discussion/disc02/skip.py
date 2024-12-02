def skip_factorial(n):
    if n == 1:
        return 1 # 递归基础条件： n 为 1 ，返回 1 
    if n == 2:
        return 2 # 递归基础条件： n 为 2 ，返回 2
    else:
        return(n * skip_factorial(n - 2)) # 递归调用，跳过每隔一个数字
    

result = skip_factorial(5)
print(result)