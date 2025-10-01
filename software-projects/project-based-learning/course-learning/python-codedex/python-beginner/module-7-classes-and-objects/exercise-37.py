# Bank Accounts
# Task: To create a bank account class and have users use methods inside the class to complete tasks, like withdraw and deposit money

class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def display_balance(self):
        print("The account balance is:" + str(self.balance))

user1 = BankAccount("Anis", "Layaida", 615567943, "Current Account", 7064, 100.00)

user1.deposit(96)
user1.withdraw(25)
print(user1.display_balance())