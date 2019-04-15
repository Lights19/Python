#'exceptions' are the errors detected at the time of program execution
# #handling the exception, by using "try and except"shuld be in the part of program where exception is
#expected to occur
x=input("Enter a number1: ")
y=input("Enter a number2: ")
try:
    z=int(x)/int(y)
except ZeroDivisionError as e:
    print("Division by Zero exception:",e)
    z=None # initializing z as None if cannot be divided
print("Division is: ",z)


# general format for taking detour or handeling exception

try:
    while road_is_clear():
        drive()
except Accident as e:
    take_detour()


#handeling multiple exception or unknown type of error
x=input("Enter a number1: ")
y=input("Enter a number2: ")
try:
    z=int(x)/int(y)
except ZeroDivisionError as e:
    print("Division by Zero exception:")
    z=None # initializing z as None if cannot be divided
except ValueError as e:    
    print("Type error:",type(e).__name__,)
    z=None
print("Division is: ",z) 

