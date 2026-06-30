##################################################### While Loop ###############################################
# Syntax =>   while condition:
#                   statements

#WAP to find out even numbers for 1-10
start=1
end=10
while start<=end:
    if start%2==0:
        print(start, end="")
    start+=1
print(end="\n")

#WAP to find out odd numbers for 1-10
start=1
end=10
while start<=end:
    if start%2!=0:
        print(start, end="")
    start+=1
print(end="\n")

#WAP to find out odd numbers for -10 to -1
start=-10
end=-1
while start<=end:
    print(start, end="")
    start+=1
print(end="\n")

#WAP to find out odd numbers for -1 to -10
start=-1
end=-10
while start>=end:
    print(start, end="")
    start-=1
print(end="\n")

#WAP to print prime number in between range of 1 to 10
num=1
while num<=10:
    if num>1:
        i=2
        while i<=int(num/2):
            if num%i==0:
                break
            i+=1
        else:
            print(num)
    num+=1
print(end="\n")

#WAP to print fibonacci series from 0 t0 10.
a,b=0,1
count=0
while a<=10:
    print (a ,end="")
    c=a+b         #1  2  3  5  8
    a=b           #1  1  2  3  5  ==>>  fibonacci series
    b=c           #1  2  3  5  8
print(end="\n")

##################################################### for Loop #################################################

########################  range()  ###################

#WAP to print even number from 1-50 by using for loop.
for i in range(1,50,1):
    if i%2==0:
        print(i, end=' ')
print(end="\n")

########################  enumerate()  ###################

#WAP to print the values inside list along with their indexes
l=[1,2,3,4,5,6,7,8]
for index, value in enumerate(l):
    print(index, value)

#WAP to print the values inside list along with their indexes list in tuple form
l=[1,2,3,4,5,6,7,8]
for i in enumerate(l):
    print(i)

########################  zip()  ###########################

####### Syntax: ==>  zip(iterable1, iterable2...etc)
##Basically zip() takes more then one iterable and convert them in form of list of tuple [( ), ( ), ( )]

#WAP to create list of tuple by combining both list values in order
l1=['apple', 'google', 'flipkart']
l2=[10,20,30]
for i in zip(l1,l2):
    print(i)

# #WAP to create a dict by making one list as key and elements of other list as value
l1=['apple', 'google', 'flipkart']
d={}
for j,k in zip(l1,l2):
    d[j]=k
print(d)

########################  zip_longest()  ###########################

####### Syntax: ==>  zip(iterable1, iterable2...,fillvalue=None)
## if both iterables lengths are not same in that case we can use zip_longest it will use none as  pair
## of other value. We need to import zip_longest from itertools class before using it

#WAP to create list of tuple by combining both list values in order
from itertools import zip_longest
l1=['apple', 'google', 'flipkart','walmart']
l2=[10,20,30]
for i in zip_longest(l1,l2):
    print(i)

########################  for else loop ###################
########################     break      ###################

#WAP to print prime number from 1-10 by using for loop.
for i in range(1,10):
    if i >1:
        for k in range(2,int(i/2)):
            if i%k==0:
                break
        else:
            print(i, "is prime number")
print(end="\n")

################# Traversing through for loop ###################
####### String ####
s= "hello"
for i in s:
    print(i, end="")
print(end="\n")

for i in range(len(s)):
    print(i,s[i])
print(end="\n")

####### Dict ####
d={'a':1, 'b':2, 'c':3}
for key in d:
    print(key, d[key])

####### Set ####
s={1,2,3,4,5}
for i in s:
    print(i)

#############################  Activity ###############################

#WAP to count the no. of words in sentence
s="hello how are you"
count=0
for i in s.split():
    count+=1
print(count)

#WAP to print all the repeated characters
s="hello how are you"
for i in s:
    if s.count(i)>1:
        print(i)

#WAP to remove the duplicate and repeated character in the string
s="hello how are you"
s1=""
for i in s:
    if s.count(i)==1:
        s1+=i
print(s1)

#WAP to print the duplicate character without using inbuilt function
s1="hello world"
duplicate=""
non_duplicate=""
for i in s1:
    if i not in non_duplicate:
        non_duplicate+=i
    else:
        duplicate+= i
print(("".join(set(duplicate)), non_duplicate))

#WAP to print all the indices of the given sub string
s="hello world"
ch='o'
for i in range(len(s)):
    if s[i]==ch:
        print(s[i], i)

#WAP to print first indices of the given sub string
s="hello world"
ch='o'
for i in range(len(s)):
    if s[i]==ch:
        print(s[i], i)
        break

#WAP to print second indices of the given sub string
s="hello world"
ch='o'
count=0
for i in range(len(s)):
    if s[i]==ch:
        count+=1
        if count==2:
            print(s[i], i)
            break

#WAP to create list with word ending with vowels
s="Hi good afternoon, welcome to afternoon session"
l=s.split()
l1=[]
for i in l:
    if i[-1] in "AEIOUaeiou":
        l1.append(i)
print(l1)

#WAP to create set with word ending with vowels
s="Hi good afternoon, welcome to afternoon session"
l=s.split()
l1=set()
for i in l:
    if i[-1] in "AEIOUaeiou":
        l1.add(i)
print(l1)

#WAP to create a list of tuple with word and its length pair
s="Hi good afternoon, welcome to afternoon session"
l=s.split()
l1=[]
for i in l:
    l1.append((i,len(i)))
print(l1)

#WAP to create a dict with word and its length pair if word starts with vowel
s="Hi good afternoon, welcome to afternoon session"
l=s.split()
d={}
for i in l:
    if i[0] in "AEIOUaeiou":
        d[i]=len(i)
print(d)

#WAP to create a dict with letter and word starting with that letter pair
s="Hi good afternoon, welcome to the afternoon session"
d={}
for i in s.split():
    if i[0] not in d:
        d[i[0]]=[i]
    else:
        d[i[0]].append(i)
print(d)

#WAP to create a dict of character and indices pair
s="Hi good afternoon, welcome to the afternoon session"
d={}
for i in range(len(s)):
    if s[i] not in d:
        d[s[i]]=[i]
    else:
        d[s[i]].append(i)
print(d)

#WAP to create a dict of character and its asci value pair
s="Hi good afternoon, welcome to the afternoon session"
d={}
for i in s:
    if ord(i) not in d:
        d[ord(i)]=[i]
    else:
        d[ord(i)].append(i)
print(d)

#WAP to create a dictionary with value if integer datatype
d={'a':1, 'b':'hello', 'c':85, 'd':12.3, 'e':[1,2,3]}
d1={}
for i in d:
    if isinstance(d[i],int):
        d1.update({i:d[i]})
print(d1)

#WAP to create a dictionary if the value is string, reverse it, else keep it as it.
d={'a':1, 'b':'hello', 'c':85, 'd':12.3, 'e':[1,2,3]}
d1={}
for i in d:
    if isinstance(d[i],str):
        d1.update({i:d[i][::-1]})
    else:
        d1.update({i: d[i]})
print(d1)

#WAP to print index and element of an iterable
iterable=['apple', 'google','wallmart','flipkart','gmail']
for i in enumerate(iterable):
    print(i, end=' ')

#WAP to print even index element of an iterable
###################  First Method
iterable=['apple', 'google','wallmart','flipkart','gmail']
for i in enumerate(iterable):
    if i[0]%2==0:
        print(i[1], end=' ')
print(end='\n')

###################  Second Method
iterable=['apple', 'google','wallmart','flipkart','gmail']
for i,v in enumerate(iterable):
    if i%2==0:
        print(v, end=' ')

#WAP to create a dict of indexes element pair only if the element of and odd length
iterable=['apple', 'google','wallmart','flipkart','gmail']
d={}
for i,v in enumerate(iterable):
    if len(v)%2!=0:
        d[i]=v
print(d)




