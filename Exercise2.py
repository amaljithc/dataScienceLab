#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
print("Enter the entries in a single line (separated by space): ")
entries = list(map(int, input().split()))
m1= np.array(entries).reshape(R, C)
print(m1)
print("------------------------------------------------------------")
R1 = int(input("Enter the number of rows:"))
C1 = int(input("Enter the number of columns:"))
print("Enter the entries in a single line (separated by space): ")
entries = list(map(int, input().split()))
m2 = np.array(entries).reshape(R1, C1)
print(m2)
print("------------------------------------------------------------")
m3=m1.dot(m2)
print("dot product is:")
print(m3)
print("------------------------------------------------------------")
m4=m1.transpose()
print("transpose of matrix1:")
print(m4)
m5=m2.transpose()
print("transpose of matrix2:")
print(m5)
print("------------------------------------------------------------")
m6=m1.trace()
print("trace of matrix1:")
print(m6)
m7=m2.trace()
print("trace of matrix2:")
print(m7)
print("------------------------------------------------------------")
rank1 = np.linalg.matrix_rank(m1)
print("Rank of the given Matrix1 is : ",rank1)
rank2 = np.linalg.matrix_rank(m2)
print("Rank of the given Matrix2 is : ",rank2)
print("------------------------------------------------------------")
det1 = np.linalg.det(m1)
print("Determinant of given matrix1:")
print(det1)
det2 = np.linalg.det(m2)
print("Determinant of given matrix2:")
print(det2)
print("------------------------------------------------------------")
print("inverse of given matrix1:")
print(np.linalg.inv(m1))
print("inverse of given matrix2:")
print(np.linalg.inv(m2))
print("------------------------------------------------------------")
w, v = np.linalg.eig(m1)
  
print("Printing the Eigen values of the given square array:\n",
      w)

print("Printing Right eigenvectors of the given square array:\n",
      v)
x, y = np.linalg.eig(m2)
  
print("Printing the Eigen values of the given square array:\n",
      x)

print("Printing Right eigenvectors of the given square array:\n",
      y)

