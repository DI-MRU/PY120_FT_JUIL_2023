class Farm:
    def __init__(self,name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count
        
    def get_info(self):
        info = [f"{self.name}'s farm\n\n"]
        for animal,count in self.animals.items():
            info.append(f"{animal} : {count}")
        info.append(f"\tE-I-E-I-O!")

        return "\n".join(info)
    
    def get_animal_types(self):
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_str=", ".join(animal_types)
        return f"{self.name}'s farm has {animal_str}."


# Test the code
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print(macdonald.get_short_info())