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


car = Vehicle("Car", "Red", 4, 8, 7)
bike = Vehicle("Bike", "Blue", 0, 0, 2)
print("===============Vehicle 1 Details=================")
print("Before:", car.color)
print(car.description())
car.make_it_blue()
print("After:", car.color)
print(car.description())
print("===============Vehicle 2 Details=================")
print("Before:", bike.color)
print(bike.description())
bike.make_it_blue
print("After:", bike.color)
print(bike.description())
