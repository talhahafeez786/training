class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner        # Public attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True 
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance

# Creating an object of the BankAccount class
account = BankAccount("Alice", 1000)

# Using the public methods to interact with the private balance attribute
print(account.get_balance())  # Output: 1000

account.deposit(500)
print(account.get_balance())  # Output: 1500

account.withdraw(300)
print(account.get_balance())  # Output: 1200

# Trying to access the private attribute directly (Not recommended)
# print(account.__balance)  # This will raise an AttributeError
