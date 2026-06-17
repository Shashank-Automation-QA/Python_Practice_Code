#
'''
count=0
count1=0
for var in range(2,10,1):
    for var1 in range(1,5,1):
        if var%var1==0:
            count +=1
        else:
            break
            
    if count==2:
        print(var)    


#print prime no in given range........

for num in range(10):
    if num > 1:
        for div_num in range(2,num):
            if num%div_num==0:
                break
        else:
            print(num)
print()

#check no is prime or not........
            
num=10
for div_num in range(2,num):
            if num%div_num==0:
                print(num,"not prime no.")
                break
else:
    print(num,"prime no.")
print()

#print the nth prime no...

count=10
i=0
num=1
while i<count:
    if num>1:
        for div_num in range(2,num):
                    if num%div_num==0:
                        break   
        else:
            i+=1
            if i==10:
                 print(num,"is ",count,"th prime no.")
                    
    num+=1
print()

#WAP to create a dictonary of word and length pair of words starting with vowels.......

s="hi hello how are you"
d={}
l=s.split()
for word in l:
    if word not in d:
        if word[0] in "aeiouAEIOU":
            d[word]=len(word)
print(d)
print()
'''

#write a prime no using one line.........


num=[7,4,5,3,1,2,8,9]
print(list(filter((lambda value:["not prime" if value%i==0 else value for i in range(2,value)]),num)))
print()
'''
#WAP to get output 2A2B3C1D2A1C1D  input AABBCCCDAACDA
s="AABBCCCDAACDA"
s1=""
count=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        s1=s1+str(count)+s[i]
        count=1
print(s1)
print()
#print below given pattern

#print [1,2]
       [3,4]
       [5,6]
       [7,8]
       [9]


l=[1,2,3,4,5,6,7,8,9,10,11]
count=0
for i in range(0,len(l)-1,2):
    count+=1
    for j in range(i,2+i):
        if j%2==0:
            print([l[j],l[j+1]])
if len(l)%2!=0:
    print([l[-1]])
else:
    pass
print(count)

# correct it

from collections import Counter
d={}
words=["silent","sea","ease","listen","pea","ape","fare","fear"]
for i in range(len(words)-1):
    if len(words[i])==len(words[i+1]):
        if Counter(words[i])==Counter(words[i+1]):
            if words[i] not in d:
                d[words[i]]=words[i+1]
            else:
                d[words[i]]+=words[i+1]
    else:
        pass
        
print(d)


#########



s1="ate"
s2="tea"
if list(sorted(s1))==list(sorted(s2)) and s1!=s2:
    print("anagram")
else:
    print("not")

#2nd method
from collections import Counter
s1="ate"
s2="tea"
if Counter(s1)==Counter(s2) and s1!=s2:
    print("anagram")
else:
    print("not")

##

def count_(*args):
    b=len(args)
    print(b)
count_(0,1,2,3,1,4)
    
###
def max_min(s):
    s.sort()
    max_,*rest,min_=s
    print(max_)
    print(min_)

max_min([5,6,2,7,9])
print("************************")
##############


def sequence_(element,sequence):
    if isinstance(sequence,(str,list,tuple)):
        print(sequence.index(element))
    else:
        print("is not present")
sequence_("hi",["hi" ,"hello" ,"how" ,"are" ,"you"])


def outer(func):
    def wrapper(*args,**kwargs):
        return (func(*args,**kwargs).swapcase())
    return wrapper
@outer
def func1():
    return (input("enter the string "))
print(func1())


##################################

def check(*args,**kwargs):
    if len(args)or len(kwargs)>5:
        return "pass"
print(check(1))
