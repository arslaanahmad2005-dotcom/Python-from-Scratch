#1. Introduction to NumPy (10 Minutes)
#What is NumPy?

NumPy stands for Numerical Python.

It is a Python library used to perform fast mathematical operations on arrays.

Instead of storing one value at a time like normal Python variables, NumPy stores many values together inside an object called an ndarray (N-Dimensional Array).

#Example

import numpy as np

arr = np.array([10,20,30,40])
print(arr)

Output

[10 20 30 40]
Why NumPy is used in Data Science?

Almost every Data Science library uses NumPy internally.

Examples:

Pandas
Scikit-learn
TensorFlow
PyTorch
OpenCV

Because datasets are basically collections of numbers.

Example

Student Marks

90
85
78
65
88

NumPy stores them efficiently.

Why not use Python Lists?

Python List

marks = [90,85,78,65]

Looks simple.

But internally...

Every element is stored separately.

Memory consumption is high.

Operations are slow.

NumPy Array

marks = np.array([90,85,78,65])

Stores data continuously in memory.

#Benefits:

✅ Less memory

✅ Faster calculations

✅ Easy mathematical operations

#Example

Python List

marks = [10,20,30]

print(marks*2)

Output

[10,20,30,10,20,30]

It repeats the list.

NumPy

arr=np.array([10,20,30])

print(arr*2)

Output

[20 40 60]

Each element is multiplied.

This is called Vectorization.

#What is ndarray?

#Full form:

#N-Dimensional Array

It is the main object of NumPy.

Everything in NumPy is stored inside ndarray.

Example

arr=np.array([1,2,3])

print(type(arr))

Output

<class 'numpy.ndarray'>
2. Array Dimensions (10 Minutes)

Dimensions tell how data is organized.

1D Array

One row.

Example

arr=np.array([10,20,30])

Looks like

[10 20 30]

Think of it as a straight line.

Dimension = 1

2D Array

Rows and Columns

Example

arr=np.array([[1,2,3],
              [4,5,6]])

Looks like

1 2 3
4 5 6

Dimension = 2

Think of an Excel sheet.

#3D Array

Collection of multiple 2D arrays.

Example

arr=np.array([
 [[1,2],[3,4]],

 [[5,6],[7,8]]
])

Visualization

Layer 1

1 2
3 4

Layer 2

5 6
7 8

Dimension = 3

Difference Between Dimensions
Dimension	Structure	Example
1D	Line	[1,2,3]
2D	Table	[[1,2],[3,4]]
3D	Stack of Tables	[[[1,2],[3,4]],[[5,6],[7,8]]]
3. Creating Arrays (15 Minutes)

First import NumPy

import numpy as np
np.array()

Creates an array from Python data.

arr=np.array([1,2,3])

print(arr)

Output

[1 2 3]
np.zeros()

Creates an array filled with 0.

arr=np.zeros((2,3))

print(arr)

Output

[[0. 0. 0.]
 [0. 0. 0.]]
np.ones()

Creates an array filled with 1.

arr=np.ones((2,2))

print(arr)

Output

[[1. 1.]
 [1. 1.]]
np.arange()

Works like Python's range() but returns a NumPy array.

arr=np.arange(1,10)

Output

[1 2 3 4 5 6 7 8 9]

With step

arr=np.arange(0,20,2)

Output

0 2 4 6 8 10 12 14 16 18
np.linspace()

Creates evenly spaced numbers between a start and end value.

Syntax

np.linspace(start,end,total_numbers)

Example

arr=np.linspace(1,10,5)

print(arr)

Output

[1.   3.25 5.5  7.75 10.]

Unlike arange(), linspace() includes the ending value by default.