class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []

    def deposit(self,amount,description =''):
        self.ledger.append({'amount': amount, 'description': description})

    
    def withdraw(self,amount,description = ''):
        if self.get_balance() > 0:
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)
    
    
    def transfer(self,amount,Category):
        if self.get_balance() > 0:
            self.withdraw(amount, f"Transfer from {Category.name}")
            Category.deposit(amount, f'Transfer to {self.name}')
            return True
        return False
    
    
    def __str__(self):
        title = f'{self.name:*^30}\n'

        items =''
        for entry in self.ledger:
            desc = entry['description'][:23]
            amt = f"{entry['amount']:.2f}"
            items += f'{desc:<23}{amt:>7}\n'

        Total = f'Total: {self.get_balance():.2f}'

        return title + items + Total
    
entertainment = Category('entertainment')
entertainment.deposit(30000, 'funactivities')
entertainment.withdraw(6900, 'dates')
entertainment.withdraw(5000, 'subscriptions')
entertainment.withdraw(3000, 'dates')

clothing = Category('clothing')
entertainment.transfer(50, clothing)
print(entertainment)
        