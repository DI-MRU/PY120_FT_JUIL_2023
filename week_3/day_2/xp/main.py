import random
from dog import Dog  # Import the Dog class from the previous exercise

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        # Trains the dog and sets the trained attribute to True
        print(self.bark())  # Print the dog's bark when training
        self.trained = True

    def play(self, *dog_names):
        # Allows the dog to play with other dogs by taking multiple dog names as arguments
        print(f"{', '.join(dog_names)} all play together")  # Print the names of all dogs playing together

    def do_a_trick(self):
        # If the dog is trained, performs a random trick from the list; otherwise, notifies that the dog is not trained
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))  # Print a random trick from the list
        else:
            print(f"{self.name} is not trained yet.")  # Notify that the dog is not trained yet

# Example usage:
dog1 = PetDog("Buddy", 3, 15)
dog2 = PetDog("Max", 5, 20)

dog1.train()
dog1.play("Max")
dog1.do_a_trick()

dog2.train()
dog2.play("Buddy", "Charlie")
dog2.do_a_trick()

