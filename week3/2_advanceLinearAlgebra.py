# determinan and inverse matrix

import numpy as np
print('\n ---determinan matrix---\n')
# reference 
# https://www.ruangguru.com/blog/cara-mencari-determinan-dan-invers-matriks

A = np.array([[2,3],
              [4,5]])
deteminant= np.linalg.det(A)

print('\n initial matrix A:\n',A)
print('\n deteminant matrix A:\n',deteminant)

print('\n ---inverse matrix---\n')

inverse = np.linalg.inv(A)
print('\n inverse matrix A:\n',inverse)

# eigenvectors and  eigenvalues

eigenValues,eigenVectors = np.linalg.eig(A)
print('\n eigenValues:\n',eigenValues)
print('\n eigenVectors:\n',eigenVectors)

B = np.array([[4,2],[1,1]])
print('\n initial matrix B:\n',B)
eigenVal,eigenVec = np.linalg.eig(B)
print('\n eigenValues:\n',eigenVal)
print('\n eigenVectors:\n',eigenVec)

# matrix decomposition 

import numpy as np
from scipy.linalg import lu

print('\n LU Decomposition \n')
# Matriks A
A = np.array([[4, 3],
              [6, 3]])

# LU Decomposition
P, L, U = lu(A)

print("Matriks A:")
print(A)
print("\nLower Triangular Matrix (L):")
print(L)
print("\nUpper Triangular Matrix (U):")
print(U)

print('\n QR Decomposition \n')
# QR Decomposition
Q, R = np.linalg.qr(A)

print("\nMatriks A:")
print(A)
print("\nMatriks Q (Ortogonal):")
print(Q)
print("\nMatriks R (Segitiga Atas):")
print(R)

print('\n Cholesky Decomposition \n')

from numpy.linalg import cholesky

# Matriks harus simetris dan positif definit
B = np.array([[4, 2],
              [2, 3]])

# Cholesky Decomposition
L = cholesky(B)

print("\nMatriks B:")
print(B)
print("\nLower Triangular Matrix (L):")
print(L)

print('\n Singular Value Decomposition (SVD) \n')
# SVD
U, Sigma, VT = np.linalg.svd(A)

print("\nMatriks A:")
print(A)
print("\nMatriks U:")
print(U)
print("\nSingular Values (Sigma):")
print(Sigma)
print("\nMatriks V^T:")
print(VT)

print('\n Eigenvalue Decomposition \n')

# Eigenvalue Decomposition
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nMatriks A:")
print(A)
print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)

# notes 
# SVD dalam PCA:
# Reduksi dimensi untuk dataset yang memiliki banyak fitur.
# Digunakan untuk mengekstrak fitur yang paling relevan.

# LU dan Cholesky dalam Sistem Linear:
# Memecahkan persamaan linear besar dengan lebih efisien.

# Eigenvalue Decomposition dalam Spektral Clustering:
# Memahami hubungan dalam data berbasis graf.

# QR Decomposition dalam Regresi Linier:
# Digunakan untuk menghitung parameter model linier dengan stabilitas numerik lebih tinggi. 



