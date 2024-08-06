# Base class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        return "Vehicle started"

# Derived class
class Car(Vehicle):
    def start(self):
        return f"{self.make} {self.model} started with a roar!"

# Derived class
class Bicycle(Vehicle):
    def start(self):
        return f"{self.make} {self.model} started silently!"

# Creating an object of the base class
vehicle = Vehicle("Generic", "Model")
print(vehicle.start())  # Output: Vehicle started

# Creating an object of the derived class Car
car = Car("Toyota", "Corolla")
print(car.start())  # Output: Toyota Corolla started with a roar!

# Creating an object of the derived class Bicycle
bicycle = Bicycle("Giant", "Escape 3")
print(bicycle.start())  # Output: Giant Escape 3 started silently!

car = Car("Bmw", "X5")
print(car.start())  # Output: Vehicle started