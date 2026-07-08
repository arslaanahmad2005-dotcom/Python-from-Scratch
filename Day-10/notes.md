#Classes and Objects

A class is a blueprint for creating objects, while an object is an actual instance of a class. Think of a class as a cookie mold and an object as the cookie made from that mold.

#Example:

#class Student:
    pass

student1 = Student()   # Object
student2 = Student()   # Another object

#The __init__() Method & Attributes

The __init__() method is a special constructor that is automatically called when an object is created. It initializes the object's attributes (data).

#Example:

#class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Arslaan", 20)

print(student.name)
print(student.age)

#Methods (Object Actions)

Methods are functions defined inside a class. They describe the actions or behavior of an object. The first parameter is always self, which refers to the current object.

#Example:

#class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

student = Student("Arslaan")
student.greet()

#Using a List or Dictionary Inside a Class

A class can use lists or dictionaries as attributes to store multiple values.

#Example (List):

#class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(name)

room = Classroom()
room.add_student("Arslaan")
room.add_student("Ali")

print(room.students)

Example (Dictionary):

#class Student:
    def __init__(self):
        self.marks = {}

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

student = Student()
student.add_mark("Math", 95)

print(student.marks)

#Using lists and dictionaries inside classes helps organize and manage collections of related data efficiently.