#Problem 1
def find_student_score(dictionary,name):
    return dictionary.get(name)

student_dictionary={
    "Rahul":75,
    "Sonu":87,
    "Meena":78,
    "Raj":98
}
print(find_student_score(student_dictionary,"Raj"))
print(find_student_score(student_dictionary,"Ayush"))

#Problem 2
def count_occurences(item_list):
    counts={}
    for item in item_list:
        if item in counts:
            counts[item]+=1
        else:
            counts[item]=1

    print("Occurences Summary\n")
    for item,count in counts.items():
        print(f"{item}: {count}")
    return counts
choices=["A","B","C","A","B","A"]
result_dict=count_occurences(choices)

