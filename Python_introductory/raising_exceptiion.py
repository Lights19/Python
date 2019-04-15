'''try:
    raise MemoryError('Memory error') # 'MemoryError' is exception class name
except MemoryError as e:
    print(e)'''


# we can find several standards excepiton in google by searching 'python builtin exceptions'


# for userdefined exception we need to define a class

class Accident(Exception):  #Accident is derived from Eception class
    def __init__(self,msg):
        self.msg=msg
    def print_exception(self):
        print("User defined exception:",self.msg())

        
try:
    raise Accident("crash between  2 car") 
except Accident as e:
    e.print_exception()
