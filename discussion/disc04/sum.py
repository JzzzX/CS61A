def sums(n, m):
    """返回所有符合条件的和为 n 的列表，它们只包含不大于 m 的正数，且没有相邻重复的数字。
    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """

    if n < 0:
        return []
    if n == 0:
        sums_to_zero = []  # 唯一能让正整数和为零的方法是空列表
        return [sums_to_zero]  # 返回一个包含和为零的方法的列表，即空列表的列表

    result = []
    for k in range(1, m + 1):
        result = result + [[k] + rest for rest in sums(n-k, m) if rest == [] or rest[0] != k]