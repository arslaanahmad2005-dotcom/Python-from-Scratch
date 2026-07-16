#1. Indexing (10 Minutes)
What is Indexing?

Indexing means accessing a specific element of an array using its position.

#Remember:

Indexing starts from 0.
Every element has an index.

#Example:

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

#Positions:

Index:   0   1   2   3   4
Value:  10  20  30  40  50
Positive Indexing

Positive indexing starts from the left.

print(arr[0])

Output:

10
print(arr[2])

#Output:

30
print(arr[4])

#Output:

50
Negative Indexing

Negative indexing starts from the right.

Index:  -5  -4  -3  -2  -1
Value:  10  20  30  40  50

#Example:

print(arr[-1])

Output:

50
print(arr[-2])

Output:

40
print(arr[-5])

Output:

10

#Negative indexing is useful when you want elements from the end without knowing the array length.

#Accessing Elements in a 1D Array
arr = np.array([5, 10, 15, 20])

print(arr[0])
print(arr[2])
print(arr[-1])

Output:

5
15
20
Accessing Elements in a 2D Array

A 2D array has rows and columns.

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

#Visualization:

      Col
      0 1 2

Row 0 1 2 3
Row 1 4 5 6

#Syntax:

arr[row, column]

Examples:

print(arr[0, 0])

Output:

1
print(arr[0, 2])

Output:

3
print(arr[1, 1])

Output:

5
Accessing Elements in a 3D Array

A 3D array contains multiple 2D arrays (layers).

arr = np.array([
    [
        [1,2],
        [3,4]
    ],

    [
        [5,6],
        [7,8]
    ]
])

#Visualization:

Layer 0

1 2
3 4

Layer 1

5 6
7 8

#Syntax:

arr[layer, row, column]

#Examples:

print(arr[0,0,1])

Output

2
print(arr[1,1,0])

Output

7
#2. Slicing (10 Minutes)
#What is Slicing?

#Slicing means extracting multiple elements from an array.

#Syntax:

array[start:stop:step]

#Where:

start → starting index (included)
stop → ending index (excluded)
step → jump size
Basic Slicing
arr = np.array([10,20,30,40,50,60])
print(arr[1:4])

#Output:

[20 30 40]

#Explanation:

#Starts from index 1 and stops before index 4.

print(arr[:3])

Output:

[10 20 30]

Start defaults to 0.

print(arr[3:])

Output:

[40 50 60]

Stop defaults to the last element.

Step Size
print(arr[::2])

#Output:

[10 30 50]

It selects every second element.

Reverse Slicing
print(arr[::-1])

Output:

[60 50 40 30 20 10]

A step of -1 reverses the array.

Row Slicing (2D)
arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(arr[1:])

Output:

[[4 5 6]
 [7 8 9]]
Column Slicing
print(arr[:,1])

Output:

[2 5 8]

Explanation:

: means all rows.
1 means the second column.
Sub-array (Matrix Slicing)
print(arr[0:2, 1:3])

Output:

[[2 3]
 [5 6]]

Explanation:

Rows: 0 and 1

Columns: 1 and 2

#3. Reshaping Arrays (10 Minutes)
What is Reshaping?

Reshaping changes the shape of an array without changing its data.

reshape()

Example:

arr = np.arange(12)

print(arr)

Output:

[0 1 2 3 4 5 6 7 8 9 10 11]

Now reshape it.

new_arr = arr.reshape(3,4)

print(new_arr)

Output:

[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

The data remains the same, only the structure changes.

When is Reshaping Possible?

The total number of elements must stay the same.

Example:

12 elements can become:

3 × 4
2 × 6
6 × 2
4 × 3

But 12 cannot become 5 × 3, because 5 × 3 = 15.

flatten()

Converts a multidimensional array into a new 1D copy.

arr = np.array([[1,2],[3,4]])

flat = arr.flatten()

print(flat)

Output:

[1 2 3 4]

Changes to flat do not affect the original array.

ravel()

Also converts to 1D, but it usually returns a view of the original array instead of a copy.

flat = arr.ravel()

ravel() is generally faster and uses less memory.

Difference:

flatten() → Copy of the data.
ravel() → Usually a view of the original data.
#4. Transpose (5 Minutes)
What is Transpose?

Transpose swaps rows and columns.

Example:

arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr.T)

Output:

[[1 4]
 [2 5]
 [3 6]]

Original shape:

2 × 3

After transpose:

3 × 2
transpose()

You can also write:

arr.transpose()

It gives the same result as:

arr.T
Why is Transpose Useful?

Transpose is commonly used in:

Machine Learning
Data Analysis
Matrix Multiplication
Linear Algebra
Deep Learning
Image Processing

Many mathematical operations require rows and columns to be swapped before calculations.