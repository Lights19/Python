'''
Numpy: basics , array, functions, constants, formulas , random '''
import numpy as np
a=np.arange(5,16)
#array([ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])
a.dtype #dtype('int32')
a.shape #11
a.ndim # 1

z= np.zeros((3,6)) # gives 3X6 array of zeros
ez=np.empty((3,6)) # gives 3X6 array of zeros
ez+2 # 2 added
ez*1.25 # multiplication
ez+z # matrix addition
z.shape # dimension of z i.e. 3X6

b=np.array([[1,23,45],[56,6,7],[78,34,25]]) 
'''array([[ 1, 23, 45],
       [56,  6,  7],
       [78, 34, 25]])'''


b.ndim #2
b.shape #(3,3)

b[1] #elements of first row >array([56,  6,  7])

b[b<10] # elements <10 in array >array([1, 6, 7])

b>40
'''array([[False, False,  True],
       [ True, False, False],
       [ True, False, False]])'''

#some more operations
c= np.arange(4,16).reshape((3,4))
'''c
array([[ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])'''
np.sqrt(c) # square root of give array

np.where(c>10,2,c)  # replace elements >10 by 2 in c
np.where(c<=9,2,c) # similar as above
np.subtract(c,4) # subtract 4 from elemenst of c

np.sum(c) # 114
 #Return the cumulative sum of the elements along a given axis.
d= np.array([[1,2,3],[4,5,6]])
'''d > array([[1, 2, 3],
           [4, 5, 6]])
np.cumsum(d) #output: array([ 1,  3,  6, 10, 15, 21]) '''

np.cumprod(d) #Return the cumulative product of elements along a given axis.
'''
np.cumprod(d, dtype=float) # specify type of output
    array([   1.,    2.,    6.,   24.,  120.,  720.]) '''
    
np.argmin(d) #  Returns the indices of the minimum values along an axis.
np.argmax(d) # Returns the indices of the minimum values along an axis.

np.mean(d) #Compute the arithmetic mean along the specified axis.
ae = np.array([[1, 2], [3, 4]])
'''array([[1, 2],
       [3, 4]])'''
np.mean(ae) #output:  2.5 #diaginally i guess
np.mean(a, axis=0) #output:array([ 2.,  3.]) >>hint: from top
np.mean(a, axis=1)  #output:array([ 1.5,  3.5]) >> 
    
np.std(arr) #Compute the standard deviation along the specified axis.
np.var(arr) #Compute the standard deviation along the specified axis.

ab=np.random.normal() '''Draw random samples from a normal (Gaussian) distribution.
takes 3 parameters loc> mean or center, scale> sd  and 3rd  size is optional'''

#ac = np.random.randn(3,5,9) #Return a sample (or samples) from the standard normal distribution.

np.tile(arr,3)
'''tile(A, reps) >Construct an array by repeating A the number of times given by reps.
arr=np.arange(3)
>>> arr
array([0, 1, 2])
>>> np.tile(arr,3)
array([0, 1, 2, 0, 1, 2, 0, 1, 2])'''

arr.repeat(3)
'''arr.repeat(3)
array([0, 0, 0, 1, 1, 1, 2, 2, 2])'''

np.add.reduce(arr) #3
'''import matplotlib.pyplot as plt
mu,sigma=2,0.5
v = np.random.normal(mu,sigma,10000)
plt.show() '''
