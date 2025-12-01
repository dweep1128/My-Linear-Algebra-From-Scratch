import numpy as np
from sympy import matrices, Matrix

A = np.array([
    [2,4,3],
    [1,2,3],
    [4,8,10]
])

sympy_matrix_pre_rref = Matrix(A)

matrix_post_rref = sympy_matrix_pre_rref.rref()
# The above line of code will return a tuple with the rref matrix and the column of
# the leading ones

rref_matrix = matrix_post_rref[0]
# With this we select the first element of our tupple that is the requires rref

numpy_rref_matrix = np.array(rref_matrix, dtype=int)
# It translates your data from the "Symbolic Math" world (SymPy) to the
# "Numeric Computing" world (NumPy).
print(numpy_rref_matrix)