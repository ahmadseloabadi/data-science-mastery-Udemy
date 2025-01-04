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

reshaped = arr1.reshape((3,2))

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



