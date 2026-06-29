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