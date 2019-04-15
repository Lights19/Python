###############################
###Dictionary Examples#######
###############################
d= {'dog':'chases a cat',
    'cat':'chases a rat',
    'rat':'rats runaway'}

word=input("Enter a word:")
print("The defination is:",d[word])

d2=d.copy()
print(d2) 


#################################################333

letter=input("Enter a letter:")
d={ 'A':'20','B':'30','C':'40','D':'50'}

if letter in d:
    print("The value is:",d[letter])
else:
    print("Not Available")

#printing key and value
for key in d:
    print(d[key])

###########################

keys of list
list(d)

Values of key
list(d.values())

(key,value) pairs of d
list(d.items())
########################################################

#alternative way to create dictionary

#d=dict([('A',20),('B',30),('C',40),('D',50),('E',90)])

