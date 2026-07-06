#The for Loop: Stepping Through Collections

The for loop is used to iterate through each item in a collection, such as a list, tuple, or string. It executes the block of code once for every item.

#The enumerate() Function: Keeping Track of Item Indexes

The enumerate() function returns both the index and the value of each item while looping through a collection.

Example:

fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

#The Accumulator Pattern: Filtering and Calculating Totals

The accumulator pattern uses a variable to collect or calculate results while looping through data, such as finding a sum or counting items.

Example:

numbers = [10, 20, 30, 40]
total = 0

for num in numbers:
    total += num

print(total)   # 100

#The range() Function: Generating Custom Sequences of Numbers

The range() function generates a sequence of numbers and is commonly used with for loops.

range(5) → 0, 1, 2, 3, 4
range(1, 6) → 1, 2, 3, 4, 5
range(1, 10, 2) → 1, 3, 5, 7, 9

Example:

for i in range(1, 6):
    print(i)