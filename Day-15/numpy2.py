import numpy as np
#Task 1
arr1=np.arange(1,11)
arr2=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
arr3 = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])
print(arr1[0])
print(arr1[-1])
print(arr1[5])
print(arr2[2:])
print(arr2[:1])
print(arr3[0:1])
#Task 2
# Create a 5×5 matrix
matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

print("Original Matrix:\n", matrix)

# First row
print("\nFirst Row:")
print(matrix[0])

# Last row
print("\nLast Row:")
print(matrix[-1])

# First column
print("\nFirst Column:")
print(matrix[:, 0])

# Last column
print("\nLast Column:")
print(matrix[:, -1])

# Middle 3×3 sub-matrix
print("\nMiddle 3x3 Sub-Matrix:")
print(matrix[1:4, 1:4])

# Reverse the rows
print("\nReverse the Rows:")
print(matrix[::-1])

# Reverse the columns
print("\nReverse the Columns:")
print(matrix[:, ::-1])
#Task 3
# Create a 1D array of 12 elements
ar = np.arange(1, 13)

print("Original Array:")
print(ar)

# Reshape into 3×4
arr_3x4 = ar.reshape(3, 4)
print("\n3x4 Matrix:")
print(arr_3x4)

# Reshape into 2×6
arr_2x6 = ar.reshape(2, 6)
print("\n2x6 Matrix:")
print(arr_2x6)

# Reshape into 4×3
arr_4x3 = ar.reshape(4, 3)
print("\n4x3 Matrix:")
print(arr_4x3)

# Flatten each reshaped array
print("\nFlatten 3x4:")
print(arr_3x4.flatten())

print("\nFlatten 2x6:")
print(arr_2x6.flatten())

print("\nFlatten 4x3:")
print(arr_4x3.flatten())

# Transpose the 3×4 matrix
print("\nTranspose of 3x4 Matrix:")
print(arr_3x4.T)
