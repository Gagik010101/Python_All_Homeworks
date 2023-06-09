from random import randint
try:
    class BankAccount():
        def __init__(self, account_number, Money, amount):
            self.account_number = account_number
            self.Money = Money
            self.amount = amount

        def deposit(self):
            print(f"Your account number is {self.account_number}")
            print(f"You have topped up your account ${self.Money}")
            print(f"Your account balance is ${self.Money + self.amount}")

        def withdraw(self):
            if self.amount - self.Money >= 0:
                print(f"You have successfully cashed out ${self.Money}")
                print(f"Your account balance is ${self.amount - self.Money}")
            else:
                print("An error occurred\nInsufficient funds")

        def print_balance(self):
            print(f"Your account balance is ${self.amount}")


    account_number = int(input("Please enter your account number\n"))
    if account_number == 123456789:
        end = 1
        amount = 100000
        while end == 1:
            Transaction = input("Select the transaction\nTransaction deposit <<entre A>>"
                                 "\nTransaction withdraw <<enter B>>"
                                 "\nTransaction print_balance <<enter C>>\n")
            if Transaction == "A":
                Money = int(input("Please enter your MONEY\n"))
            elif Transaction == "B":
                Money = int(input("Please select the amount to withdraw\n"))
            elif Transaction == "C":
                Money = None
            else:
                print("An error occurred\nPlease start again")
            Customer = BankAccount(account_number, Money, amount)

            if Transaction == "A":
                print(Customer.deposit())
            elif Transaction == "B":
                print(Customer.withdraw())
            elif Transaction == "C":
                print(Customer.print_balance())
            else:
                print("An error occurred\nPlease start again")
            end = int(input("enter 1 if you want to continue, 0 otherwise"))
    else:
        print("wrong account\nplease start again")
except ValueError:
        print("An error occurred\nPlease start again")
