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


