# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "some sound"

# Derived classSome sound
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow"

         
## Creating an object of the base class
animal = Animal("Generic Animal")
print(animal.speak())  # Output: Some sound

cat = Cat("lily")
print(cat.speak())

