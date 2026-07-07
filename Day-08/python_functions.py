#Problem 1
#Linear Search
def linear_search(target_list,target_item):
    for i in range(0,len(target_list)):
        if(target_list[i]==target_item):
            return i
    return -1

#Binary Search
# Binary Search
def binary_search(target_list, target_item):
    low = 0
    high = len(target_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if target_list[mid] == target_item:
            return mid
        elif target_list[mid] < target_item:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Main Program
list = [1,2,3,4,5,6,7,8,9]
target = 7

print(linear_search(list, target))
print(binary_search(list, target))

#Problem 2
def calculate_metrics(score_list):
    sum=0
    for i in score_list:
        sum=sum+i
    average=sum/len(score_list)
    maximum=max(score_list)
    print(f"The sum of all grades is: {sum}\nThe average is: {average}\nThe maximum grade is: {maximum}")
    return



grades=[57,87,97,100]
calculate_metrics(grades)
