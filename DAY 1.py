import numpy as np
a = np.array([[1,2,3],[3,4,55],[-7,-1,-2]])
b = np.array([[2,4,5],[4,6,8],[3,2,-1]])
# Matrix addition
c = a+b
# matrix substraction
d = a-b
# scalar multiplication
e = 2*a
# matrix multiplication
m1 = np.matmul(a,b)
m2 = np.matmul(b,a)
print(f"Multiplication of a and b {np.matmul(a,b)}")
print(f"Multiplication of a and b {np.matmul(b,a)}")

# Inverse of a matrix
i1 = np.linalg.inv(a)
print(f"inverse of matrix a {i1}")

# to confirm that it is inverse the product of a and i1 should give an identity matrix
result = np.matmul(a, i1)
print(np.round(result, 2))

# Transpose
t1 = np.transpose(a)
print(t1)