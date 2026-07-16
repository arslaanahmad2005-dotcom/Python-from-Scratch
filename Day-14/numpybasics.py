#Task 1
import numpy as np

# 1D Array
arr1 = np.array([10,20,30,40])

# 2D Array
arr2 = np.array([
    [1,2,3],
    [4,5,6]
])

# 3D Array
arr3 = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])

# Zeros
zeros = np.zeros((2,3))

# Ones
ones = np.ones((3,2))

# Arange
arr_range = np.arange(1,11)

# Linspace
arr_line = np.linspace(0,100,5)

print(arr1)
print(arr2)
print(arr3)
print(zeros)
print(ones)
print(arr_range)
print(arr_line)

#Task 2
arrays = [arr1, arr2, arr3, zeros, ones, arr_range, arr_line]

for i, arr in enumerate(arrays, start=1):
    print(f"\nArray {i}")
    print(arr)
    print("Shape:", arr.shape)
    print("Dimensions:", arr.ndim)
    print("Size:", arr.size)
    print("Data Type:", arr.dtype)

#Task 3
a=np.arange(1,21)
b=np.arange(0,100,2)
c=np.ones((3,3))
d=np.array([[1,2,3,4],[5,6,7,8]])
print(a)
print(b)
print(c)
print(d)