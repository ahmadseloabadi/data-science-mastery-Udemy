import numpy as np

arr = np.array([1,2,3,4])

print( '\ninitial array \n',arr)

zeros = np.zeros((3,4))

print('\ninitial zero array \n',zeros)

ones = np.ones((3,4))

print('\ninitial one array \n',ones)

range_arr = np.arange(1,10,2) # np.arange(start,stop,step)

print('\ninitial arange array \n',range_arr)

linspace_arr = np.linspace(0,10,5)

print('\ninitial linspace array \n',linspace_arr)

#  manipulating arrays
print('\n----manipulating array-----\n')

# change shape
print('\n change shape\n')

arr1 = np.array([1,2,3,4,5,6])

reshaped = arr1.reshape((3,2)) # reshaped(rows, columns)

print('\n initial array \n',arr1)
print('\n reshape array \n',reshaped)

# add dimension
print('\n add dimension\n')

arr2 = np.array([1,2,3])

expand_arr = arr2[:,np.newaxis]

print('\n expand array \n',expand_arr)

# basic operations in array
print('\n----- basic operation in array----- \n')

print('\n element wise operation in array\n')


print('\n mathematical operations in array\n')
a = np.array([1,2,3])
b = np.array([4,5,6])
print('\n initial array a\n',a)
print('\n initial array b\n',b)

print('\n additional of array a and b \n',a + b)
print('\n substraction of array a and b \n',a - b)
print('\n multiplication of array a and b \n',a * b)
print('\n devide of array a and b \n',a / b)

c = np.array([4,9,16,25])
print('\n initial array c\n',c)
print('\n square root of array c \n',np.sqrt(c))
print('\n sum of array c \n',np.sum(c))
print('\n mean of array c \n',np.mean(c))
print('\n max of array c \n',np.max(c))
print('\n min of array c \n',np.min(c))


# array indexing slicing and reshaping with numpy


print('\n----- indexing in array with numpy----- \n')

arr3 = np.array([10,20,30,40,50,60])
print('initial array with numpy :',arr3)
print('index 0 in array :',arr3[0])
print('index -1 in array :',arr3[-1])

print('\n----- slicing in array with numpy----- \n')
print('slicing [1:4] in array :',arr3[1:4])
print('slicing [:3] in array :',arr3[:3])
print('slicing [1:] in array :',arr3[1:])

print('\n----- reshaping in array with numpy----- \n')
print('reshaping (2,3) in array :\n',arr3.reshape(2,3))
print('reshaping (3,2) in array :\n',arr3.reshape(3,2))

# exercise 
# generate array for basic mathematical operations

print('\n--- exercise ----- \n')
print('\n generate array for basic mathematical operations \n')
import numpy as np

ar1 = np.arange(1,6)
ar2 = np.arange(6,11)

print('\n initial array a\n',ar1)
print('\n initial array b\n',ar2)

print('\n additional of array a and b \n',ar1 + ar2)
print('\n substraction of array a and b \n',ar1 - ar2)
print('\n multiplication of array a and b \n',ar1 * ar2)
print('\n devide of array a and b \n',ar1 / ar2)

print('\n create 3x3 matrix and perform operations :\n')

matrix1 = np.array([[1,2,3],[4,5,6],[7,8,9]])

print('create 3x3 matrix1 :\n',matrix1)

# transpose matrix

transpose = np.transpose(matrix1)

print('transpose matrix :\n',transpose)

matrix2 = np.array([[9,8,7],[6,5,4],[3,2,1]])
print('create 3x3 matrix2 :\n',matrix2)

print('\n additional of matrix matrix1 and matrix2 \n',matrix1 + matrix2)
print('\n substraction of matrix matrix1 and matrix2 \n',matrix1 - matrix2)
print('\n multiplication of matrix matrix1 and matrix2 \n',matrix1* matrix2)
print('\n devide of matrix matrix1 and matrix2 \n',matrix1 / matrix2)






