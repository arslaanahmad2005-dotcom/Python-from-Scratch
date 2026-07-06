#String Indexing and Slicing

Strings are sequences of characters, and each character has an index starting from 0.

Indexing: Access a single character using square brackets [].
text[0] → First character
text[-1] → Last character (negative indexing)
Slicing: Extract a part of a string using text[start:stop].
The stop index is not included.

#Essential String Methods

Python provides built-in methods to work with strings. Since strings are immutable, these methods return a new string without changing the original.

.upper() → Converts all letters to uppercase.
.lower() → Converts all letters to lowercase.
.strip() → Removes leading and trailing spaces or newlines.
.replace("old", "new") → Replaces one substring with another.

#String Formatting (f-strings)

f-strings provide an easy and readable way to insert variables into a string. Add f before the string and place variables inside {}.