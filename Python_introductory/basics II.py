entry=0 # ensures the loop is entered
sum=0   #initialize sum

#request input from user
print("Enter numbers to sum, negative number ends list:")
while entry >=0: # A negative number exits the loop 
    entry=eval(input())   # Get the value
if entry >=0: # Is number non-negative?
    sum +=entry    # Only add it if it is non-negative
print("sum=",sum) # Display the sum


####################################################

x=input('please enter first integer:')

y=input('please enter second integer:')

num1=int(x)
num2=int(y)
print('sum of', num1 ,'and' ,num2 ,'is', num1+num2)


####################################################

r=eval(input('enter the radius of the circle:'))
PI=3.14
C=2*PI*r

print(C, 'is the circumference of the circle')

######################################################
w,x,y,z=10,20,30,40
print(w,x,y,z)
print(w,x,y,z,sep=',')
print(w,x,y,z,sep=' ')
print(w,x,y,z,sep='---')

######################################################
print('A\nB\nC')
print('D\tE\tF')
print('WX\bYZ')
print('1\a2\a3\a4\a5\a6')

######################################################
degreesF=eval(input('please enter the temperature in degreesF:'))
#perform the conversion
degreesC=5/9*(degreesF-32);
#print the result
print(degreesF,'degreesF=', degreesC,'degreesC')

######################################################
print('enter some text:')
x=input()
print('Text entered:', x)
print('type', type(x))


