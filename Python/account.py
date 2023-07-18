class account:
    numcreated = 0


    def __init__(self,initial):
        self.balance = initial
        account.numcreated += 1

    def deposit(self, amt):
        self.balance += amt
        return

    def withdraw(self, amt):
        self.balance -= amt
        return

    def getbalance(self):
        return self.balance


