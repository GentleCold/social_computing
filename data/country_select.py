from collections import Counter
import pandas as pd
import csv
li=[]
with open('personel-final-data.csv','r') as data:

    r=data.readline().split("[")
    while(len(r)>1):
           temp=r[-1].replace("]","").replace("\'","").split(",")
           print(temp[7])
           li.append(temp[7])
           r=data.readline().split("[")
counter = Counter(li)
print(li)
with open('counter_output.txt', 'w') as file:
    for element, count in counter.items():
        file.write(f"{element}: {count}\n")
