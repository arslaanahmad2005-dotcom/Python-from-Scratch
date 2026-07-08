#Problem 1
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"Product: {self.name}, Price: ₹{self.price}"


class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_months):
        super().__init__(name, price)
        self.warranty_months = warranty_months

    def get_details(self):
        return f"Product: {self.name}, Price: ₹{self.price}, Warranty: {self.warranty_months} months"


class ClothingProduct(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def get_details(self):
        return f"Product: {self.name}, Price: ₹{self.price}, Size: {self.size}"


# Test
laptop = ElectronicProduct("Laptop", 65000, 24)
shirt = ClothingProduct("T-Shirt", 999, "L")

print(laptop.get_details())
print(shirt.get_details())

#Peoblem 2
class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.__balance = initial_balance   # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance


# Test
account = BankAccount("Arslaan", 10000)

account.deposit(5000)
account.withdraw(3000)

print("Current Balance:", account.get_balance())

# Attempt to access private attribute directly
print(account.__balance)