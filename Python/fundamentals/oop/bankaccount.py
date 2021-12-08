class BankAccount:
    #all_accounts = []
    accounts = [] # better variable to call later
    def __init__(self, int_rate=0.04, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        #if BankAccount.can_withdraw(self.balance, amount): # wrong method but kept for posterity
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    # not the best method -- commented out for posterity
    # @staticmethod
    # def can_withdraw(balance, amount):
    #     if (balance - amount) < 0:
    #         return False
    #     else: 
    #         return True
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            #self.balance = self.balance + self.balance * self.int_rate
            self.balance += (self.balance * self.int_rate) # better method, cleaner syntax
        # else:  not needed
        #     return False
        return self
    # adding class method after turn in
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

Checking = BankAccount()
Savings = BankAccount(0.01,1000)

Checking.deposit(700).deposit(1000).deposit(1500).withdraw(500).yield_interest().display_account_info()
Savings.deposit(1500).deposit(5000).withdraw(500).withdraw(100).withdraw(500).withdraw(800).yield_interest().display_account_info()

BankAccount.print_all_accounts()