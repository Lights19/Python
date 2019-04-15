num = eval(input('please enter the number:'))
if num >0:
   if num<10:
      print('its less than 10')
print('done')


#Example 2


if num >=0 and num <= 10:
       print('in range')
print('done')

#Example 2

if num >=0:
        if num <=20:
               print(num,'is in range')
        else:
               print( num, 'is too large')
else:
               print(num,'is too small')
print('done')
                     
#######################################  

########################################
for i in range(10):
    print('Hello')


#Ex -2
   
for i in range(3):
    num =eval(input("please enter your number:"))
    print("square of num is", num*num)
print("the loop is done")
##################################################3
#Ex- 3


#Write a program that asks the user for their name and
#how many times to print it. #
# The program should print out the user’s name the speciﬁed number of times.

Name= input("please enter your name:")
times =eval(input("how many times you want to repeat?"))
for i in range(times):
    print(Name)
 ###############################################33

x= eval(input("how wide?"))
y= eval(input("how high?"))

print("*"*x)
for i in range(y):
   print("*"*i, "*"*y)
for i in range(y):
    print("*")
print("*"*x)

################################################
from random import randint
num=randint(1,10)
guess=eval(input("please enter a number:"))
if guess == num:
   print("you got it!")
else:
   print("the num is",num)

 
