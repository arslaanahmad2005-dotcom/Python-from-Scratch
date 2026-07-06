#What is a List?

A list is a collection of items stored in a single variable. Lists can contain different data types (numbers, strings, etc.) and are written using square brackets [].

#List Indexing and Slicing

Lists use indexing and slicing just like strings.

Indexing: Access a single item using its position.
list[0] → First item
list[-1] → Last item
Slicing: Extract a portion of the list using list[start:stop].
The stop index is not included.

#Mutability and Essential List Methods

Lists are mutable, which means you can add, remove, or change their elements after they are created.

Common built-in methods:

.append(item) → Adds an item to the end of the list.
.insert(index, item) → Inserts an item at a specified position.
.pop(index) → Removes and returns the item at the given index (last item by default).
len(my_list) → Returns the total number of items in the list.