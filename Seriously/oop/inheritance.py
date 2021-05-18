"""
Inheritance:
   Single Inheritance
   Multiple Inheritance
   Multilevel Inheritance
   Hierarchical Inheritance
   Hybrid Inheritance
"""


class Vehicle:
    def __init__(self, name, color, door, window, seats):  # called as initalizer
        self.name = name
        self.color = color
        self.window = window
        self.door = door
        self.seats = seats

    def seat(self):
        return self.seats

    def description(self):
        return f"{self.name}'s color is {self.color} and it has {self.door} doors."

    def make_it_blue(self):
        self.color = "Blue"


class Car(Vehicle):
    def number_of_door(self):
        return f"Car has {self.door} doors."


v1 = Car("Car", "Yellow", 4, 9, 10)
print(v1.color)
print(v1.number_of_door())
