
import time
d={}
def count_(func):
    def wrapper(*args,**kwargs):
        
        if func.__name__ not in d:
            d[func.__name__]=1
        else:
            d[func.__name__]+=1
        func(*args,**kwargs)
            
    return wrapper
@count_
def hello_(*args,**kwargs):
     print(d)

hello_("hi")
hello_("hi")

@count_
def hello_1(*args,**kwargs):
     print(d)

hello_1("hi")

#
import time
def delay_(n):
    def count_(func):
        def wrapper(*args,**kwargs):
            for _ in range(n):
                func(*args,**kwargs)
        return wrapper    
    return count_
@delay_(3)
def hello_(*args,**kwargs):
     print("hi")
hello_(2)

#
s=["hii","helo","how","awsome"]
d=(i for i in s if len(i)%2!=0)
print(list(d))


#
from itertools import islice
count=0
n=3
with open("../sample.txt") as file:
    for lines in file:
        count+=1
    file.seek(0)
    res=islice(file,count-n,count)
    print(list(res))

#

numr=100
count=0
s=10
for n in range(1,numr*numr):

    for i in range(2,n):

        if(n%i==0):

            break

    else:
        count+=1
        if count<s+1:
            print(n)
            print()


#


#
count=0
n=10
m=10
for num in range(0,n**n):
    if num>1 and count<=m:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
            count+=1

#
def fun_name(l):
    def wrapper(*args,**kwargs):
        for num in range(0,n):
            for i in range(2,num):
                if num%2==0:
                    break
            else:
                print(num)
            func(*args,*kwargs)
    return wrapper
@fun_name
def main_(l):
    l=[1,2,3,4]
    for m in l:
      print(m)
main_(l)

#


class Noint:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def move(self, dx, dy):
        self.a = self.a + dx
        self.b = self.b + dy
    
    def reset(self):
        self.a = 0
        self.b = 0
    
    def sort(self):
        if self.a > self.b:
            temp = self.a
            self.a = self.b
            self.b = temp
        
    def total(self):
        return self.a + self.b

p1=Noint(1,2)
p2=Noint(3,4)

#print(p1.__dict__)
#print(dir(p1))
print(p1.__dict__)

print(p1.reset())
print(p1.__dict__)
print(dir(p1))
print("*********************************************************************")



class p:
    def __init__(self,value):
        self.x=value
    
    def a():
        print("hi")

class b(p):
    def n():
        print("bye")
print("**********************************************")



#wap o count the length of any iterable......

s="hello hi how are you "
count=0
for i in s:
    count+=1
print(count)

###############################

s="hello world welcome world"

d=""
l=s.split()
for i in l:
    if i == "world":
        d=d+" universe"
    else:
        d+=" "+i
         
print(d)

#############################

#waf to convers a string in to  a lsit and vice versa.....
def func(stri):
    l=(list(stri))
    print(l)
    b="".join(l)
    print(b)

func("shashank")

#conver the string hello welcome to python.............
s="hello welcome to python"
print(",".join(s.split()))



print(isinstance(s,str))


#############

#add the elements of inner list...........

res=[]
l=[[1,2,3],[4,5,6],[7,8,9]]
for i in l:
    sum_=0
    for j in i:
        sum_+=j
    res.append(sum_)
print(res)

###############
resu=[]
l=[[1,2,3],[4,5,6],[7,8,9]]
for i in l:
    resu.append(sum(i))
print(resu)
###########

print([sum([1,2,3]),sum([4,5,6]),sum([7,8,9])])

###################
l=[sum(i) for i in l]
print(l)

#####################

#remove duplicate item without using inbuilt
l1=[]
l=["apple","google","apple","yahoo","apple"]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        count+=1
        l1.remove(i)
print(l1)

#
l=[1,2,3,0,4,3,2,4,2,1,0,4]
l.sort()
min_,*rest,max_=l
print(max_)
for i in l :
    if i==max_:
        print(i)

#####\
#o/p={'h': ['hello', 'hi'], 'w': ['world', 'welcome', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'progarming']}

s="hello world welcome to python progarming welcome hi there"
d={}
l=s.split()
for i in l:
    if i[0] not in d:
        d[i[0]]=[i]
    else:
         d[i[0]]+=[i]

print(d)
        
##
from collections import defaultdict
dd=defaultdict(list)
s="hello world welcome to python progarming welcome hi there"
for i in s.split():
    dd[i[0]].append(i)
print(dd)

###
d={"a":"hello","b":100,"c":10.1,"d":"world"}
for key,value in d.items():
    if isinstance(value,str):
        d[key]=value[::-1]
print(d)

d1={key:value[::-1] if isinstance(value,str)else value for key,value in d.items() }
print(d1)

#replace nose with net
d={"a":100,"b":{"m":"man","n":"nose","o":"ox","c":"cat"}}
for key,value in d.items():
    if isinstance(value,dict):
        for key1,value1 in value.items():
            if value[key1]=="nose":
                value[key1]="net"
print(d)

#group flower and animal in the below list.......

items=["lotus-flower","lilly-flower","cat-animal","sunflower-flower","dog-animal"]
d={}
for i in items:
    l=i.split("-")
    if l[1] not in d:
        d[l[1]]=[l[0]]
    else:
        d[l[1]]+=[l[0]]
print(d)

#n
names=["apple","google","apple","yahoo","yahoo","google","gmail","gmail","gmail"]
g ={}
for index,values in enumerate(names):
    if values not in g:
        g[values]=[index]
        #print(g)
    else:
        g[values].append(index)
print(g)
    

#123*
#12*4
#1*34
#*234

l=""
for j in range(1,5):
    for i in range(1,5):
        if i==5-j:
            l=l+" *"
        else:
            l=l+" "+str(i)
count=0
for k in range(int((len(l)-1)/4)):
        print(l[0+count:8+count])
        count+=8
        
#create dctonary with words and its length pair .....

s="this is a bunch of words"
l=s.split()
d={}
for i in l:
    if i not in d:
        d[i]=len(i)
print(d)
print()

#flipping key and values o dictonary using dict comprihension..
d={'a':1,'b':2,'c':3}
print({value:key for key,value in d.items()})
print()    
            
#counting the no of each character in a string ....

s="guido van rossum"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
print()

#count the number of character  in given string...
s="hello world welome to python hello hi world welcome to python"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
print()

#dictoary of character and its ascci values.....
s="abcABC"
d={}
for i in s:
    if i not in d:
        d[i]=ord(i)
print(d)
print()

#creating the dictonary of city and its population pair.....
cities=['Tokyo',"delhi","sanghai","sao paulo","mumbai"]
population=["38,001,000","25,703,168","23,740,778","21,006,245","21,042,538"]
d={}
for i in range(len(cities)-1):
    if  cities[i] not in d:
        d[cities[i]]=population[i]
print(d)
print()


#create a dictonary of dail code and country code from the following list..
s=[(86,'china'),(91,'india'),(1,'us'),(62,'indinesia'),(55,'brazil'),(92,'pakistan'),(880,'bangladesh')]
d={}
for i in s:
    if i[1] not in d:
        d[i[1]]=i[0]
print(d)
print()

#print(list([(S.count((max(S))))*max(S), (S.count((max(S))))]))

#WAF the takes variable no of positional arguments as input how to check if the arguments are passed more than 5.......

def func_(*args):
    if len(args)>5:
        print("length is more than five")
    else:
        print("length is less than five")
func_(1,2,3,4,5,6)
print()


#write a program to check wether no is prime or not....

l=[2,3,4,56,78]
for j in l:
    if j>1:
        for i in range(2,j):
            if j%i==0:
                print(f"{j} num is not prime")
                break
            else:
                print(f"{j} num is prime")
print()

#WAF that return the last digit of an integer......

def func_1(num):
    return num%10
print(func_1(1223))

#waf that name tail that takes a seqence (like a string, list or tuple) and number n and returns the last n elements from the given sequence as a list....

def tail(*sequence):
    return [sequence[-1]]
print(tail(1,2,3,4))

#waf 




class A:
    
    def log(self):
        print("hi")

class b:
    def log(self):
        super().log()
        print("hello")
        
        
class c(b,A):
    pass

########################################


S="aabbbbccccdddddeeeeeeeeeeeeeeeeeeeee"
d={}
l=[]
for i in S:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for j in S:
    if d[j]>(max(d.values()))-1 and (d[j]*j,d[j]) not in l:
            l.append((d[j]*j,d[j]))
print(l)

#WAP to count the no. of lines without loading the file in the memory...

#WAP to count the no of ip addresses in access log file..

d={}
with open(r"C:\Users\singh\OneDrive\Desktop\python'\access-log.txt") as file:
    for lines in file:
        if lines.strip():
            l=lines.split()
            if l[0] not in d:
                d[l[0]]=1
            else:

                d[l[0]]+=1
print(d)
print()
        
#WAP to print most repeated ip address along with its count

d={}
with open(r"C:\Users\singh\OneDrive\Desktop\python'\access-log.txt") as file:
    for lines in file:
        if lines.strip():
            l=lines.split()
            if l[0] not in d:
                d[l[0]]=1
            else:
                d[l[0]]+=1

                
v=(max(d.values()))
for i in d:
    if d.values()==v:
        print(d[i])

#WAP to print nth line ,file
        

n=6
with open(r"C:\Users\singh\OneDrive\Desktop\python'\access-log.txt") as file:
    for line_no,line in enumerate(file,start=1):
        
            print(line)
            break
            


#wap to read random line from the file.....

import random
count=0
with open(r"C:\Users\singh\OneDrive\Desktop\python'\access-log.txt") as file:
    for line_no,lines in enumerate(file):
        count+=1
    n = random.randint(0,count)
    print(f"Total no of lines in file are {count}")
    print()
    file.seek(0)
    for line_no1,line1 in enumerate(file):
        if line_no1==n:
            print(f"{line1} present in {n} number")

print("****************************")    


# add positive and negative value....

l=[1,-2,3,-7]
pos=lambda num:num>0
neg=lambda num:num<0

pos_sum=sum(list(filter(pos,l)))
neg_sum=sum(list(filter(neg,l)))
print(pos_sum,neg_sum)

'''
# anagram

l=["ate","eat","tea","silent","listen"]
from collections import Counter
d={}
def xyz(l):
    global d
    for i in l:
        if i not in d:
            d[i]= i
            return i
for i in l:
    if Counter(i)
print(xyz(l),d)
'''        
############################################
from re import findall,sub,finditer

s="Shashank singh hi. "
re=finditer(r"\.",s)
print(re)

res=findall(r"(Inbox\(?\d*\)?)","Inbox")
print(res)


























    
    
            
    
