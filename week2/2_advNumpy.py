# broadcasting in numpy


print('\n------broadcasting in numpy-----\n')

# rules for broadcasting:
# -> dimensions are aligned from the right
# -> a dimension is compatible if:
# --> it matches the other array's dimensions
# --> one of the dimensions is 1

print('array and scalar broadcasting\n')
import numpy as np

arr = np.array([1, 2, 3])

print('initial array :',arr)
print('broadcast numbers (10) to each element of array :', arr+10)

matrix = np.array([[1,2,3],[4,5,6]])
vector = np.array([1,0,1])

print('\n initial matrix 2x3 :\n', matrix)
print('\n initial vector :\n', vector)

print('\n additional matrix and vector:\n', matrix+vector)

# aggregate functions
# aggregate functions compute summary statistics for arrays
print('\n aggregate functions:\n')
print('common function\n')
arr1 = np.array([[1,2,3],[4,5,6]])

print('initial array/matrix 2x3 :\n',arr1)

print('\n sum of matrix 2x3 :\n',np.sum(arr1))
print('\n mean of matrix 2x3 :\n',np.mean(arr1))
print('\n max of matrix 2x3 :\n',np.max(arr1))
print('\n min of matrix 2x3 :\n',np.min(arr1))
print('\n standard deviation of matrix 2x3 :\n',np.std(arr1))
print('\n sum along rows of matrix 2x3 :\n',np.sum(arr1,axis=1))
print('\n sum along columns of matrix 2x3 :\n',np.sum(arr1,axis=0))

# booleans indexing and filtering
# booleans and condition use to filtering element from an array

arr2 = np.array([1,2,3,4,5,6])

evens = arr2[arr2 % 2 == 0]

print('\ninitial array : \n',arr2)
print('\nevens :\n',evens)


