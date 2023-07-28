#  Exercise 1 : Pets
# Instructions

# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.

# Using this code:

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Create instances of different cat breeds
bengal_cat = Bengal("Bengal Cat", 3)
chartreux_cat = Chartreux("Chartreux Cat", 2)
siamese_cat = Siamese("Siamese Cat", 4)

# Create a list containing all cat instances
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# Create a Pets instance with all_cats as an argument
sara_pets = Pets(all_cats)


# Take all the cats for a walk using the walk method of Pets
sara_pets.walk()


# Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        self_run_speed = self.run_speed() * self.weight
        other_run_speed = other_dog.run_speed() * other_dog.weight

        if self_run_speed > other_run_speed:
            return f'{self.name} won the fight'
        elif self_run_speed < other_run_speed:
            return f'{other_dog.name} won the fight'
        else:
            return 'It was a tie'

# Create three dog instances
dog1 = Dog("Buddy", 3, 15)
dog2 = Dog("Max", 5, 20)
dog3 = Dog("Charlie", 2, 10)

# Test the methods for each dog
print(dog1.bark())  # Output: "Buddy is barking"
print(dog2.run_speed())  # Output: 40.0 (20/5*10)
print(dog3.fight(dog1))  # Output: "Buddy won the fight" (Buddy's run_speed * Buddy's weight is higher than Charlie's)
print(dog2.fight(dog3))  # Output: "Max won the fight" (Max's run_speed * Max's weight is higher than Charlie's)
print(dog1.fight(dog2))  # Output: "It was a tie" (Buddy's run_speed * Buddy's weight is equal to Max's)



#  Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.