temp=0
while temp !=-1000:
    temp=eval(input("please enter the temp in celcius:"))
    if temp!=-1000:
        print(temp, "degree Celcius =", (9/5)*temp-32," degree F")
    else:
        print("Bye")

#Ex 2-

i=0
while i<50:
    print(i)
    i=i+3
print("Bye")

#Ex 3-
for i in range(10):
    num=eval(input("Enter a number:"))
    if num <0:
        print("Stopped early")
        break
else:
    print("user entered all 10 values!")
             
#two ways to check if an integer num is prime

# Ex4i-
i=2
num = eval(input("Please enter a num:"))
while i<num and num%i !=0:
        i=i+1
if i==num:
    print("prime")
else:
    print("Not a prime")

#Ex 4ii
for i in range(2,num):
    if num%i==0:
        print("Not a prime")
        break
else:
    print("Prime")
