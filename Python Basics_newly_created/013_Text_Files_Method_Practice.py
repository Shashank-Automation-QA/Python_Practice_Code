# Below all methods are used to handle the files

# popen(file_name, mode) ==>> similar to open(), popen() do a pipe/gateway and access the file directly
# rename(old_name, new_name)   ==>> renames the file with new name
# remove()   ==>> used to remove or delete a file path. This method can not remove or delete directory. If the
                #specified path is a directory then OSError will be raised by the method.


import os
# os.popen(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\000_Python Theory")

# os.remove("we need to provide the file path here")
# os.rename("old","new")

#To check if the path is exist or not we have method exists()
print(os.path.exists("000_Python Theory"))

#To check the file size we have method getsize()
print(os.path.getsize("000_Python Theory"))



# open file ==>> perform operation (read and write)  ==>>  close file     this is the process to work with file in python.

################## open file  ##############
# In python we can open file two ways without context manager and with context manager

#Without context manager
#Syntax:   file_obj = open (file_name, mode)   If we open file with this syntax we need to close file manually.

#With context manager
#Syntax:   with open (file_name, mode) as file_obj:   If we open file with this syntax it will close file automatically.

f_path=r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\files\sample.txt"

#Without context manager
f_obj = open(f_path)
print(f_obj.closed)    #false

f_obj.close()
print(f_obj.closed)    #true

#With context manager
with open(f_path) as f:
    print("inside with block", f.closed)    #false

print("outside with block", f.closed)    #true

#Modes :  There are 4 different methods(mode) for opening a file:

# "r" ==>> Read default value. Opens a file for reading, error if the file does not exist.

# "a" ==>> Append - open a file for appending ,create the file if it does not exist.

# "w" ==>> Write - open a file for writing,creates the file if it does not exist(override the context of file if the file exist)

# "x" ==>> Create - create a specified files and return error if file already exist.

#Note: If the mode is r+,w+,a+,x+ it means we can do read and write both of the operation on the file

#####################    File object attributes   ####################

# file.closed():  Returns true if file is closed.
# file.mode():   Returns access mode with which file was opened.
# file.name():  Returns name of file.
# file.redable():  Returns true if file is opened on read mode.
# file.writable():  Returns true if file is opened on write mode.
# file.close():  close the file.

#methods to read data from file:
#read(): read the data from starting till end of file read() can have one argument which is and integer it specifies the no. of character to be read from the file from the starting.

#WAP to read a data from starting to end of file
import os
os.chdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\files")
file=open("sample.txt","r")
print(file.read())   #or   print(file.read(4))

#readline(): read a single line from the file
file=open("sample.txt","r")
print(file.readline())

#readlines(): read a entire text in form of list, separating each line as an element
file=open("sample.txt","r")
print(file.readlines())

with open("sample.txt","r") as file:
    for line in file:
        print(line)     #traversing through file by loading one line into memory

with open("sample.txt","r") as file:
    print(next(file))
    print(next(file))   #traversing through one line at a time(lazy iterable)


#####################                        Activity                                  #####################

#WAP to read the contains of a file without loading the file in to memory
import os
os.chdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\files")
with open("sample.txt","r") as file:
    for line in file:
        print(line)

#WAP to print line no along with the line
with open(r"sample.txt","r") as file:
    for line_no,line in enumerate(file,start=1):
        print(line_no,line)

#WAP to print only non blank line
with open(r"sample.txt","r") as file:
    for line in file:
        if line.strip():
            print(line)

#WAP to read file in reverse order
with open(r"sample.txt","r") as file:
    for line in reversed(list(file)):
        print(line)

#WAP to count no. of lines in sample.txt file
with open(r"sample.txt","r") as file:
    count=0
    for _ in file:
        count+=1
print(count)

#WAP to count no. of words present in sample.txt file
with open(r"sample.txt","r") as file:
    words_count = 0
    for line in file:
        l=line.split()
        for word in l:
            words_count+=1
print(words_count)

#WAP to print length of each line with the line in file sample.txt
with open(r"sample.txt","r") as file:
    for line in file:
        if line.strip():
            print(line,len(line))

#WAP to create a dictionary with word and its count pair in the file.
with open(r"sample.txt","r") as file:
    d={}
    for line in file:
        if line.strip():
            l=line.split()
            for i in l:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
print(d)

#WAP to extract the IP address from file
with open(r"access-log.txt","r") as file:
    for line in file:
        if line.strip():
            l=line.split("-")
            print(l[0])

#WAP to create dictionary with IP address and their count pair.
with open(r"access-log.txt","r") as file:
    d={}
    for line in file:
        l=line.split("-")
        if l[0] not in d:
            d[l[0]]=1
        else:
            d[l[0]]+=1
print(d)

#WAP to print most accured IP address in the "access logged" file.
with open(r"access-log.txt","r") as file:
    d={}
    for line in file:
        if line.strip():
            l=line.split("-")
            if l[0] not in d:
                d[l[0]]=1
            else:
                d[l[0]]+=1
min_,*rest,max_=sorted(d.items(), key=lambda item:item[-1])
print(max_)

#WAP to print nth line from file.
with open(r"sample.txt","r") as file:
    count=0
    for line in file:
        count+=1
        if count==9:
            print(line)

                    # OR

with open(r"sample.txt","r") as file:
    n=input("enter line number: ")
    for index,line in enumerate(file, start=1):
        if index==int(n):
            print(line)

#WAP to print read first n lines from file.
with open(r"sample.txt","r") as file:
    n=input("Enter line number: ")
    for index,line in enumerate(file,start=1):
        if index<=int(n):
            print(line)

#************************************** Write action on files *******************************************

#For writing content inside file we have write() and writelines() methods are present and we must have to choose the correct mode for writing data

# tell() return the correct position of cursor
# seek(position) change the position of cursor it takes one argument as index

import os
os.chdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\files")
print(os.getcwd())  #To check current working directory location
with open(r"demo.txt","w") as file:
    print(file.write("Hi My Name is Shashank and i am learning python\n"))   #>>  file.write() returns no of characters entered in file, and it takes only string values
    print(file.tell())  # tell() return the cursor location

    file.writelines("Hi \nhello \nhow are you\n") #>>  file.writelines() returns none and write iterables like dict, list, tuple in file

    #below adding dict data in to file
    data={"name":"shashank\n", "city":"Banglore\n"}

    file.writelines(data)           #>>>>>  If we will write only data then it will add only dict keys on file

    file.writelines(data.values())  #>>>>>  If we will write data.values() then it will add only values on file

    #If we want both key and value the we have to write code like below line
    file.writelines(f"{k}:{v}" for k,v in data.items())
    file.close()

