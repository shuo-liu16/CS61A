from cgitb import small

class Transaction:
    def __init__(self, id, before, after):
        self.id = id
        self.before = before
        self.after = after

    def changed(self):
        """Return whether the transaction resulted in a changed balance."""
        "*** YOUR CODE HERE ***"
        if self.before != self.after:
            return True
        else:
            return False

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
            if self.before > self.after:
                msg = 'decreased ' + str(self.before) + '->' + str(self.after)
            else:
                msg = 'increased ' + str(self.before) + '->' + str(self.after)
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
    def next_id(self):
        print("DEBUG:len",len(self.transactions))
        return len(self.transactions)
    
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def deposit(self, amount):
        """Increase the account balance by amount, add the deposit
        to the transaction history, and return the new balance.
        """
        self.transactions.append(Transaction(self.next_id(), self.balance, self.balance + amount))
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount, add the withdraw
        to the transaction history, and return the new balance.
        """
        if amount > self.balance:
            self.transactions.append(Transaction(self.next_id(), self.balance, self.balance))
            return 'Insufficient funds'
        self.transactions.append(Transaction(self.next_id(), self.balance, self.balance - amount))
        self.balance = self.balance - amount
        return self.balance




class Email:
    """An email has the following instance attributes:

        msg (str): the contents of the message
        sender (Client): the client that sent the email
        recipient_name (str): the name of the recipient (another client)
    """
    def __init__(self, msg, sender, recipient_name):
        self.msg = msg  # msg内容
        self.sender = sender    # client 发信人 对象
        self.recipient_name = recipient_name # 接信人名称

class Server:
    """Each Server has one instance attribute called clients that is a
    dictionary from client names to client objects.
    """
    def __init__(self):
        # 服务器所有人员对象
        self.clients = {}

    def send(self, email):
        """Append the email to the inbox of the client it is addressed to."""
        self.clients[email.recipient_name].inbox.append(email)
        # 在服务器中遍历，向接信人邮箱投递email

    def register_client(self, client):
        """Add a client to the dictionary of clients."""
        self.clients[client.name] = client
        # 在服务器中注册账号

class Client:
    """A client has a server, a name (str), and an inbox (list).

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
    def __init__(self, server, name):
        self.inbox = []     # 邮箱
        self.server = server    # 服务器
        self.name = name    # 邮箱用户
        server.register_client(self)    # 注册

    def compose(self, message, recipient_name):
        """Send an email with the given message to the recipient."""
        email = Email(message, self, recipient_name)
        # 编写右键
        self.server.send(email)
        # 发送


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
    smallest = min(coins)
    rest = remove_one(coins, smallest)
    if amount < smallest:
        return None
    elif amount == smallest:
        return [smallest]
    else:
        if make_change(amount - smallest, rest) is None:
            return make_change(amount, rest)
        else:
            return [smallest] + make_change(amount - smallest, rest)


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
        if make_change(coin, self.coins) is None:
            return [coin]
        else:
            res = make_change(coin, self.coins)
            # 删除硬币
            for x in res:
                self.coins = remove_one(self.coins, x)
            # 添加硬币
            if coin in self.coins:
                self.coins[coin] += 1
            else:
                self.coins[coin] = 1
            print("DEBUG:", str(self.coins))
            return res

