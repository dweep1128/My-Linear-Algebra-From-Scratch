import numpy as np

# Multiplying two array without numpy
r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]

s1 = [1,2,1]
s2 = [2,3,4]
s3 = [4,2,1]

A = []
B = []
A.append(r1)
A.append(r2)
A.append(r3)

B.append(s1)
B.append(s2)
B.append(s3)

C = [[0,0,0],[0,0,0],[0,0,0]]
dim = 3

# C[i][j] is the dot product of the ith row of A and jth column of B
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            C[i][j] = C[i][j] + A[i][k] * B[k][j]
print(C)

# Check for upper triangular matrix
A1 = np.array([[0,0,0],[-2,0,0],[3,-4,0]])
dim = len(A1)
k = 0
for i in range(dim):
    for j in range(dim):
        if(i>j):
            if(A1[i][j] != 0):
                k=1
                break
    if k == 1:
        break
if(k == 0):
    print("It is an upper triangular matrix")
else:
    print("It is not an upper triangular matrix")

# chk for skew symmetric matrix
N1 = np.array([[0,2,-3],[-2,0,4],[3,-4,0]])
N2 = np.transpose(-N1)
if np.array_equal(N1,N1):
    print("it is skew symmetric matrix")
else:
    print("It is not a skew symmetric matrix")

