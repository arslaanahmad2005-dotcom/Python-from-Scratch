#Problem 1
Guests=["Alice","Bob","Charlie"]
Guests.append("David")
Guests[1]="Eve"
print("Final list: ",Guests)
print("Total number of guests: ",len(Guests))

#Problem 2
inventory=["laptop","mouse","keyboard","monitor","hdmi_cable"]
peripherals=inventory[1:4]
inventory.pop()
print(f"Updated inventory list: {inventory}")
print(f"New Peripherals list: {peripherals}")
