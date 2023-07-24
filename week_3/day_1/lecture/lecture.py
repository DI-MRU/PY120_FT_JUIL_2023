# Extra, if we have time, special methods


# These 3 ways of defining classes are all the same
# class Car():
# class Car(object):
class Car:
    def __init__(self, color, brand, model, price=0):
        """
        Constructor.

        Special method that is called whenever a new object of this class is initialized
        """
        # Please don't try to use `color = color` because the computer won't know which object we're talking about
        self.color = color  # Use `self` so that the computer may differentiate and know which object we're using
        self.brand = brand
        self.model = model
        self.price = price
        print("A Car object was initialized.")

    def print_properties(self):
        """
        This is a function that prints out the car properties.
        """
        print(self.color)
        print(self.brand)
        print(self.model)
        print(self.price)

    def change_color(self, new_color):
        # old_color = self.color
        # self.color = new_color
        print(f"The car color was changed from {self.color} to {new_color}")
        self.color = new_color

    def set_price(self, price):
        self.price = price
        print(f"The car is priced at ${self.price}")


car_a = Car("Red", "Ford", "Mustang", 30000)
car_a.print_properties()
print(f"This is car of color {car_a.color}")

car_b = Car("Blue", brand="Toyota", model="Prius")
Car.print_properties(car_b)
car_b.price = 50000
print(f"The car is priced at ${car_b.price}")

car_c = Car("Green", "Volkswagen", "Golf")
car_c.print_properties()
car_c.change_color("Purple")
car_c.set_price(20000)


print(type(car_a))
print(type(car_b))


class BankAccount:
    """Base class for bank accounts."""

    def __init__(self, account_number, balance=0):
        """Constructor.

        Args:
            account_number: The account number at the bank.
            balance: The amount of money in the account.
        """
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        print(
            f"Amount is {amount} | Balance is {self.balance} | Balance - 50 is {self.balance - 50}"
        )

        if amount > self.balance:
            print("Insufficient Funds")
        elif amount > self.balance - 50:
            print("Your balance will become too low. We wanna keep your money.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

        return 0

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)


vincent_acc = BankAccount(777, -100)
# view_balance.transaction # FAIL
# view_balance(self.account_number) # FAIL
# view_balance = self.balance # FAIL
vincent_acc.view_balance()  # No need to specify self as it is implied
BankAccount.view_balance(
    vincent_acc
)  # Need to provide the value for self as the class doesn't know which object to use
# view_balance() # Will not work as view_balance is a method of BankAccount and not available outside of it

anas_acc = BankAccount(2134, 100000)
vincent_acc.deposit(-50)
vincent_acc.deposit(99)
vincent_acc.deposit(150)

print(f"Vincent's transactions are {vincent_acc.transactions}")

vincent_acc.deposit(1000)
vincent_acc.view_balance()
# vincent_acc.withdraw(200)
wallet_amount = vincent_acc.withdraw(vincent_acc.balance - 100)
# wallet_amount = vincent_acc.withdraw(1294902385907324057034)
print(f"My wallet contains {wallet_amount} monies.")


# print(f"Vincent's transactions are {vincent_acc.transactions}")

# vincent_acc.view_balance()
vincent_acc.view_transactions()
