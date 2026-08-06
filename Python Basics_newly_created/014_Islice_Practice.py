#**************************************     islice  *******************************************************

#islice is a class in itertools module which is use to perform slicing on any iterables
# like: Collections, iterator object ,enumeration, zip object, reversed and file object etc.


#Syntax         from itertools import islice
#               object = islice(iterable,start,stop,step)

#WAP to print 10th to 15th lines.
start=10
end=15
#Below lines are for changing the directory location
import os
os.chdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\files")
from itertools import islice
with open(r"access-log.txt","r") as file:
    lines=islice(file,start-1,end)   # if we want to start from in between we need to give start-1 otherwise it will start from 0 index
    print(list(lines))  # if we don't use list it will give the object address

#WAP to print last n lines
#since we can't directly get file length or no. of lines in file first we need to write code to get count of lines in file
import os
os.chdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\files")
count=0
n=4
with open(r"sample.txt","r") as file:
    for line in file:
        count+=1
    file.seek(0)    # this is use to take cursor in the specific location and this is mandatory
    from itertools import islice
    lines = islice(file,count-4,count)
    print(list(lines))

#second method using deque
import os
from collections import deque
os.chdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\files")
n=4
with open(r"sample.txt","r") as file:
    lines=deque(file,n)
    print(list(lines))

#WAP to find the line no. of particular word in the file
import os
os.chdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\files")
word="hello"
with open(r"sample.txt","r") as file:
    for index,line in enumerate(file, start=1):
        if line.strip():
            words=line.split()
            if word in words:
                print(index)

#WAP to count all lower case and upper case letters in file
import os
os.chdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\files")
upper=0
lower=0
with open(r"sample.txt","r") as file:
    for line in file:
        for l in line:
            if l.isupper():
                upper+=1
            elif l.islower():
                lower+=1
print(lower,upper)

#WAP to create dictionary with vowels and their count pairs
import os
os.chdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\files")
d={}
with open(r"sample.txt","r") as file:
    for line in file:
        for l in line:
            if l in "aeiouAEIOU":
                if l not in d:
                    d[l]=1
                else:
                    d[l]+=1
print(d)

#**************************************     counter  *******************************************************

# Syntax        from collections import Counter     >> Counter's C should be capital

#WAP to count the of each item
from collections import Counter
l=['a','a','a','d','a','b','b']
print(dict(Counter(l)))        #>>>  {'a': 4, 'd': 1, 'b': 2}    type casting to dictionary

#**************************************     Deque  *******************************************************
#Deque (Doubly Ended Queue ) is the optimize list for quicker operation from both side of the container

#**** Note:  Basically Deque read line from last if

#WAP to read last n lines of file
import os
from collections import deque
os.chdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\files")
n=4
with open(r"sample.txt","r") as file:
    lines=deque(file,n)
    print(list(lines))

#WAP to rotate list elements
from collections import deque
l=[1,2,3,4,5]
rotation=1
d=deque(l)
d.rotate(rotation)            #>>> We have rotate keyword in deque concept
print(list(d))

