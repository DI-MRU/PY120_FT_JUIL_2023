'''
🌟 Exercise 1: Cats
Instructions
Using this class

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
Instantiate three Cat objects using the code provided above.
Outside of the class, create a function that finds the oldest cat and returns the cat.
Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
'''
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1=Cat("PsPsPs",3)
cat2=Cat("felix",20)
cat3=Cat("Spike",7)
 
    
def oldest_cat(cat_list):
    oldest_cat = cat_list[0]
    for cat in cat_list:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat
   

calculate_oldest = oldest_cat([cat1,cat2,cat3]) 
print(f"The oldest cat is {calculate_oldest.name}, and is {calculate_oldest.age} years old.")

'''
🌟 Exercise 2 : Dogs
Instructions
Create a class called Dog.
In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
Create a method called bark that prints the following string “<dog_name> goes woof!”.
Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
Print the details of his dog (ie. name and height) and call the methods bark and jump.
Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
Print the details of her dog (ie. name and height) and call the methods bark and jump.
Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
'''
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")


davids_dog = Dog("Rex", 50)


print(f"David's dog: {davids_dog.name}, height: {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()


sarahs_dog = Dog("Teacup", 20)


print(f"Sarah's dog: {sarahs_dog.name}, height: {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()


if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger.")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is bigger.")
else:
    print("Both dogs are the same height.")

'''
🌟 Exercise 3 : Who’s The Song Producer?
Instructions
Define a class called Song, it will show the lyrics of a song.
Its __init__() method should have two arguments: self and lyrics (a list).
Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
Create an object, for example:

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


Then, call the sing_me_a_song method. The output should be:

There’s a lady who's sure
all that glitters is gold
and she’s buying a stairway to heaven
'''
class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for music_line in self.lyrics:
            print(music_line)

stairway=Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()
'''
🌟Exercise 4 : Afternoon At The Zoo
Instructions
Create a class called Zoo.
In this class create a method __init__ that takes one parameter: zoo_name.
It instantiates two attributes: animals (an empty list) and name (name of the zoo).
Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
Create a method called get_animals that prints all the animals of the zoo.
Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
Example

{ 
    1: "Ape",
    2: ["Baboon", "Bear"],
    3: ['Cat', 'Cougar'],
    4: ['Eel', 'Emu']
}


Create a method called get_groups that prints the animal/animals inside each group.

Create an object called ramat_gan_safari and call all the methods.
Tip: The zookeeper is the one who will use this class.
Example
Which animal should we add to the zoo --> Giraffe
x.add_animal(Giraffe)
'''
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to the zoo.")

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")

    def sort_animals(self):
        sorted_animals = {}
        for animal in self.animals:
            first_letter = animal[0].capitalize()
            if first_letter in sorted_animals:
                sorted_animals[first_letter].append(animal)
            else:
                sorted_animals[first_letter] = [animal]
        return sorted_animals

    def get_groups(self):
        sorted_animals = self.sort_animals()
        print("Animals grouped by their first letter:")
        for group, animals in sorted_animals.items():
            print(f"{group}: {', '.join(animals)}")


ramat_gan_safari = Zoo("Ramat Gan Safari")

# Adding animals to the zoo
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Tiger")
ramat_gan_safari.add_animal("Elephant") 

# Printing all the animals in the zoo
ramat_gan_safari.get_animals()

# Selling an animal from the zoo
ramat_gan_safari.sell_animal("Tiger")

# Printing animals grouped by their first letter
ramat_gan_safari.get_groups()


