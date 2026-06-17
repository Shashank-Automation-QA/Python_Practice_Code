#extract no and add 2.........from "$50000/-"

s="$50000/-"
s2=""
for num in s:
    if ord("0")<=ord(num)<=ord("9"):
        s2=s2+str(num)
num1=int(s2)
num1=num1+2
print(num1)

#                                               *******************os module****************************                                                       



#                                                   all commands for handling the directories....


import os
print(os.getcwd()) #to get the path of urrent working directory
print()

os.chdir(r"C:\Users\singh\OneDrive\Desktop\python'") #to change the directory name
print(os.getcwd())

os.mkdir("demo")# to make a directory (folder)
os.rmdir("demo")#to delete a direcory (folder)

print(os.listdir())#to print all the files present inside the directory
print()



#                                                   all commands for handling the files....

import os
##os.popen("sample.txt") #to open file
##os.rename("sample.txt","sample1.txt") #to rename alredy existing file
##os.remove("sample1.txt")




#                                                           commands for path

import os
print(os.path.exists(r"C:\Users\singh\OneDrive\Desktop\python'"))  #if path exist it return true it will work for both(directory,file)
print(os.path.getsize(r"C:\Users\singh\OneDrive\Desktop\python'")) #if path exist it return size of file or directory



#opening files in python .....



f_path=r"C:\Users\singh\OneDrive\Desktop\python'\sample.py"
f_obj=open(f_path) #to open a file without context manager
print(f_obj.closed) #it will reurn false if file is open if file is close then it return true
print()


file=open("../sample.txt", "r")
print(file.read())#return all the data present in side the file
print()


file=open("../sample.txt", "r")
print(file.readline())#return first line present inside the file
print()


file=open("../sample.txt", "r")
print(file.readlines())#return all the lines present in file and give o/p in list 
print()



#                                                         file questions


#WAP to print the line with line numbers.........

import os
with open("../sample.txt") as file:
    for line_no,line in enumerate(file, start=1):
        if line.strip():
            print(line_no,line,sep="")
print()

#WAP to read the file in reverce order......

with open("../sample.txt") as file:
    for line in reversed(list(file)):
        print(line)
print()         

#WAP to find the length of the each line in the text file...

with open("../sample.txt") as file:
    for line in file:
        print(len(line))
print()

#WAP to extract ip address from log file .........

with open("../access-log.txt") as file:
    for line in file:
        if line.strip():
            l=line.split()
            print(l[0])
print()

#WAP to counting no of accurence of ip address in the log file.......
d={}
with open("../access-log.txt") as file:
    for line in file:
        if line.strip():
            l=line.split()
            if l[0] not in d:
                d[l[0]]=1
            else:
                d[l[0]]+=1
print(d)

#WAP to extracting message from sample.log....

with open(r"C:\Users\singh\OneDrive\Desktop\mam\Alpha5\files\sample.log") as file:
    for line in file:
        l=line.split(":")
        print("==>",l[-1])
print()

#WAP to counting number of INFO,WARN,TRACE messages.......

d={}
with open(r"C:\Users\singh\OneDrive\Desktop\mam\Alpha5\files\sample.log") as file:
    for line in file:
        if line.strip():
            l=line.split(":")
            a=l[2].split()
            if a[1] not in d:
                d[a[1]]=1
            else:
                d[a[1]]+=1
print(d)
print()

#WAP read countries from football.txt.......

with open(r"C:\Users\singh\OneDrive\Desktop\mam\Alpha5\files\football.txt",encoding = "UTF-8") as file:
    d={}
    for line in file:
        if line.strip():
            l=line.split("\t")
            if l[1] not in d:
                d[l[1]]=1
            else:
                d[l[1]]+=1
print(d)
print()

#WAP to least and most occurances of the word....
from collections import Counter
with open("../sample.txt") as file:
    l=[]
    for line in file:
        if line.strip():
            word=line.split()
            l.extend(word)
c=Counter(l)
most,*rest,least=c.items()
print(most)






