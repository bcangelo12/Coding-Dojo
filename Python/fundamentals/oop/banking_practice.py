# Practice setup
# class User:
#     bank_name = "First National Dojo"
#     def __init__(self):
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.account_balance = 0
#         pass

# guido = User()
# monty = User()

# guido.name = "Guido"
# print(guido.name)
# monty.name = "Monty"
# print(monty.name)

# #guido.bank_name = "Dojo Credit Union"
# print(guido.bank_name)
# print(monty.bank_name)

# User.bank_name = "Bank of Dojo"
# print(guido.bank_name)
# print(monty.bank_name)

class User:
    # class attributes get defined in the class
    bank_name = "First National Dojo"
    # now our method has 2 parameters
    def __init__(self, name, email_address):
        # we assign them accordingly
        self.name = name
        self.email_address = email_address
        # the account balance is set to $0
        self.account_balance = 0
    #adding deposit method
    def make_deposit(self, amount): #takes and argument that is the amount of the deposit
        self.account_balance += amount #the specific user's account increases by the amount of the vaule received

guido = User("Guido van Rassum", "guido@python.com")
monty = User ("Monty Python", "monty@python.com")
print(guido.name)
print(monty.name)

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)
print(monty.account_balance)