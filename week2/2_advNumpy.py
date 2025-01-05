# broadcasting in numpy
# It is a feature in NumPy that allows arithmetic or logical operations to be performed on arrays of different shapes without the need for manually repeating the elements of the smaller array.

print('\n------broadcasting in numpy-----\n')

# rules for broadcasting:
# -> dimensions are aligned from the right
# -> a dimension is compatible if:
# --> it matches the other array's dimensions
# --> one of the dimensions is 1

print('\n-----array and scalar broadcasting-----\n')
import numpy as np

arr = np.array([1, 2, 3])

print('initial array :',arr)
print('\n broadcast numbers (10) to each element of array :', arr+10)

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

print('\n initial array/matrix 2x3 :\n',arr1)

print('\n sum of matrix 2x3 :\n',np.sum(arr1))
print('\n mean of matrix 2x3 :\n',np.mean(arr1))
print('\n max of matrix 2x3 :\n',np.max(arr1))
print('\n min of matrix 2x3 :\n',np.min(arr1))
print('\n standard deviation of matrix 2x3 :\n',np.std(arr1))
print('\n sum along rows of matrix 2x3 :\n',np.sum(arr1,axis=1))
print('\n sum along columns of matrix 2x3 :\n',np.sum(arr1,axis=0))

# booleans indexing and filtering
# booleans and condition use to filtering element from an array
print('\n ----booleans indexing and filtering-----\n')

arr2 = np.array([1,2,3,4,5,6])

evens = arr2[arr2 % 2 == 0] # arr2[arr2 % 2 == 0] => [False, True, False, True, False, True] => [2,4,6]

print('\ninitial array : \n',arr2)
print('\nevens :\n',evens)

# modified array

arr2[arr2 > 3] = 0
print('modified array : \n',arr2)

# generating random  number and setting seeds

print('\n ----generating random  number and setting seeds-----\n')

random_arr = np.random.rand(3,2)

print('\n initial random array/matrix 3x2: \n',random_arr)

random_int = np.random.randint(0,10,size=(3,4))

print('\n random integer array/matrix 3x4 with range 0-10: \n',random_int)

print('\n set seed to 42')

np.random.seed(42)

random_seed = np.random.rand(3,4)

print('\n random array/matrix 3x4 with seed = 42 :\n',random_seed)
random_seed_int = np.random.randint(0,10,size=(4,5))

print('\n random integer array/matrix 4x5 with seed = 42 :\n',random_seed_int)


