#1. Composition ("Has-A" Relationship)

#Composition means building a class by including objects of other classes. This represents a "Has-A" relationship.

#Example: A Car has an Engine, instead of Car is an Engine.

3Example:

#class Engine:
    def start(self):
        print("Engine started")

#class Car:
    def __init__(self):
        self.engine = Engine()

car = Car()
car.engine.start()

#2. Composition over Inheritance

#Modern software development often prefers composition over inheritance because it makes code:

More modular and reusable.
Less tightly coupled.
Easier to maintain and extend.
Free from deep and complex inheritance trees.

Use inheritance for an "Is-A" relationship and composition for a "Has-A" relationship.

#3. Magic (Dunder) Methods

#Magic methods (also called dunder methods) are special methods with double underscores (__) that let custom objects work with Python's built-in functions and operators.

a. __str__() vs. __repr__()
__str__() → Returns a user-friendly string representation.
__repr__() → Returns a developer-friendly representation, mainly for debugging.

#Example:

class Student:
    def __str__(self):
        return "Student Object"

student = Student()
print(student)
b. __eq__()

The __eq__() method defines how two objects are compared using the == operator.

#Example:

class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

s1 = Student("Arslaan")
s2 = Student("Arslaan")

print(s1 == s2)   # True
c. __len__()

The __len__() method allows a custom object to work with Python's built-in len() function.

#Example:

class Basket:
    def __init__(self):
        self.items = ["Apple", "Banana", "Mango"]

    def __len__(self):
        return len(self.items)

basket = Basket()
print(len(basket))   

#Magic methods make custom classes behave like Python's built-in objects, making code more natural and easier to use.