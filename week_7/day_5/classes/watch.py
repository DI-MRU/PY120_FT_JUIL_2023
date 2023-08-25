class Watch:
    def __init__(self, brand, price, year, color):
        self.brand = brand
        self.price = price
        self.year = year
        self.color = color

    def __str__(self):
        return f"{self.brand} | {self.price} | {self.year} | {self.color}"

    def tell_time(self):
        print(f"The time is time.")
