# Encapsulation using example of a bank account
class BankAccount:
    def __init__(self, accountholder, balance):
        self.accountholder = accountholder
        self.__balance = balance  # Private variable

    # Public method to check balance
    def get_balance(self):
        return self.__balance  

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # Correct balance update
            print(f"Deposited {amount}. New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:  # Correct balance check
            self.__balance -= amount  # Correct balance update
            print(f"Withdrew {amount}. Remaining Balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount")

# Creating an object
account = BankAccount("Imran", 20000)

# Accessing public variable correctly
print(account.accountholder)

# Trying to access private variable directly (This will cause an error)
# print(account.__balance)  # Uncommenting this will cause an AttributeError

# Accessing private variable using method
print(account.get_balance())

# Depositing money
account.deposit(5000)

# Withdrawing money
account.withdraw(3000)
