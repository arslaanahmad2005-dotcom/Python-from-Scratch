#Problem 1
full_name=input("Enter your full name: ")
modified_name= full_name.strip().upper()
print(f"Your name in capital letters is: {modified_name}")

#Problem 2
sentence="The secret password is 'Skyblue123'"
secured_sentence= sentence.replace("Skyblue123","[REDACTED]")
print(secured_sentence)

