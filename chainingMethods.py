class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.name}'s account balance is {self.account_balance}")
        return self

james = User("James")
john = User("John")
jane = User("Jane")

james.make_deposit(100).make_deposit(50).make_deposit(50).make_withdrawal(50).display_user_balance()

john.make_deposit(100).make_deposit(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()

jane.make_deposit(100).make_withdrawal(50).make_withdrawal(10).make_withdrawal(20).display_user_balance()