#Dictionary Syntax and Key-Value Mapping ({})

A dictionary stores data as key-value pairs. It is created using curly braces {}, where each key is unique and maps to a value.

#Example:

student = {
    "name": "Arslaan",
    "age": 20,
    "course": "B.Tech"
}

print(student["name"])   # Arslaan

#The .get() Method and Handling Missing Keys Safely

The .get() method retrieves the value for a key. If the key does not exist, it returns None (or a default value if provided) instead of causing an error.

#Example:

student = {"name": "Arslaan"}

print(student.get("name"))          # Arslaan
print(student.get("age"))           # None
print(student.get("age", 0))        # 0

#Looping Through Dictionaries

You can loop through a dictionary to access its keys, values, or key-value pairs.

#Example:

student = {
    "name": "Arslaan",
    "age": 20
}

for key, value in student.items():
    print(key, value)

#Safe Data with Tuples and Tuple Unpacking

A tuple is an ordered collection of items that cannot be changed (immutable). Tuples are created using parentheses ().

Tuple unpacking allows you to assign tuple values to multiple variables in one step.

#Example:

person = ("Arslaan", 20)

name, age = person

print(name)   # Arslaan
print(age)    # 20

Tuples are useful for storing fixed data, while tuple unpacking makes it easy to extract multiple values at once.