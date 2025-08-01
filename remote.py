class Bank_account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance #private attribute

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    #setter for balance with validation
    def balance(self,amount):
        if amount >= 0:
            self.__balance = amount
            return self.__balance
        else:
            print('Balance cannot be negative')
account = Bank_account('Alice', 1000)
print(account.balance)
account.balance = 1499
account.balance = -122
print(account.balance)
