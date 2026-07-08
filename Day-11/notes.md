#Inheritance

Inheritance allows a new class (child class) to inherit the properties and methods of an existing class (parent class). It promotes code reusability and reduces duplication.

#Example:

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()

#The super() Function

The super() function is used to call the parent class's methods or constructor (__init__) from the child class. It helps avoid rewriting code.

#Example:

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

dog = Dog("Tommy")
print(dog.name)

#Method Overriding

Method overriding occurs when a child class provides its own implementation of a method that already exists in the parent class.

#Example:

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()

#Encapsulation & Private Attributes

Encapsulation is the process of hiding an object's data and allowing access only through its methods. In Python, a private attribute is created by adding two underscores (__) before its name.

#Example:

#class Student:
    def __init__(self, name):
        self.__name = name   # Private attribute

    def get_name(self):
        return self.__name

student = Student("Arslaan")
print(student.get_name())

#Encapsulation protects data from being modified directly and makes programs more secure and easier to maintain.