#Problem 1
num=int(input("Enter a number for multipliction table: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

#Problem 2
secret=7
while(True):
    guess=int(input("Guess the number: "))
    if(guess==secret):
        print("Congrats guessing number is correct")
        break
    else:
        print("Try again")
