import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

#Array Indexing

arr = np.array([1, 2, 3, 4])
print(arr[0])

arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])

#2D Array Indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])
