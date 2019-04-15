

#####using print function

name='Mitchell Johnson'
phone='98606060660'
yr=1999
index=99.12345
print(name)
print(name,phone,yr)
print(type(name))

'''now using format'''

print('My name is:'+name)
print('My name is:',name)

print('My name is: '+name+"   "+phone+" -- "+str(yr)) # for printing several strigs use'+'

##modern way of printing the same thing as above
print('My name is : {0}, phone is: {1}' .format(name,phone))
print('My name is : {1}, phone is: {0}' .format(phone,name))
print('My name is : {0}, phone is: {1}, yr is {2}.' .format(name,phone,yr))

print('index is {0:.3f}'.format(index)) #.3f says print 3 floating numbers after decimal
print('index is {0:.2d}'.format(index)) # throws as error 'Unknown format code 'd' for object of type 'float'
print('power is {0}:' .format()) # throws an error 'tuple index out of range'
print('power is {0}:' .format(2**3)) # gets '8'


## New case

print('Phone is %s & year is %f' %(phone, yr)) # s is string d denotes decimal no.


####### Math
a=10
b=20.23
c=3
print("Line 1\n {0:.2f}".format(a+b+c))
print("Line 2\n",(a*c+b))
print("Line 3\n",(a*(b/c)))
