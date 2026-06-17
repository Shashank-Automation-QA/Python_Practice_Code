#Write a program to read all the names of the employees in employees.csv.file....

import os
import csv
with open (r"C:\Users\singh\OneDrive\Desktop\mam\Alpha5\files\csv_files\employees.csv")as file:
    rows=csv.reader(file)
    header=next(rows)
    for data in rows:
        print(data[0])
print()


#WAP to print only the salaries that are >70000...........

import os
import csv
with open (r"C:\Users\singh\OneDrive\Desktop\mam\Alpha5\files\csv_files\employees.csv")as file:
    rows=csv.reader(file)
    header=next(rows)
    for data in rows:
        if int(data[3])>70000:
            print(data)
print()

#WAP to group male and female employees in the file........

import os
import csv
male=[]
female=[]
with open (r"C:\Users\singh\OneDrive\Desktop\mam\Alpha5\files\csv_files\employees.csv")as file:
    rows=csv.reader(file)
    header=next(rows)
    for data in rows:
        if data[1] == "male":
            male.append(data[0])
        else:
            female.append(data[0])
data={"male":male,"female":female}
print(data)
print()

#WAP to group employees based on their team..........

d={}
import os
import csv
path=r"C:\Users\singh\OneDrive\Desktop\mam\Alpha5\files\csv_files\employees.csv"
with open (path) as file:
    rows=csv.reader(file)
    header=next(rows)
    for data in rows:
        if data[2] not in d:
            d[data[2]]=[data[0]]
        else:
             d[data[2]]+=[data[0]]
print(d)


#WAp to sort the shares in test.csv file based on the share prices......

import os
import csv
l=[]
path=r"C:\Users\singh\OneDrive\Desktop\mam\Alpha5\files\csv_files\test.csv"
with open (path) as file:
    rows=csv.reader(file)
    header=next(rows)
    for data in rows:
        if data[2]!="":
            l.append(float(data[2]))
    l.sort()
print(l)
print()

#WAp to add the shares in test.csv file......

import os
import csv
sum=0
path=r"C:\Users\singh\OneDrive\Desktop\mam\Alpha5\files\csv_files\test.csv"
with open (path) as file:
    rows=csv.reader(file)
    header=next(rows)
    for data in rows:
        if data[1]!="":
            sum=sum+int(data[1])
print(sum)


#WAP to print total_vacinations of all the countries......

import os
import csv
path=r"C:\Users\singh\OneDrive\Desktop\mam\Alpha5\files\csv_files\vaccination_data.csv"
with open (path) as file:
    rows=csv.reader(file)
    header=next(rows)
    for data in rows:
        print(data[5])
print()

#WAP to print total vacination by countries.....

import os
import csv
d={}
path=r"C:\Users\singh\OneDrive\Desktop\mam\Alpha5\files\csv_files\vaccination_data.csv"
with open (path) as file:
    rows=csv.reader(file)
    header=next(rows)
    for data in rows:
        print(data[5])
        if data[0] not in d:
            d[data[0]]= data[5]
        else:
            d[data[0]]+= data[5]
print(d)

#WAP to name of countries and who region.......

import os
import csv
d={}
path=r"C:\Users\singh\OneDrive\Desktop\mam\Alpha5\files\csv_files\vaccination_data.csv"
with open (path) as file:
    rows=csv.reader(file)
    header=next(rows)
    for data in rows:
        print(data[5])
        if data[2] not in d:
            d[data[2]]= [data[0]]
        else:
            d[data[2]]+= [data[0]]
print(d)

#WAP to print country and person vaccinated and get 3 countries with most vaccinated people........

import os
import csv
path=r"C:\Users\singh\OneDrive\Desktop\mam\Alpha5\files\csv_files\vaccination_data.csv"
with open (path) as file:
    rows=csv.reader(file)
    header=next(rows)
    for data in rows:
        if data[5]!=0 or data[5]!="":
            print(data[0],data[6])
            print(max(int(data[5])))
        
















        
        
        
