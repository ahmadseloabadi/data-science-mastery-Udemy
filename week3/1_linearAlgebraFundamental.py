import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print('\n initial matrix a :\n',a)
print('\n initial matrix b :\n',b)

print('\n additional matrix :\n',a + b)
print('\n subtraction matrix :\n',a - b)

scalar_a = 2 * a

print('\n scalar multiplication:\n',scalar_a)

matrix_multi = np.dot(a,b)
# syarat dot 
# Jumlah kolom dari matriks pertama (a.shape[1]) harus sama dengan jumlah baris dari matriks kedua (b.shape[0]).
# karena oprasinya baris x kolom = baris matrix pertama x kolom matrix kedua
# ex: matrix 2x3 denan 3x2
print('\n matrix multiplication:\n',matrix_multi)

# Baris 1, Kolom 1: (1⋅5)+(2⋅7)=19
# Baris 1, Kolom 2: (1⋅6)+(2⋅8)=22
# Baris 2, Kolom 1: (3⋅5)+(4⋅7)=43
# Baris 2, Kolom 2: (3⋅6)+(4⋅8)=50

# another example
# Matriks A: 2x3
A = np.array([[1, 2, 3],
              [4, 5, 6]])

# Matriks B: 3x4
B = np.array([[7, 8,9,10],
              [9, 10,11,12],
              [11, 12,13,14]])

print('\n initial matrix A :\n',A)
print('\n initial matrix B :\n',B)

# Perkalian matriks
matrix_multi2 = np.dot(A, B)
print('\n matrix multiplication:\n',matrix_multi2)

# special matrix

# indentity matrix /matrix identitas

I = np.eye(3)
print('\n identity matrix:\n',I)

# zero matrix

Z = np.zeros((3,3))

print('\n zero matrix:\n',Z)

D = np.diag([1,2,3])

print('\n diagonal matrix:\n',D)

# exercise 

# create matrix and vector

M = np.array([[1,2,3],[4,5,6],[7,8,9]])
V = np.array([1,0,-1])

# matrix-vector multiplication
print('\n initial matrix M :\n',M)
print('\n initial matrix zero Z :\n',Z)
matrix_vector_multi = np.dot(M, V)
print('\n matrix multiplication:\n',matrix_vector_multi)

# practice

