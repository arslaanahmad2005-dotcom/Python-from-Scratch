#Problem 1
class Engine:
    def start(self):
        return "Vroom!"


class Wheels:
    def roll(self):
        return "Wheels are spinning."


class Vehicle:
    def __init__(self):
        self.engine = Engine()
        self.wheels = Wheels()

    def drive(self):
        print(self.engine.start())
        print(self.wheels.roll())


# Test
vehicle = Vehicle()
vehicle.drive()

#Problem 2
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


class Library:
    def __init__(self, books):
        self.books = books

    def __len__(self):
        return len(self.books)


# Test
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book3 = Book("1984", "George Orwell", 328)

library = Library([book1, book2, book3])

# Compare books
print(book1 == book2)

# Print book
print(book1)

# Length of library
print(len(library))