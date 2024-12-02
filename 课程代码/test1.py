#our first python source file

from operator import floordiv,mod

def divide_exact(n, d):
	#通过N与D的整除与mod运算返回商和余数
	q,r = divide_exact(2024,10)
	print('Quotient', q)
	print('Remainder', r)
	return floordiv(n, d), mod(n, d)

def absolute_value(x):
	#返回x的绝对值
    if x < 0:
          return -x
    elif x == 0:
          return 0
    else:
          return x
    
# 调用absolute_value函数，传入参数
print(absolute_value(-5))  # 示例调用，检查 -5 的绝对值