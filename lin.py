import numpy as np
from numpy.linalg import solve

A = np.array([[1.,2], [3,4]])
b = np.dot(A, np.array([8.,9]))

print "solving for Ax=b"

print solve(A,b)
