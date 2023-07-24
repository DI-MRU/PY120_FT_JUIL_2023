class Computer(object):
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def __str__(self):
        """String representation fo the object"""
        return f"The computer is a {self.brand} and of price ${self.price}"

    def __lt__(self, other):
        """Less than"""
        return self.price < other.price

    # def __gt__(self, other):
    # def __eq__(self, other):


v_pc = Computer("ASUS", 100)
o_pc = Computer("HP", 101.50)
l_pc = Computer("Apple", 349583495)
a_pc = Computer("Dell", 439)
d_pc = Computer("Samsung", 349578)

print(v_pc)
print(o_pc)
print(l_pc)
print(a_pc)
print(d_pc)

print(f"V's pc is better than A's pc: {v_pc > a_pc}")
print(f"V's pc is worse than A's pc: {v_pc < a_pc}")
print(f"V's pc is as good as  A's pc: {v_pc == a_pc}")
