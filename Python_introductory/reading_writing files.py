f=open("D:\Aaa\\Python\\Practice lessons\\empty.txt","w") # w is for write
f.write("I love to Practice")
f.close() 
# this over writes if process is repeated

# we need to append  to add.

f=open("D:\Aaa\\Python\\Practice lessons\\empty.txt","a") # a is for append
f.write("I love to Practice \n and that makes me perfect")
f.close()


#reading a file line by line


f=open("D:\Aaa\\Python\\Practice lessons\\funny.txt","r") # r is to read
f_out=open("D:\Aaa\\Python\\Practice lessons\\funny_wc.txt","w")

for line in f: # every time it reads one line
    tokens=line.split(' ') # gives array of words
    f_out.write("words count:"+str(len(tokens)) +"\t"+line )
    
f.close()
f_out.close()


#r opens file only
#w opens file for writing only, it will create new one if it doesnot exists and if it
#exists it overwrites it.
#r+ opens file for both reading and writing, doesnt creats a new file if it doesn't exists
#w+  opens file for both reading and writing. it will create new one if it doesnot exists and if it
#exists it overwrites it.
#a opens a file in append mode. whatever you write the file will get appended and 
#original content will not be overwritten


#with statement
#with open("D:\Aaa\\Python\\Practice lessons\\funny.txt","r") as f: # by this we don't have to close the file.

#f.closed # tells you whether the file is closed or not gives True or False
