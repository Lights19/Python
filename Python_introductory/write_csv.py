
import sys
import csv
import os


filename="write_csv.csv"

with open(os.path.dirname(os.path.abspath(__file__))+'/'+filename, 'w+',newline="") as f:
    writer=csv.writer(f)
    writer.writerow(['Header1','Header2','Header3','Header4','Header5'])
    for i in range(4):
        print(i)
        row=[ i+1,"Data"+str(i),"Data again"+str(i),"Data again","and again"+str(i)]
        writer.writerow(row)

print(open(os.path.dirname(os.path.abspath(__file__))+'/'+filename,'r').read())
