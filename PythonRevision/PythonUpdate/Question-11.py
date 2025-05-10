# To use OOP here
from sympy.strategies.core import switch


class BankAccount:
    def __init__(self, balance: int):
        self.balance = balance

    def deposition(self):
        amount = int(input("Enter the amount you want to deposit in your bank account: "))
        self.balance = amount + self.balance
        print(f"Deposited INR. {amount}. The balance: INR. {self.balance}.")

    def withdrawal(self):
        amount = int(input("Enter the amount of money you want to withdraw: "))
        if amount > self.balance:
            print("The amount you want to withdraw is higher than your bank balance. Insufficient bank balance.")
            return
        self.balance = self.balance - amount
        print(f"Withdrawal Successful. Balance: {self.balance}")

    def check_balance(self):
        print(f"Your Bank balance is: {self.balance}")


balance1 = int(input("Enter the balance amount of your Bank account: "))
account = BankAccount(balance1)
flag = True
while flag:
    print(f"What actions would you like to perform with your account? \n 1. Deposit \n 2. Withdraw \n 3. Check balance "
          f"\n 4. Exit")
    a = input("Enter your choice: ")
    match a:
        case '1':
            account.deposition()
        case '2':
            account.withdrawal()
        case '3':
            account.check_balance()
        case '4':
            print("Exiting the program...")
            flag = False
