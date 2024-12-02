class Transaction:
    def __init__(self, id, before, after):
        self.id = id
        self.before = before
        self.after = after

    def changed(self):
        """Return whether the transaction resulted in a changed balance."""
        "*** YOUR CODE HERE ***"
        return self.before != self.after

    def report(self):
        """Return a string describing the transaction.

        >>> Transaction(3, 20, 10).report()
        '3: decreased 20->10'
        >>> Transaction(4, 20, 50).report()
        '4: increased 20->50'
        >>> Transaction(5, 50, 50).report()
        '5: no change'
        """
        msg = 'no change'
        if self.changed():
            "*** YOUR CODE HERE ***"
            if self.after < self.before:
                verb = 'decreased'
            else:
                verb = 'increased'
            msg = verb + ' ' + str(self.before) + '->' + str(self.after)
        return str(self.id) + ': ' + msg

class Account:
    """A bank account that tracks its transaction history.

    >>> a = Account('Eric')
    >>> a.deposit(100)    # Transaction 0 for a
    100
    >>> b = Account('Erica')
    >>> a.withdraw(30)    # Transaction 1 for a
    70
    >>> a.deposit(10)     # Transaction 2 for a
    80
    >>> b.deposit(50)     # Transaction 0 for b
    50
    >>> b.withdraw(10)    # Transaction 1 for b
    40
    >>> a.withdraw(100)   # Transaction 3 for a
    'Insufficient funds'
    >>> len(a.transactions)
    4
    >>> len([t for t in a.transactions if t.changed()])
    3
    >>> for t in a.transactions:
    ...     print(t.report())
    0: increased 0->100
    1: decreased 100->70
    2: increased 70->80
    3: no change
    >>> b.withdraw(100)   # Transaction 2 for b
    'Insufficient funds'
    >>> b.withdraw(30)    # Transaction 3 for b
    10
    >>> for t in b.transactions:
    ...     print(t.report())
    0: increased 0->50
    1: decreased 50->40
    2: no change
    3: decreased 40->10
    """

    # *** YOU NEED TO MAKE CHANGES IN SEVERAL PLACES IN THIS CLASS ***
    def next_id(self):
        """
        通过返回当前交易列表的长度作为下一笔交易的ID
        每次交易都会在self.transactions中增加一条记录
        """
        return len(self.transactions)

    def __init__(self, account_holder):
        """初始化账户:设置余额为0,保存账户持有人姓名,初始化交易列表。"""
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def deposit(self, amount):
        """增加账户余额，记录存款交易，返回新余额。"""
        # 添加存款交易，记录交易ID、交易前余额、交易后的新余额
        self.transactions.append(Transaction(self.next_id(), self.balance, self.balance + amount))
        # 更新账户余额
        self.balance = self.balance + amount
        # 返回新余额
        return self.balance

    def withdraw(self, amount):
        """减少账户余额，记录取款交易，返回新余额。如果余额不足，记录失败交易。"""
        # 如果取款金额大于余额，记录无变化的交易
        if amount > self.balance:
            self.transactions.append(Transaction(self.next_id(), self.balance, self.balance))
            return 'Insufficient funds'
        # 添加取款交易，记录交易前后的余额变化
        self.transactions.append(Transaction(self.next_id(),self.balance, self.balance - amount))
        # 更新账户余额
        self.balance = self.balance - amount
        return self.balance




class Email:
    """An email has the following instance attributes:

        msg (str): the contents of the message
        sender (Client): the client that sent the email
        recipient_name (str): the name of the recipient (another client)
    """
    def __init__(self, msg, sender, recipient_name):
        self.msg = msg
        self.sender = sender
        self.recipient_name = recipient_name

class Server:
    """Each Server has one instance attribute called clients that is a
    dictionary from client names to client objects.
    (模拟一个邮件服务器，管理所有的客户端并处理邮件的转发)
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Append the email to the inbox of the client it is addressed to."""
        self.clients[email.recipient_name].inbox.append(email)

    def register_client(self, client):
        """Add a client to the dictionary of clients."""
        self.clients[client.name] = client

class Client:
    """A client has a server, a name (str), and an inbox (list).
    (表示邮件系统中的客户端（用户），可以发送和接收邮件。)
    >>> s = Server()
    >>> a = Client(s, 'Alice')
    >>> b = Client(s, 'Bob')
    >>> a.compose('Hello, World!', 'Bob')
    >>> b.inbox[0].msg
    'Hello, World!'
    >>> a.compose('CS 61A Rocks!', 'Bob')
    >>> len(b.inbox)
    2
    >>> b.inbox[1].msg
    'CS 61A Rocks!'
    >>> b.inbox[1].sender.name
    'Alice'
    """
    # 创建用户
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name
        server.register_client(self)
    # 操作邮件
    def compose(self, message, recipient_name):
        """Send an email with the given message to the recipient."""
        email = Email(message, self,recipient_name)
        self.server.send(email)


def make_change(amount, coins):
    """Return a list of coins that sum to amount, preferring the smallest coins
    available and placing the smallest coins first in the returned list.

    The coins argument is a dictionary with keys that are positive integer
    denominations and values that are positive integer coin counts.

    >>> make_change(2, {2: 1})
    [2]
    >>> make_change(2, {1: 2, 2: 1})
    [1, 1]
    >>> make_change(4, {1: 2, 2: 1})
    [1, 1, 2]
    >>> make_change(4, {2: 1}) == None
    True

    >>> coins = {2: 2, 3: 2, 4: 3, 5: 1}
    >>> make_change(4, coins)
    [2, 2]
    >>> make_change(8, coins)
    [2, 2, 4]
    >>> make_change(25, coins)
    [2, 3, 3, 4, 4, 4, 5]
    >>> coins[8] = 1
    >>> make_change(25, coins)
    [2, 2, 4, 4, 5, 8]
    """
    if not coins:
        return None
    # 查找最小面值硬币
    smallest = min(coins)
    # 更新硬币字典
    rest = remove_one(coins, smallest)
    # 检查目标金额是否小于最小面值 如果目标金额小于最小面值 无法凑出
    if amount < smallest:
        return None
    # 目标金额等于最小面值，直接返回最小面值
    elif amount == smallest:
        return [smallest]
    # 剩余情况 使用递归进行查找
    else:
        result = make_change(amount - smallest, rest)
        # 递归成功 返回应得结果
        if result:
            return [smallest] + result
        # 递归失败 停止使用此最小面额组合 尝试其他组合
        else:
            return make_change(amount, rest)
    
def remove_one(coins, coin):
    """Remove one coin from a dictionary of coins. Return a new dictionary,
    leaving the original dictionary coins unchanged.

    >>> coins = {2: 5, 3: 2, 6: 1}
    >>> remove_one(coins, 2) == {2: 4, 3: 2, 6: 1}
    True
    >>> remove_one(coins, 6) == {2: 5, 3: 2}
    True
    >>> coins == {2: 5, 3: 2, 6: 1} # Unchanged
    True
    """
    copy = dict(coins)
    count = copy.pop(coin) - 1  # The coin denomination is removed
    if count:
        copy[coin] = count      # The coin denomination is added back
    return copy

class ChangeMachine:
    """A change machine holds a certain number of coins, initially all pennies.
    The change method adds a single coin of some denomination X and returns a
    list of coins that sums to X. The machine prefers to return the smallest
    coins available. The total value in the machine never changes, and it can
    always make change for any coin (perhaps by returning the coin passed in).

    The coins attribute is a dictionary with keys that are positive integer
    denominations and values that are positive integer coin counts.

    >>> m = ChangeMachine(2)
    >>> m.coins == {1: 2}
    True
    >>> m.change(2)
    [1, 1]
    >>> m.coins == {2: 1}
    True
    >>> m.change(2)
    [2]
    >>> m.coins == {2: 1}
    True
    >>> m.change(3)
    [3]
    >>> m.coins == {2: 1}
    True

    >>> m = ChangeMachine(10) # 10 pennies
    >>> m.coins == {1: 10}
    True
    >>> m.change(5) # takes a nickel & returns 5 pennies
    [1, 1, 1, 1, 1]
    >>> m.coins == {1: 5, 5: 1} # 5 pennies & a nickel remain
    True
    >>> m.change(3)
    [1, 1, 1]
    >>> m.coins == {1: 2, 3: 1, 5: 1}
    True
    >>> m.change(2)
    [1, 1]
    >>> m.change(2) # not enough 1's remaining; return a 2
    [2]
    >>> m.coins == {2: 1, 3: 1, 5: 1}
    True
    >>> m.change(8) # cannot use the 2 to make 8, so use 3 & 5
    [3, 5]
    >>> m.coins == {2: 1, 8: 1}
    True
    >>> m.change(1) # return the penny passed in (it's the smallest)
    [1]
    >>> m.change(9) # return the 9 passed in (no change possible)
    [9]
    >>> m.coins == {2: 1, 8: 1}
    True
    >>> m.change(10)
    [2, 8]
    >>> m.coins == {10: 1}
    True

    >>> m = ChangeMachine(9)
    >>> [m.change(k) for k in [2, 2, 3]]
    [[1, 1], [1, 1], [1, 1, 1]]
    >>> m.coins == {1: 2, 2: 2, 3: 1}
    True
    >>> m.change(5) # Prefers [1, 1, 3] to [1, 2, 2] (more pennies)
    [1, 1, 3]
    >>> m.change(7)
    [2, 5]
    >>> m.coins == {2: 1, 7: 1}
    True
    """
    def __init__(self, pennies):
        self.coins = {1: pennies}

    def change(self, coin):
        """Return change for coin, removing the result from self.coins."""
        "*** YOUR CODE HERE ***"
        # 将传入的硬币 coin 添加到 找零机 中
        self.coins[coin] = 1 + self.coins.get(coin, 0)

        # 调用 make_change 函数尝试使用现有的硬币凑出和 coins 相同的组合
        result = make_change(coin, self.coins)

        # 使用 result 中的硬币作为找零，并从储存中移除他们
        for c in result:
            self.coins = remove_one(self.coins, c)

        # 返回找零结果  
        return result

