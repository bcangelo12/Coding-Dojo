class BankAccount:
    accounts = []
    def __init__(self, int_rate=0.04, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        return f"{self.balance}"
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account = {
            "checking": BankAccount(0.02,500),
            "savings" : BankAccount(0.04,2000)
        }
        pass
    def make_deposit(self, amount):
        self.account.deposit(amount)
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: ${self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: ${self.account['savings'].display_account_info()}")
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self

brendan = User('Brendan','brendanangelo12@gmail.com')

brendan.account['checking'].deposit(500)
brendan.display_user_balance()