import math
import turtle

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
            self.diameter = radius * 2
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("Please specify either the radius or the diameter of the circle.")

    def __str__(self):
        return f"Circle with radius: {self.radius}, diameter: {self.diameter}"

    def area(self):
        return math.pi * self.radius**2

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

# Testing the Circle class
if __name__ == "__main__":
    circle1 = Circle(radius=50)
    circle2 = Circle(diameter=100)
    circle3 = Circle(radius=30)

    print(circle1)
    print(circle2)
    print(circle3)

    print("Area of circle1:", circle1.area())

    circle4 = circle1 + circle3
    print("Circle4 (circle1 + circle3):", circle4)

    print("Is circle1 equal to circle3?", circle1 == circle3)
    print("Is circle1 less than circle2?", circle1 < circle2)

    circles = [circle1, circle2, circle3, circle4]
    circles.sort()

    # Drawing the sorted circles using Turtle
    turtle.speed(0)
    for circle in circles:
        turtle.penup()
        turtle.goto(circle.radius, 0)
        turtle.pendown()
        turtle.circle(circle.radius)

    turtle.done()
