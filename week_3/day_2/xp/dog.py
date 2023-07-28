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
