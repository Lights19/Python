
# basic use of print function
print("*")
print("**")
print("***")
print("****")

#ex2-some math
x=512-282
y=(47*48)+5
print("It is roughly", x/y)

#ex3 asking for input I

wgt= eval(input("Please enter the amount in Kg:"))
pnd= (2.2)/wgt;
print( wgt," kilo gram is equal to ", pnd, "pound")


#ex4 asking for input II
a= eval(input("please enter the first no:"))
b= eval(input("please enter the second no:"))
c= eval(input("please enter the third no:"))
total= a+b+c
#average=total/3
print("sum of", a, b, "and", c, "is", total)



#####################################3
####String operations#####################
############################################
s = 'abcdefghij'

e= input("Enter a string::")
if e[0].isalpha():
    print("your string starts with letter")
else:
    print("your string starts with non-letter")

# Ex-2 Lists
L= eval(input("please enter the list"))
print("first element of L is",L[0])

#Ex-3 built in functions for lists

l=[1,3,0,12,43,11,9,32,19,4]
l.append(15)
l.sort()
l[2]=6

