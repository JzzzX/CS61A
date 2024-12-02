def race(x, y):
    """乌龟每分钟总是走 x 英尺，而兔子每分钟跑 y 英尺持续 5 分钟，然后休息 5 分钟。
    返回乌龟第一次追上兔子经过的分钟数。
    
    >>> race(5, 7)  # 7 分钟后，两者都走了 35 步
    7
    >>> race(2, 4) # 10 分钟后，两者都走了 20 步
    10
    """
    assert y > x and y <= 2 * x, '兔子必须比乌龟快，但不能太快'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes


def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result) None
    """
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)
        i += 1



def is_prime(n):
    """
    >>>is_prime(10)
    False
    >>>is_prime(7)
    True
    >>>is_prime(1)
    False
    """
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True



def unique_digits(n):
    """Return the number of unique digits in positive integer n.
    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    unique = 0
    while n > 0:
        last = n % 10
        n = n // 10
        if not has_digits(n, last):
            unique += 1
    return unique

# Alternate solution
def unique_digits_alt(n):
    unique = 0
    i = 0
    while i < 10:
        if has_digits(n, i):
            unique += 1
        i += 1
        return unique
    
#辅助函数 has_digits(n, k)
def has_digits(n, k):
    """Returns whether k is a digit in n.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """ 
    assert k >= 0 and k < 10 #确保k是一个有效数字（0-9）
    while n > 0:
        last = n % 10 #提取n的最后一位
        n = n // 10 #去掉最后一位
        if last == k: 
            return True
    return False

