# Question 4
class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(
            f"Deposit of ${amount:.2f} successful. Current balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(
                f"Withdrawal of ${amount:.2f} successful. Current balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        print(f"Current balance: ${self.balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(
            f"Interest applied: ${interest:.2f}. New balance: ${self.balance:.2f}")

    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\n
        Balance: ${self.balance: .2f}\nInterest Rate: {self.interest_rate}%"


# Create a BankAccount instance
account1 = BankAccount("1234567890", "John Doe")

# Perform deposit and withdrawal operations
account1.deposit(1000)
account1.withdraw(500)
account1.get_balance()

# Create a SavingsAccount instance
savings_account = SavingsAccount("9876543210", "Jane Doe", 2.5)

# Apply interest and print the details
savings_account.apply_interest()
print(savings_account)
