# Matrix Algebra

#PLACE YOUR CODE HERE

import numpy as np
A = np.array([[1,2,3], [2,7,4]])
B = np.array([[1,-1], [0, 1]])
C = np.array([[5, -1], [9, 1], [6, 0]])
D = np.array([[3, -2, -1], [1, 2, 3]])
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([[1],[8],[0],[5]])
list = [A, B, C, D, u, v, w]
#Matrix Dimensions
print("1.1", A.shape)
# 1.1 (2, 3)
print("1.2", B.shape)
# 1.2 (2, 2)
print("1.3", C.shape)
# 1.3 (3, 2)
print("1.4", D.shape)
# 1.4 (2, 3)
print("1.5", u.shape)
# 1.5 (4,)
print("1.6", w.shape)
# 1.6 (4, 1)
#Vector Operations
print("2.1", u + v)
# 2.1 [ 9  7 -4  9]
print("2.2", u - v)
# 2.2 [ 3 -3 -2  1]
print("2.3", 6 * u)
# 2.3 [ 36  12 -18  30]
print("2.4", u @ v)
# 2.4 51
print("2.5", np.linalg.norm(u))
# 2.5 8.60232526704
#Matrix Operations
#print(A + C)
print("3.1 - not defined")
# 3.1 - not defined
print("3.2", A - C.transpose())
# 3.2 [[-4 -7 -3]
# [ 3  6  4]]
print("3.3", C.transpose() + (3 * D))
# 3.3 [[14  3  3]
# [ 2  7  9]]
print("3.4", np.dot(B, A))
# 3.4 [[-1 -5 -1]
# [ 2  7  4]]
#print(np.dot(B, A.transpose()))
print("3.5 - not defined")
# 3.5 - not defined
#Optional
#print(np.dot(B, C))
print("3.6 - not defined")
# 3.6 - not defined
print("3.7", np.dot(C, B))
# 3.7 [[ 5 -6]
# [ 9 -8]
# [ 6 -6]]
print("3.8", np.linalg.matrix_power(B, 4))
# 3.8 [[ 1 -4]
# [ 0  1]]
print("3.9", np.dot(A, A.transpose()))
# 3.9 [[14 28]
# [28 69]]
print("3.10", np.dot(D.transpose(), D))
# 3.10 [[10 -4  0]
# [-4  8  8]
# [ 0  8 10]]



'''
















'''