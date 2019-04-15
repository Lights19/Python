import csv
import os
''' multiline comment
filename ='write_csv.csv'

header1,header=[],[]
l=[]

with open(os.path.dirname(os.path.abspath(__file__))+'/'+filename) as f:
    reader=csv.reader(f)


    count=0
        for row in reader:
        print(reader.line_num,">>",row)
        l.append(reader.line_num)
        count+=1
        if count==5:
            break
    print("There are Total:",len(l),"Rows")'''



filename='w_earthquakePast_check.csv'

lats,lons = [], []
epicentre,magnitudes = [],[]
timestrings = []
l=[]

with open(os.path.dirname(os.path.abspath(__file__))+'/'+filename) as f:
    reader=csv.reader(f)

    for row in reader:
        print(reader.line_num,">>>>",row)
        l.append(reader.line_num)
    print("There are Total:",len(l),"Rows")

    
    
