list=[]
for i in range(0,10):
    list.append(int(input("Enter a number: ")))
target=7
for i in range(0,len(list)):
    if(list[i]==target):
        print(f"{target} found at {i} index")
    else:
        print("Not found")