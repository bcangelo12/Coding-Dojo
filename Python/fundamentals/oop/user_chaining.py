class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
# creating 3 instances of user 
Alex = User("Alex Smith", "alex.smith@gmail.com")
Brendan = User("Brendan Angelo", "brendan.angelo@gmail.com")
Chad = User("Chad Strong", "chad.strong@gmail.com")
# first user 3 deposits, 1 withdrawl, display, all chained
Alex.make_deposit(200).make_deposit(700).make_deposit(4000).make_withdrawl(1700).display_user_balance()
# second user 2 deposits, 2 withdrawls, display, all chained
Brendan.make_deposit(5000).make_deposit(15000).make_withdrawl(9999).make_withdrawl(6900).display_user_balance()
# third user 1 deposit, 3 withdrawls, display, all chained
Chad.make_deposit(10000).make_withdrawl(1000).make_withdrawl(4000).make_withdrawl(1700).display_user_balance()
# user 1 transfer to user 3, display both, cannot be chained with current knowledge
Alex.transfer_money(Chad, 200)
Alex.display_user_balance()
Chad.display_user_balance()