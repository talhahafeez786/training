# Base class 1
class Engine:
    def start_engine(self):
        return "Engine started"

# Base class 2
class Radio:
    def play_music(self):
        return "Playing music"

# Derived class
class Car(Engine, Radio):
    def drive(self):
        return "Car is driving"

# Creating an object of the Car class
my_car = Car()

# Using methods from multiple base classes
print(my_car.start_engine())  # Output: Engine started
print(my_car.play_music())    # Output: Playing music
print(my_car.drive())         # Output: Car is driving
