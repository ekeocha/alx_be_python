class BankAccount:
    
    def __init__(self,account_balance):
        self.account_balance = account_balance

    def deposit(self,amount):
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            return True
        return False
    
    def display_balance(self):
        print(f"Your account balance is {self.account_balance:.2f}") 