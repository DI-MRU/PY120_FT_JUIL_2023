# Data Types
# 1. Which of the following is not a mutable data type in Python?
#    a) List
#    b) Dictionary
#    c) Tuple
#    d) Set
# Answer: C

# Lists and Loops
# 1. Using a list comprehension, generate a list of the squares of numbers from 1 to 10, but only include squares of even numbers.

numbers = range(11)
squares = [number**2 for number in numbers if number % 2 == 0]
print(squares)

# 2. Using the range function, create a list of numbers from 1 to 10, then print numbers that are divisible by both 2 and 3.

## Method 1
numbers = range(11)
divisible_numbers = []
for number in numbers:
    if number % 2 == 0 and number % 3 == 0:
        divisible_numbers.append(number)
print(divisible_numbers)

## Method 2
print([number for number in numbers if number % 2 == 0 and number % 3 == 0])

# 3. Loop through the provided list of dictionaries and print the names and ages:
student_list = [
    {"name": "John", "age": 24},
    {"name": "Anna", "age": 22},
    {"name": "Mike", "age": 25},
]

for student in student_list:
    print(student["name"], student["age"])

# Function Behavior with *args and **kwargs

# 1. Write a function combine_words that accepts any number of positional arguments and key-value arguments. The function should return a single sentence combining all the words provided.
#    Example:
#    print(combine_words("Hello", "world", second="is", third="great!", first="Python"))
#    Expected Output: # IMPORTANT: Please disregard this, the order of the kwargs should be as provided to the function instead
#    "Hello world. Python is great!"
#    Test cases
#    print(combine_words("Hello", "world", second="is", third="great!", first="Python"))
#    print(combine_words("Hello", second="is", third="great!"))
#    print(combine_words("Hello", "world", "sjkldfhs",second="is", third="great!", first="Python", dfgkfd="sdfsdf"))
#    print(combine_words("Hello", "world", second="is", third="great!", first="Python", "sdkfsdk")) # Should fail
#    print(combine_words("Hello", "world", "I'm sleepy"))
#    print(combine_words(test="hkdfhf"))


def combine_words(*args, **kwargs):
    """Combines any amount of words into a single sentence.

    Arguments:
    *args - Positional string arguments.
    **kwards - Keyword string arguments.

    Returns:
    A string containing the combined words separated with a space.
    """

    sentence = ""
    # order_list = ["first", "second", "third", "fourth", "fifth", "hundredth"] # Please don't do this

    # Loop through positional arguments
    for argument in args:
        sentence += " " + argument

    # Loop through keyword arguments
    for key, value in kwargs.items():
        sentence += " " + value

    return sentence


print(combine_words("Hello", "world", second="is", third="great!", first="Python"))
print(combine_words("Hello", second="is", third="great!"))
print(
    combine_words(
        "Hello",
        "world",
        "sjkldfhs",
        second="is",
        third="great!",
        first="Python",
        dfgkfd="sdfsdf",
    )
)
# print(combine_words("Hello", "world", second="is", third="great!", first="Python", "sdkfsdk")) # Should fail
print(combine_words("Hello", "world", "I'm sleepy"))
print(combine_words(test="hkdfhf"))

# Object-Oriented Programming (OOP)
# 1. Create a class Vehicle with string attributes type, brand, and integer attribute year. Ensure instances of the vehicle cannot be created if any of these attributes are missing and include a method to display the vehicle’s info. Use dunder method.


# ## Method 1
# class Vehicle:
# ## Method 2
# class Vehicle():
## Method 3
class Vehicle(object):
    def __init__(
        self, type, brand, year
    ):  # Please don't use reserved/inbuilt names such as type, class, for, print
        self.type = type
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"""
Vehicle:
Type  - {self.type}
Brand - {self.brand}
Year  - {self.year}
"""


audi = Vehicle("Sedan", "Audi", 2023)
bmw = Vehicle("SUV", "BMW", 2024)
print(audi)
print(bmw)

# OOP Inheritance and Decorators
# 1. Create a class Car with string attributes brand, model, and integer attribute mileage. Implement a method to return the car’s details.


class Car(object):
    def __init__(
        self, brand, model, mileage
    ):  # Please don't use reserved/inbuilt names such as type, class, for, print
        self.brand = brand
        self.model = model
        self.mileage = mileage

    def __str__(self):
        return f"""
Car:
Brand    - {self.brand}
Model    - {self.model}
Mileage  - {self.mileage}
"""


# 2. Create a subclass ElectricCar inheriting from Car with an additional float private attribute __battery_capacity. Override the car’s details method to include the battery capacity.
#    Use the @property decorator to get the battery_capacity value and @battery_capacity.setter to modify the battery capacity only if the new value is positive.


class ElectricCar(Car):
    def __init__(self, brand, model, mileage, color, battery_capacity):
        super().__init__(brand, model, mileage)
        self.color = color
        self.__battery_capacity = battery_capacity

    def __str__(self):
        return f"""
Car | Electric:
Brand    - {self.brand}
Model    - {self.model}
Mileage  - {self.mileage} km
Color    - {self.color}
Battery  - {self.battery_capacity} kW
"""

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, value):
        if value > 0:
            self.__battery_capacity = value
        else:
            raise ValueError("The battery capacity must be positive.")


mustang = ElectricCar("Ford", "Mustang", "10000", "Matte Black", "100")
print(mustang)
mustang.battery_capacity = 150
print(mustang)

# 3. Create a BankAccount class with private float attribute _balance and private string attribute _account_holder. Implement methods to deposit, withdraw, and view the balance. Include a class method to track accounts created and a static method for a bank policy message. Ensure the balance is non-negative.


class BankAccount:
    def __init__(self, account_holder, balance=0):
        self._balance = balance
        self._transactions = 0
        self._account_holder = account_holder

    def __str__(self):
        return f"""--- START Account {self._account_holder} ---
Balance:      {self._balance}
Transactions: {self._transactions}
---   END Account {self._account_holder} ---"""

    def deposit(self, amount):
        self._transactions += 1
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("The deposit amount is invalid.")

    def withdraw(self, amount):
        self._transactions += 1
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
        elif amount > 0 and amount > self._balance:
            raise ValueError("Insufficient balance.")
        else:
            raise ValueError("The withdraw amount is invalid.")

    def view(self):
        self._transactions += 1
        print(self)


laeticia_acc = BankAccount("Laeticia", 1000000)
# print(laeticia_acc)
laeticia_acc.view()
# laeticia_acc.deposit(-100) # Invalid amount
laeticia_acc.deposit(100)
laeticia_acc.view()
# laeticia_acc.withdraw(-500) # Invalid amount
# laeticia_acc.withdraw(2000000) # Insufficient balance
laeticia_acc.withdraw(1000000)
laeticia_acc.view()

# Data Science
# Numpy and Pandas Visualization
# 1. Create a numpy array of shape (3,3) filled with integers from 1 to 9 using arange().
# 2. Provided pandas DataFrame df:
#    import pandas as pd
#    df = pd.DataFrame({'A': [1, 'apple', 3, 4, 'banana'], 'B': [5, 6, 7, 8, 9]})
#    - Replace non-numeric values in column “A” with the mean of numeric values. Plot a histogram of the “A” column using matplotlib.
# 3. Plot “A” and “B” columns of df using matplotlib. Add x-axis, y-axis labels, and a title.

# Django and Django REST
# Create a new Django project called ‘academy’. After that - create a new app (inside the ‘academy’ project) called ‘school’.
# Django Models with Foreign Key
# 1. Define Django models Teacher and Course. Course has course_name (CharField) and course_code (CharField). Teacher has name (CharField). Create a many-to-many relationship between Teacher and Course.
# Views
# 1. Create a Django view course_details to fetch details of a course by its id.
# 2. Use a APIview for Teacher to display all teachers.
# Full App
# 1. Create a base model SchoolFacility with facility_name (CharField) and usage_purpose (TextField).
# 2. Create a Laboratory model inheriting from SchoolFacility with equipment_list (TextField).
# 3. Create views for all school facilities and another for only laboratories.
# 4. Create a serializer for SchoolFacility and another for Laboratory to convert to JSON. Test using Postman.
