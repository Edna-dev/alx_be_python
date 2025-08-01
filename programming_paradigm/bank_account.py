class BankAccount:
    def __init__(self, initial_balance=0):
        # Encapsulated balance with double underscores
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add amount to the account balance."""
        self.__account_balance += amount

    def withdraw(self, amount):
        """Subtract amount from the balance if funds are sufficient."""
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.__account_balance}")
