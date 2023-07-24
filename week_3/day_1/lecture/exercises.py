class Person:
    """
    Base class for person objects.
    """

    def __init__(self, name, age):
        """
        Constructor.

        Args:
            name: The name of the person.
            age: The age of the person.
        """
        self.name = name
        self.age = age

    def show_details(self):
        """
        Prints out a greeting with the name of the person.
        """
        print("Hello my name is " + self.name)


first_person = Person("John", 36)
first_person.show_details()


class Computer(object):
    """Type of computers."""

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        # Analyse the line below
        print(self)


mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark")
