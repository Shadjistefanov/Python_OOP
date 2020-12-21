class Account:
    def __init__(self, id, name, *args):
            self.id = id
            self.name = name
            if (args):
                self.balance = args[0]
            else:
                self.balance=0

    def credit(self,amount):
        self.balance+=amount
        return self.balance

    def debit(self,amount):
        if (amount<=self.balance):
            self.balance-=amount
            return self.balance
        else:
            return f'Amount exceeded balance'

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"

account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())