#Problem 1
class Book:
    def __init__(self,title,author,available_copies):
        self.title= title
        self.author= author
        self.available_copies= available_copies


class Library:
    def __init__(self):
        self.inventory={}

    def add_book(self,book_object):
        self.inventory[book_object.title]= book_object
    def borrow_book(self,title):
        if title in self.inventory:
            book= self.inventory[title]
            if book.available_copies>0:
                book.available_copies-=1
                print(f"Success: You borrowed '{title}'. Copies remaining: {book.available_copies}")
            else:
                print(f"Sorry, '{title}' is currently out of stock.")
        else:
            print(f"Error, '{title}' is not in the library inventory.")

# --- TEST SCRIPT ---

# 1. Create a library instance
my_library = Library()

# 2. Create sample book objects
book1 = Book("The Hobbit", "J.R.R. Tolkien", 2)
book2 = Book("1984", "George Orwell", 1)

# 3. Add books to the library inventory
my_library.add_book(book1)
my_library.add_book(book2)

# 4. Test borrowing a book that is in stock
print("--- Test 1: Borrow 'The Hobbit' (Expect Success) ---")
my_library.borrow_book("The Hobbit") 

# 5. Test borrowing the last copy of a book
print("\n--- Test 2: Borrow '1984' (Expect Success) ---")
my_library.borrow_book("1984") 

# 6. Test borrowing a book that is now out of stock
print("\n--- Test 3: Borrow '1984' again (Expect Out of Stock) ---")
my_library.borrow_book("1984") 

# 7. Test borrowing a book that does not exist
print("\n--- Test 4: Borrow a non-existent book (Expect Error) ---")
my_library.borrow_book("Harry Potter")

#Problem 2
class Student:

    # Step 1 & Step 2
    def __init__(self, name, student_id):
        self.profile = (name, student_id)   # Tuple (immutable)
        self.grades = []                    # Empty list

    # Step 3
    def add_grade(self, subject, score):
        self.grades.append((subject, score))

    # Step 4
    def get_average(self):
        if len(self.grades) == 0:
            return 0

        total = 0
        for subject, score in self.grades:
            total += score

        return total / len(self.grades)


# ---------------- TEST ----------------

student1 = Student("Arslaan", "CSE101")

student1.add_grade("Math", 90)
student1.add_grade("Physics", 85)
student1.add_grade("Python", 95)

print("Student Profile:", student1.profile)
print("Grades:", student1.grades)
print("Average Marks:", student1.get_average())