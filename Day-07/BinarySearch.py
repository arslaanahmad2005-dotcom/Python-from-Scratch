# 1. Get and sort the user list
nums = sorted([int(x) for x in input("Enter numbers: ").split()])
target = int(input("Enter number to find: "))
print(f"Sorted list: {nums}")

# 2. Binary search logic
low, high, index = 0, len(nums) - 1, -1

while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
        index = mid
        break  # Stop early if found
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

# 3. Print result
print(f"Found at index: {index}" if index != -1 else "Not found")
