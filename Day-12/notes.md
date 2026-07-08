#1. Polymorphism

#Polymorphism means "many forms." It allows different classes to use the same method name but perform different actions. Python often uses Duck Typing: if an object has the required method, it can be used.

#Example:

class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

for animal in [Dog(), Cat()]:
    animal.speak()

#2. Abstract Base Classes (ABCs)

#An Abstract Base Class (ABC) is a blueprint for other classes. It is created using the abc module and the @abstractmethod decorator. An abstract class defines methods that child classes must implement.

#Example:

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

#3. Implementing Interfaces

An abstract class cannot be instantiated directly. Any child class that inherits from it must override all abstract methods, otherwise it will also remain abstract.

#Example:

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()

#4. Concrete vs. Abstract Classes

#Concrete Class: A normal class that can be used to create objects directly.
Abstract Class: A class that serves as a blueprint and cannot be instantiated. It is meant to be inherited by other classes.

#Example:

class Car:      # Concrete class
    pass

# Animal (ABC) is an abstract class.
car = Car()     # Valid

#Abstract classes improve code structure by defining common behavior, while concrete classes provide the actual implementation and are used to create objects.