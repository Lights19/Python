from __future__ import division
import numpy as np


my_list1 = [3,2,4,5]

my_array= np.array(my_list1)
# output:array([3, 2, 4, 5])

my_list2= [11,22,33,44]
 
my_list=[my_list1,my_list2] #output:[[3, 2, 4, 5], [11, 22, 33, 44]]


#changing list to array
my_array= np.array(my_list)

''' output:array([[ 3,  2,  4,  5],
       [11, 22, 33, 44]]) '''


my_array.shape # output:(2,4) 2 row and 4 column


#making special class array
np.zeros(5) # array of 1X5 zeros

np.ones((5,5)) #array of 5X5 of ones


np.empty(5) # array of 1X5 zeros
np.empty((3,4)) # array of 3X4 zeros

np.eye(5) # 5X5 identity or diagonal matrix  with ones in diagonal 


###################################
#############more functions#######
##################################

#creating an array
arr=np.arange(5,20) #output:array([ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

#getting the value at and inxed
arr[5] #output:10
arr[0:5]# output:array([5, 6, 7, 8, 9])

#reassigning value
arr[0:3]=100#output:array([100, 100, 100,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17, 18,  19])

#taking care of floats


arr1=np.array([[3,5,9],[2,4,6]])

'''output:array([[3, 5, 9],
       [2, 4, 6]]'''

arr1*arr1 #multiplying array
arr1-arr1 #Subtracting array
#arithmatic operation with salars on array
1/arr1
arr1**3

#####################
###input and output###
######################

#Saving array on disk in binary format (file extension .npy)
np.save('my_array',arr1) # there will be a file ' my_array'in the folder

#Lets see the original saved copy
np.load('my_array.npy')

#Saving multiple arrays into a zip file
np.savez('two_arrays.npz',x=arr,y=arr) 

#Now loading multiple arrays
archieve_Array= np.load('two_arrays.npz')

#show
archieve_Array['x']


# Now lets remove them from the memory
#rm my_array.npy  # throws an error ???????????????
#rm two_aarays.npz


# Now saving and loading text files

arr2 = np.array([[1,2,3],[4,5,6]])
np.savetxt('test_text.txt',arr2,delimiter=',')
np.loadtxt('test_text.txt',delimiter=' ,')



#######################################
#####Array transposition#############
####################################

arr=np.arange(50).reshape((10,5)) # make a 10X5 matrix from range 0-50
arr.T # transpose


np.dot(arr.T,arr) # dot product

# for 3D matrix
arr3d= np.arange(50).reshape(5,5,2)

# trasnposing 3d matrix
arr3d.transpose((1,0,2))

# If you need to get more specific use swapaxes
arr = np.array([[1,2,3]])

#Show 
arr

arr.swapaxes(0,1)

#Important notes on Slices
slice_of_arr = arr[0:6]

#Show slice
slice_of_arr

#Change Slice
slice_of_arr[:]=99 # everything is repalce by 99

#Show Slice again
slice_of_arr

#To get a copy, need to be explicit
arr_copy = arr.copy()
arr_copy


# Indexing a 2D array

arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
arr_2d[1] # indexing 1st row
#output:array([20, 25, 30])
arr_2d[0] # indexing 0th row
#output:array([ 5, 10, 15])


# Format is arr_2d[row][col] or arr_2d[row,col]
#arr_2d[0,0] =arr_2d[0][0] =5

#Shape (2,2) from top right corner
arr_2d[:2,1:]
'''output:array([[10, 15],
       [25, 30]])'''

arr_2d[2]
#output:array([35, 40, 45])

#Shape bottom row
arr_2d[2,:]
#output: array([35, 40, 45])

# Fancy Indexing

#Set up matrix
arr2d = np.zeros((10,10))

#Length of array
arr_length = arr2d.shape[1]

#Set up array
for i in range(arr_length):
    arr2d[i] = i
print(arr2d)



#Fancy indexing allows the following
arr2d[[2,4,6,8]]

#Allows in any order
arr2d[[6,4,2,7]]

