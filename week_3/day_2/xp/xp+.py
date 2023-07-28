# Exercise 1 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]


# 2. Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ first name.

class Family:
    def __init__(self, last_name):
        self.members = []
        self.last_name = last_name

    def born(self, **kwargs):
        # Add a child to the members list using the provided information
        self.members.append(kwargs)
        print(f"Congratulations! {kwargs['name']} is born into the {self.last_name} family.")

    def is_18(self, name):
        # Check if the family member with the given name is over 18
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        # Print the family's last name and all members' first names
        print(f"Family Name: {self.last_name}")
        print("Members:")
        for member in self.members:
            print(member['name'])

# Initial members data
initial_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

# Create a Family instance
my_family = Family(last_name="Smith")

# Add initial members to the family
my_family.members = initial_members

# Test the methods
my_family.born(name='Emily', age=2, gender='Female', is_child=True)
print(my_family.is_18('Michael'))  # Output: True
print(my_family.is_18('Emily'))    # Output: False
my_family.family_presentation()


# Exercise 2 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.

# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
# ]


# Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.


# Add a method called incredible_presentation which :

# Prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method)
# Prints all the members’ incredible name and power.

# Call the incredible_presentation method.


# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.


# Call the incredible_presentation method again.

# TheIncredibles class inheriting from the Family class
class TheIncredibles(Family):
    def __init__(self, last_name):
        # Call the constructor of the base class (Family) to initialize the last_name attribute
        super().__init__(last_name)

    # Override the incredible_presentation method to include member's power and incredible_name
    def incredible_presentation(self):
        # Call the family_presentation method from the base class to print the family's last name and members' first names
        super().family_presentation()

        # Print all members' incredible names and powers
        print("Members' Powers:")
        for member in self.members:
            print(f"{member['name']} - {member['incredible_name']} ({member['power']})")

    def use_power(self, name):
        # Check if the member is over 18
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{name} uses {member['power']} power.")
                else:
                    raise Exception(f"{name} is not over 18 years old. Cannot use power.")

# Initial members data
initial_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

# Create a TheIncredibles instance
incredibles_family = TheIncredibles(last_name="Incredibles")

# Add initial members to the family
incredibles_family.members = initial_members

# Call the incredible_presentation method
incredibles_family.incredible_presentation()

# Use the born method inherited from Family class to add Baby Jack with the following power: "Unknown Power"
incredibles_family.born(name='Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='BabyJack')

# Call the incredible_presentation method again
incredibles_family.incredible_presentation()
