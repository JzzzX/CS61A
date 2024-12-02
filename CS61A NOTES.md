# CS61A NOTES

## Lectures





### Lecture 1 Welcome

**课程官网：** https://cs61a.org/

**CS自学社区课程网站**：https://www.learncs.site/docs/curriculum-resource/cs61a/syllabus

**B站课程精翻视频：**
【【完结】【CS61A精翻双语·英文原声】伯克利大学《计算机程序的结构与解释》(2024)】 https://www.bilibili.com/video/BV1sy411z7nA/?p=2&share_source=copy_web&vd_source=d1b42a139a040d437be1d5d26c2ded3f

**SCIP在线课本**：https://composingprograms.netlify.app



课程表进度（略）：见网站

lecture1：课程简介和一些python基础





### Lecture 2 Functions

lecture2主要讲解编程要素，新函数的定义。

#### **编程要素**

1.表达式；

2.调用表达式；

3.导入库函数:

4.名称与环境&求解嵌套表达式

5.非纯函数print

**纯函数（Pure functions）**：函数有一些输入（参数）并返回一些输出（调用返回结果）。

```python
>>> abs(-2)
2
```

可以将内置函数 `abs` 描述为接受输入并产生输出的小型机器。

![function_abs](https://composingprograms.netlify.app/sicp/function_abs.png)

**非纯函数（Non-pure functions）**：除了返回值外，调用一个非纯函数还会产生其他改变解释器和计算机的状态的副作用（side effect）。一个常见的副作用就是使用 `print` 函数产生（非返回值的）额外输出。

```python
>>> print(1, 2, 3)
1 2 3
```

虽然  `print` 和  `abs` 在这些例子中看起来很相似，但它们的工作方式基本不同。`print` 返回的值始终为 `None`，这是一个不代表任何内容的特殊 Python 值。而交互式 Python 解释器并不会自动打印 `None` 值，所以 `print` 函数的额外输出就是它的副作用。

![function_print](https://composingprograms.netlify.app/sicp/function_print.png)

#### 定义新函数

**如何定义函数**：函数定义包含 `def` 语句、`<name 函数名>` 和一个以逗号分隔的 `<formal parameters 形式参数>` 列表，然后是一个被称为函数体的 `return` 语句，它指定了调用函数时要计算的表达式，也就是函数的 `<return expression 返回表达式>` ：

```python
def <name>(<formal parameters>):
    return <return expression>
```



**环境图** 显示了当前环境中的绑定，还有名称和值的绑定  [Online Python Tutor](https://www.composingprograms.com/tutor.html)





### Lecture 3 Control

#### Multiple Enviroments

Python部运算符

1.真除法与整除法

```python
>>> from operator import truediv, floordiv
>>> truediv(2024,10)  #aka: 2024 / 10
202.4
>>> floordiv(2024,10) #aka: 2024 // 10
202
```

2.mod运算符（取余数）

```python
>>> from operator import mod
>>> mod(2024,10) #aka : 2024 % 10
4

#符号 % : 当 a % b = 0时表示a能被b整除
```



```python
from operator import floordiv,mod

def divide_exact(n, d):
	>>>q,r = divide_exact(2024,10)
    >>>q
    202
    >>r
    4
	print('Quotient', q)
	print('Remainder', r)
	return floordiv(n, d), mod(n, d)
```

 

#### 条件语句

```python
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
```



#### 迭代

（略）



### Lecture 4 Higher-Order Functions

#### 斐波那契数列（fib）

在此数列的构造函数中，从0开始要比从1开始更好，因为这样可以更精确计算到第0位数

```python
def fib(n):
    pred, curr = 1, 0
    k = 0
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
        return curr 
```



#### Control

```python
def if_(c, t, f):
    if c:
    	return t
	else:
    	return f
    
from math import sqrt
def  real_sqrt(x):
    return if_(x >= 0, sqrt(x), 0)
    
#调用表达式不允许跳过对调用表达式的部分进行评估，在函数被调用前，所有部分都会被进行评估；
#所以这与控制语句（if else）不同，控制语句会进行选择与跳过
#所以我们定义的函数在运行 real_sqrt(-16)这样的负数时就会报错

```



#### Control Expression

and & or

**and 连接符**

**返回值**：返回第一个 False 条件，如果没有 False，则返回最后一个 True。

​	•	**表达式结果**：

​	•	True and True -> True

​	•	True and False -> False

​	•	False and True -> False

​	•	False and False -> False



**or 连接符**

**返回值**：返回第一个 True 条件，如果没有 True，则返回最后一个 False。

​	•	**表达式结果**：

​	•	True or True -> True

​	•	True or False -> True

​	•	False or True -> True

​	•	False or False -> False





#### Higher-Order Functions

https://composingprograms.netlify.app/1/6#_1-6-1-作为参数的函数

两条原则：

1. 函数应该只做一件明确的事（复杂的文档注释说明函数做得太多）
2. DRY(Don’t Repeat Yourself)，不要重复，出现重复的代码块建议重构（refactoring），将重复代码块替换成一个单独的函数





### Lecture 5 Enviroments



#### Enviroments for Higher-order-Functions

在python tutor中可以查看python函数的环境图



#### 嵌套定义的环境

Nested def，嵌套的def函数语句

```python
def compose1(f, g):
    def h(x):
        return f(g(x))
    return h
```



#### LocalNames



#### 函数组合

与嵌套定义一同组合的多个函数

```python
# The Environment Diagram for Function Composition

def square(x):
    return x * x

def make_adder(n):
    def adder(k):
        return k + n
    return adder

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

```



#### Lambda Expressions

```python
square = lambda x: x * x

#这是另一个表达式，计算结果是一个函数。
#lambda 表达式中没有 return 关键字。
#定义了一个函数，形式参数为 x，返回值是 x * x
#必须是单个表达式
```

**Lambda 表达式**在 Python 中并不常见，但在某些情况下很重要。

**Lambda 表达式**中不能包含任何语句！



#### Function Currying

**柯里化**（Curry）是一种将具有多个参数的函数转换为一系列嵌套函数的技术，每个嵌套函数只接受一个参数。这意味着，柯里化函数将分解一个多参数函数，使得它可以被逐步调用，每次调用传入一个参数。

```python
f(a, b, c) -> f(a)(b)(c)
```

```python
def curry_function(a):
    def step1(b):
        def step2(c):
            return a + b + c
        return step2
    return step1

# 调用柯里化函数
result = curry_function(1)(2)(3)
print(result)  # 输出 6

```





### Lecture7 Functional Abstraction

#### Lambda Function Enviroments

```python
a = 1
def f(g):
    a = 2
    return lambda y: a * g(y)
f(lambda y: a + y)(a)

```

#### Return

嵌套/高阶函数，逻辑简化

#### Abstraction & Choosing Names



### Lecture8 Function Examples

#### Review Examples

`delay funtion` : 这是一个接受任何参数并返回一个函数的函数，该返回的函数会返回这个参数。

```python
def delay(arg):
    print("delayed")
    def g():
        return arg
    return g

```

```python
delay(delay())()(6)
计算结果: 6
交互式输出:
delayed
delayed
6

print(delay(print())()(4))
计算结果: None
交互式输出:
delayed
4
None
```



`Pirate Funtion`

```python
def pirate(arggg):
    print("matey")
    def plunder(arggg):
        return arggg
    return plunder


add(pirate(3)(square)(4), 1)
计算结果: 17
交互式输出:
Matey
17

pirate(pirate(pirate))(5)(7) #5作为整数不能被调用，只有函数可以被调用
计算结果: Error
交互式输出:
Matey
Matey
Error
```



`Horse Mask`

<img src="cs61a/截图/截屏2024-09-26 15.34.36.png" style="zoom:50%;" />



#### 实现函数

多想，多尝试不同的实现策略吧！



#### Decrator 装饰器

在 Python 中，**装饰器（decorator）** 是一种函数，用于修改或增强其他函数或方法的行为。它的主要用途是**在不改变函数源代码**的情况下，为函数或方法添加额外的功能。

装饰器本质上是一个**高阶函数**，它接收一个函数作为参数，并返回一个新的函数或原函数，来增强其功能。

```python
def trace1(fn):
    """Returns a version of fn that first prints before it is called."""
    # fn 是一个接收一个参数的函数
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced

@trace1
def square(x):
    return x * x

@trace1
def sum_squares_up_to(n):
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k), k + 1
    return total

```

使用 `@trace1` 装饰器的代码：

```python
@trace1
def triple(x):
    return 3 * x
```

与以下高阶函数代码是完全等价的：

```python
def triple(x):
    return 3 * x

triple = trace1(triple)
```





### Lecture9 Recursion(递归)

#### 递归函数

SICP 1.7: https://composingprograms.netlify.app/1/7#_1-7-1-递归函数剖析

<img src="cs61a/截图/截屏2024-10-01 14.10.50.png" style="zoom:50%;" />



#### 递归的信仰之跃

```python
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
```

 `fact` 实现正确吗？

1. 验证基础情况（base case）。
2. 将 `fact` 视为一个功能抽象（functional abstraction）。
3. 假设 `fact(n-1)` 是正确的。
4. 在假设 `fact(n-1)` 正确的前提下，验证 `fact(n)` 的正确性。

運常我们假设一个函数对于我们在递归调用中使用的更简单的情况是正确定义的，然后验证如果是这样，那么整个问题对于我们所陈述的问题就是正确定义的。



Recursive Leap of Faith (递归的信仰之跃) 递归与数学归纳法很像。编写递归程序时，一个base case规定边界条件、一个recursive case规定递归操作。在recursive case中，我们信任这个函数会给出正确的n返回值，再利用返回值去构建n+1的返回值。这种信任被称为"Recursive Leap of Faith"。同样当我们理解、修改递归程序时，不应该试图推演递归调用，而是直接信任它，并在其基础上修改从n到n+1的操作，leave the hard work to the computer。 当然，一定要推演的话可以推演一个递归深度浅的例子。



#### 相互递归

https://composingprograms.netlify.app/1/7#_1-7-2-互递归

Luhn sum算法——用于计算信用卡号的校验和



#### 递归&迭代

将迭代转换为递归，迭代是递归的特例。

**思路**：迭代的状态可以作为参数传递。

```python
def sum_digits_iter(n):
    digit_sum = 0
    while n > 0:
        n, last = split(n)
        digit_sum = digit_sum + last
    return digit_sum
```

```python
def sum_digits_rec(n, digit_sum):
    if n == 0:
        return digit_sum
    else:
        n, last = split(n)
        return sum_digits_rec(n, digit_sum + last)
```



### Lecture10 Tree Recursion

#### 递归调用的顺序

两种 Cascade 的定义

```python
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)
```

```py
def cascade(n):
    print(n)
    if n >= 10:
        cascade(n // 10)
        print(n)
```

如果两个实现同样清晰，那么通常较短的更好。
在这种情况下，较长的实现更清晰（至少对我来说）。
在学习编写递归函数时，应首先写出基础情况。
两者都是递归函数，尽管只有第一个具有典型的结构。

<img src="cs61a/截图/截屏2024-10-01 14.10.50.png" style="zoom:50%;" />



#### Tree Recurison

https://composingprograms.netlify.app/1/7#_1-7-4-树递归

斐波那契数列为典型例子来展开

```py
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
```



#### 例：计算分区

https://composingprograms.netlify.app/1/7#_1-7-5-示例-分割数

![](cs61a/截图/截屏2024-10-01 17.34.09.png)

<img src="cs61a/截图/截屏2024-10-01 17.42.14.png" alt="截屏2024-10-01 17.42.14" style="zoom:50%;" />





### Lecture11 Sequence

#### List

https://composingprograms.netlify.app/2/3#_2-3-1-列表

列表是从0开始统计



#### For Statements

```py
def count(s, value):
    total = 0
    for element in s:
        if element == value:
            total = total + 1
    return total
```

可以在for语句头部直接进行序列解包

```py
>>> pairs = [(1, 2), (2, 2), (3, 2), (4, 4)]
>>> same_count = 0

>>> for x, y in pairs:
...     if x == y:
...         same_count = same_count + 1

>>> same_count
2
```



#### Ranges

Ranges是序列，但不是列表

```py
list(range(-2, 2))  # 输出 [-2, -1, 0, 1]
list(range(4))      # 输出 [0, 1, 2, 3]
```



#### 列表推导

```py
def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

>>> divisors(8)
[1, 2, 4]
```



### Lecture12 Containers

#### Slicing 切片

**列表切片 `odds[1:3]`**

```py
>>> odds = [3, 5, 7, 9, 11]
>>> list(range(1, 3))
[1, 2]
>>> [odds[i] for i in range(1, 3)]
[5, 7]

>>> odds[1:3]
[5, 7]
>>> odds[:3]
[3, 5, 7]
>>> odds[1:]
[5, 7, 9, 11]
>>> odds[:]
[3, 5, 7, 9, 11]
```

#### 序列聚合

```py
序列聚合（Sequence Aggregation）
一些内置函数可以接受可迭代对象作为参数，并将它们聚合为一个值。

sum(iterable[, start]) -> value
返回一个数字可迭代对象的和（不包括字符串）加上参数 start 的值（默认为 0）。
当可迭代对象为空时，返回 start。

max(iterable[, key=func]) -> value
max(a, b, c, ...[, key=func]) -> value
如果只有一个可迭代对象作为参数，则返回其中的最大值。
如果有两个或更多参数，则返回最大的那个参数。

all(iterable) -> bool
如果可迭代对象中的所有值 x 使 bool(x) 为 True，则返回 True。
如果可迭代对象为空，返回 True。
```

#### Strings

```py
>>> city = 'Berkeley'
>>> len(city)
8
>>> city[3]
'k'

>>> 'here' in "Where's Waldo?"
True
>>> 234 in [1, 2, 3, 4, 5]
False
>>> [2, 3, 4] in [1, 2, 3, 4, 5]
False
```

#### Dictionary

```py
def index(keys, values, match):
    """返回一个从键 k 到包含使 match(k, v) 为 True 的值 v 的列表的字典。

    >>> index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)
    {7: [35, 42, 49], 9: [36, 45], 11: [33, 44]}
    """
    return {k: [v for v in values if match(k, v)] for k in keys}
```



### Lecture13 Data Abstraction

https://composingprograms.netlify.app/2/2#_2-2-数据抽象



### Lecture14 Trees

https://composingprograms.netlify.app/2/3#_2-3-6-树

```py
def fib_tree(n):
    if n <= 1:
        return tree(n)  # 基本情况：如果n是0或1，返回一个以n为标签的树
    else:
        left = fib_tree(n-2)   # 递归生成左子树，左子树是fib(n-2)
        right = fib_tree(n-1)  # 递归生成右子树，右子树是fib(n-1)
        return tree(label(left) + label(right), [left, right])  # 新树的标签是左、右子树的标签和

    
def count_leaves(t):
    if is_leaf(t):  # 如果 t 是叶子节点
        return 1    # 叶子节点计为1
    else:
        return sum([count_leaves(b) for b in branches(t)])  # 否则递归地计算所有子树的叶子数之和

    
def print_tree(t, indent=0):
    print(' ' * indent + str(label(t)))  # 根据缩进打印节点的标签
    for b in branches(t):  # 遍历所有子树
        print_tree(b, indent + 1)  # 对每个子树增加缩进后递归打印

```



递归打印树的路径和或累加字符串

`print_sums(t, so_far)`

`print_sums(t, so_far)` 函数用于递归遍历树，计算从根节点到每个叶子节点的累加值或字符串，并在叶子节点时打印累加的结果。

 函数结构：

```python
def print_sums(t, so_far):
    so_far = so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)
```



```python
def count_paths(t, total):
    """
    返回树 t 中从根节点到任何节点，路径和等于 total 的路径数。
    """
    # 如果当前节点的标签等于 total，则找到一条路径
    if label(t) == total:
        found = 1
    else:
        found = 0

    # 递归遍历子树，累加找到的路径数
    return found + sum([count_paths(b, total - label(t)) for b in branches(t)])
```



### Lecture15 Mutanility

https://composingprograms.netlify.app/2/4#_2-4-可变数据



### Lecture16 Iterators(迭代)

https://composingprograms.netlify.app/4/2#_4-2-隐式序列



### Lecture17 Generators & Yield

https://composingprograms.netlify.app/4/2#_4-2-5-生成器和-yield-语句

生成器 Yield——生成值而非返回值，节省内存/简化代码

```py
def partitions(n, m):
    """Yield partitions."""
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in partitions(n - m, m):
            yield p + ' + ' + str(m)
        yield from partitions(n, m - 1)
```



### Lecture18 Objects

https://composingprograms.netlify.app/2/5#_2-5-面向对象编程





### Lecture19 Attributes

https://composingprograms.netlify.app/2/5#_2-5-4-类属性



### Lecture20 Inheritance

https://composingprograms.netlify.app/2/5#_2-5-5-继承

 设计继承 (Designing for Inheritance)

- 不要重复自己，使用已有的实现。（Don't repeat yourself; use existing implementations.）

- 已被重写的属性仍然可以通过类对象访问。（Attributes that have been overridden are still accessible via class objects.）

- 尽可能在实例上查找属性。（Look up attributes on instances whenever possible.）

	```py
	class CheckingAccount(Account):
	    """
	    一个收取取款手续费的银行账户。
	    A bank account that charges for withdrawals.
	    """
	    withdraw_fee = 1  # 取款手续费
	    interest = 0.01  # 利率
	
	    def withdraw(self, amount):
	        # 调用父类的 withdraw 方法，并加上手续费
	        return Account.withdraw(self, amount + self.withdraw_fee)
	    
	    """
	属性查找在基类上进行（Attribute look-up on base class）：此处通过 Account.withdraw() 调用父类的方法，避免了重新实现。
	
	优选使用实例属性 self.withdraw_fee 而不是类属性（Preferred to CheckingAccount.withdraw_fee to allow for specialized accounts）：
	通过使用实例属性 self.withdraw_fee，允许不同账户实例具有不同的手续费设置，从而实现更加灵活的继承设计。
	    """
	```

	

继承和属性查找

```python
class A:
    z = -1
    def f(self, x):
        return B(x-1)

class B(A):
    n = 4
    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y+1)

class C(B):
    def f(self, x):
        return x

a = A()
b = B(1)
b.n = 5
```



<img src="截屏2024-10-16 19.18.15.png" style="zoom:50%;" />



### Lecture21 Representation

https://composingprograms.netlify.app/2/7#_2-7-对象抽象



### Lecture22 Composition

使用python 对象实现‘链表’

```py
"""
这个函数的目的是将值 v 插入到链表 s 中，保持链表的元素是按从小到大的顺序排列的。链表中的每个节点有 first 和 rest 属性。
"""

def add(s, v):
    """Add v to s, returning modified s."""
    assert s is not List.empty  # 确保 s 不是空链表，防止意外情况发生

    # 如果 v 小于 s.first
    if s.first > v:
        # 当 v 小于链表的第一个值时，v 需要插入到头部
        s.first, s.rest = v, Link(s.first, s.rest)
        # 解释：将当前链表的值推到后面，将 v 作为新的第一个节点
        # 比如，如果 s 是 Link(1, Link(3, Link(5)))
        # 现在 v 是 0，则新的链表变为 Link(0, Link(1, Link(3, Link(5))))
        
    # 如果当前值小于 v 并且 rest 是空的
    elif s.first < v and empty(s.rest):
        # 解释：如果 rest 为空，说明我们到达了链表的尾部
        # 所以直接在链表的末尾插入 v
        s.rest = Link(v)
        # 比如，如果 s 是 Link(1, Link(3, Link(5)))，v 是 6
        # 那么链表会变成 Link(1, Link(3, Link(5, Link(6))))
    
    # 如果当前值小于 v，且后面还有元素（rest 不是空的）
    elif s.first < v:
        # 递归调用，继续处理后面的链表
        # s.rest 表示链表的下一个节点，因此我们需要在 s.rest 中插入 v
        s.rest = add(s.rest, v)
        # 比如，如果 s 是 Link(1, Link(3, Link(5)))，v 是 4
        # 递归调用会去处理 Link(3, Link(5))，最终插入 4 后，链表变成
        # Link(1, Link(3, Link(4, Link(5))))

    return s
```



```py
"""
修剪树（Pruning Trees）的代码和示例。其目的是从树结构中移除某些子树，基于子树根节点的标签（label）是否等于给定的值 n。让我们仔细分析这个 prune 函数的逻辑。
"""

def prune(t, n):
    """Prune all sub-trees whose label is n."""
    
    # 保留所有标签不等于 n 的子树
    t.branches = [b for b in t.branches if b.label != n]
    
    # 对每个剩余的子树递归调用 prune，继续修剪
    for b in t.branches:
        prune(b, n)

```



### Lecture23 Efficiency

https://composingprograms.netlify.app/2/8#_2-8-%E6%95%88%E7%8E%87 效率



### Lecture24&25 Decomposition & Data Examples

模块化设计





### Lecture28&29 Scheme &SchemeLists

https://composingprograms.netlify.app/3/2#_3-2-%E5%87%BD%E6%95%B0%E5%BC%8F%E7%BC%96%E7%A8%8B 函数式编程

```scheme
;;; non-empty subsets of a list `s`
;;; 定义过程nonempty-subsets：返回列表`S`的所有非空子集
(define (nonempty-subsets s)
  (if (null? s)                ; 基准条件：如果列表`s`为空，则返回`nil`，表示没有非空子集
      nil
      (let ((rest (nonempty-subsets (cdr s)))) ; 递归调用，获取`s`的尾部部分(去掉第一个元素)的非空子集
        (append rest                           ; 使用append连接以下三部分:
                (map (lambda (t)               ; 对`rest`中的每个子集`t`，将`(car s)`加入到子集`t`中
                       (cons (car s) t))
                     rest)                     ; map的结果是将`car s`添加到每个`rest`子集的开头
                (list (list (car s)))))))      ; 将`car s`作为一个单独的子集，构造成单元素子集`(car s)`

;;; Example: nonempty-subsets '(1 2) => '((2) (1 2) (1))
;;; 解释：
;;; - 首先递归处理`(cdr s)`的非空子集，这里是`'(2)`，其非空子集是`'((2))`
;;; - 然后对`(car s)`=`1`，将`1`加到`(2)`中，结果是`(1 2)`
;;; - 最后再构造单元素子集`(1)`
;;; - 合并所有部分：`'((2) (1 2) (1))`


;;; Define even-subsets, which returns non-empty subsets of integer list `s` 
;;; where the sum of elements in each subset is even.
;;; 定义过程even-subsets：返回整数列表`s`中所有元素和为偶数的非空子集
(define (even-subsets s)
  (filter (lambda (s)                ; 过滤列表`S`的非空子集，`lambda`用于检查子集是否满足条件
            (even? (apply + s)))     ; 使用`apply`将子集中的所有元素相加，如果和为偶数，则保留该子集
          (nonempty-subsets s)))     ; 调用nonempty-subsets，生成`s`的所有非空子集作为`filter`的输入

;;; Example: even-subsets '(1 2) => '((2))
;;; 解释：
;;; - `nonempty-subsets '(1 2)` => '((2) (1 2) (1))`
;;; - 计算子集的元素和:
;;;   - (2) 的和是 2（偶数），保留。
;;;   - (1 2) 的和是 3（奇数），丢弃。
;;;   - (1) 的和是 1（奇数），丢弃。
;;; - 最终结果是：`'((2))`

```



### Lecture30 Calculator

3.4 组合语言的解释器https://composingprograms.netlify.app/3/4#_3-4-%E7%BB%84%E5%90%88%E8%AF%AD%E8%A8%80%E7%9A%84%E8%A7%A3%E9%87%8A%E5%99%A8



### Lecture31 Interpreters

3.5 抽象语言的解释器https://composingprograms.netlify.app/3/5#_3-5-%E6%8A%BD%E8%B1%A1%E8%AF%AD%E8%A8%80%E7%9A%84%E8%A7%A3%E9%87%8A%E5%99%A8





### Lecture33 Programs as Data & Macros

Macros：宏，一种编程语言结构，允许定义一个函数，该函数生成程序代码，并替换对宏函数的调用

































## Lab

借助python tutor梳理代码大有裨益：

python tutor：https://pythontutor.com/cp/composingprograms.html#mode=edit



### lab0 getting started

根据lab00的指示，完成终端（windows powershell / Mac terminal）、python、编辑器（vscode）安装与使用，文件整理和作业。



https://www.learncs.site/docs/curriculum-resource/cs61a/lab/lab00

Lab 0: Getting Started (Mac/Linux Setup): https://cs61a.org/articles/setup-mac/

作业提交使用ok系统，教程：https://cs61a.org/articles/using-ok/#signing-in-with-ok

UNIX tutorial: https://cs61a.org/articles/unix/

OK系统本地测试：

```powershell
cd ~/Desktop/ca61a/lab/lab00 
python3 ok --local
```





