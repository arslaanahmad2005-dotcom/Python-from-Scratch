#Function Syntax and Reusability (def)

A function is a reusable block of code that performs a specific task. Functions are defined using the def keyword. You can pass data into a function using parameters and send data back using the return statement.

#Key Difference:

print() → Displays output on the screen.
return → Sends a value back to the program so it can be stored or used later.

#Example:

def add(a, b):
    return a + b

result = add(5, 3)
print(result)    # 8

#Variable Scope (Local vs. Global)

Variable scope determines where a variable can be accessed.

Local Variable: Created inside a function and can only be used within that function.
Global Variable: Created outside a function and can be accessed from anywhere in the program.

Using the correct scope helps avoid bugs and prevents functions from accidentally changing data.

#Example:

name = "Arslaan"   # Global variable
def greet():
    message = "Hello!"   # Local variable
    print(message)
    print(name)

greet()
print(name)
message is local and cannot be used outside greet().