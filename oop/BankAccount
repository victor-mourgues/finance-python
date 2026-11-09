"""
BankAccount: a simple bank account class.

Illustrates __init__, self, attributes vs methods, getters, and input
validation (a withdrawal cannot exceed the balance).

"""

class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        """Add 'amount' to the balance."""
        self.balance = self.balance + amount

    def withdraw(self, amount):
        """Withdraw 'amount', unless it exceeds the balance."""
        if amount > self.balance:
            print("Not enough money to withdraw", amount)
        else:
            self.balance = self.balance - amount

    def get_balance(self):
        return self.balance

# Execution -------------------------------------------------------------------
if __name__ == "__main__":
    c = BankAccount(100)
    c.deposit(50)
    c.withdraw(30)
    print(c.get_balance())    
    c.withdraw(500)
    print(c.get_balance())    
