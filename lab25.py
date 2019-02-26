"""
Let's represent an ATM with a class containing a balance property. A newly created account will default to a balance of 0. Implement the initializer, as well as the following methods:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
Version 2

Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new function print_transactions() to your class for printing out the list of transactions.

Version 3

Allow the user to enter commands into a REPL.

> what would you like to do (deposit, withdraw, check balance, history)?
> deposit
> how much would you like to deposit?
> $5
> what would you like to do (deposit, withdraw, check balance, history)?
> check balance
> balance: $5
"""


class ATM():
    def __init__(self, balance=0, transactions=[], machineName="EasleyTech MoCash 5000"):
        self.balance = balance
        self.transactions = []
        self.machineName = machineName
        self.menu = """
                        (W)ithdraw
                        (D)eposit
                        (C)heck Balance
                        (L)ist Transactions"""

    def print_menu(self):
        print(f"{'*'*30} {self.machineName} {'*'*30}")
        print(f"{self.menu}")
        print(f"Balance: ${self.balance}")

    def get_input(self):
        return input("Enter command [C / D / L / W]: ")

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.__add_transaction(f"Deposited ${amount}")

    def check_withdrawal(self, amount):
        if (self.balance - amount) >= 0:
            return True
        else:
            return False

    def withdraw(self, amount):
        self.balance -= amount
        self.__add_transaction(f"Withdrew ${amount}")
        print(f"${amount} withdrawn. Your new balance is : ${self.balance}")

    def __add_transaction(self, transaction):
        self.transactions.append(transaction)

    def list_transactions(self):
        print(self.transactions)


def main():
    myAtm = ATM(250)
    myAtm.print_menu()

    print(myAtm.check_balance())

if __name__ == '__main__':
    main()
