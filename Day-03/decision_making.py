#Problem 1
age=int(input("Enter the age of yours\n"))
if(0<age<12):
    print("Ticket Category: Child(Free)")
elif(12<=age<=64):
    print("Ticket Category: Adult($10)")
elif((age>=65)):
    print("Ticket Category: Senior($5)")
else:
    print("Invalid age")

#Problem 2
num=int(input("Enter any whole number\n"))
if(num>=0):
    if(num%2==0):
        print(f"The number {num} is even")
    else:
        print(f"The number {num} is odd")
else:
    print("Please enter a whole number")