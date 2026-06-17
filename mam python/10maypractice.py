# WAP to create a list list (squares ) of numbers

l=[1,2,4]
l1=[]

for var_name in l:
    a=var_name*var_name
    l1.append(a)
print (l1)
print()


l1=[var_name**2 for var_name in l]
print (l1)
print()

#create a list of even nos from 1 to 50......

l=[]
for var_name in range(1,51,1):
    if var_name%2==0:
        l.append(var_name)
print(l)
print()


l=[i for i in range(1,51) if i%2==0]
print(l)
print()


#WAP to create a list with word are of even length and as it is

s="hello everyone it is sunday"
l=s.split()
l1=[]
for var_name in l:
    if len(var_name)%2==0:
        l1.append(var_name)
    else :
        l1.append(var_name[::-1])
print(l1)
print()


l1=[word if len(word)%2==0 else word[::-1] for word in l]
print(l1)
print()


#WAP to create a list of even**2 no and odd**3

l=[1,2,3,4,5,6]
l1=[i**2 if i%2==0 else i**3 for i in l]
print(l1)
print()


#*******************************solve queston only using ccomprehension***************************************

#1..list of even number between range 1-50

l=[var_name  for var_name in range(1,50) if var_name%2==0]
print(l)
print()

#2..returns a list name starting with vowels in the given string


s=["laura","steve","bill","james","bob","greg","scott","alex","ive"]

s1=[var_name for var_name in s if var_name[0] in "aeiouAEIOU" ]

print(s1)
print("")

#3..filtering all the languages which starts with 'p'

s=["python","java","perl","php","puthon","js","c++","js","python","ruby"]
s1=[var_name for var_name in s if var_name[0] =="p"]
print(s1)
print("")

#4..returns a list name starting with consonants in the given string

s=["laura","steve","bill","james","bob","greg","scott","alex","ive"]
s1=[var_name for var_name in s if var_name[0] not in "aeiouAEIOU"]
print(s1)
print()

#5..filtering out those names which are less than 6 character

s=["apple","google","yahoo","gmail","flipkart","instagram","microsoft"]
s1=[var_name for var_name in s if len(var_name)<6]
print(s1)
print()

#6..raise to the power of its index..
s=[1,2,3,4,5]
s1=[s[var_name]**var_name for var_name in range(len(s))]
print(s1)
print()


#7..build a list of tuples with string and its length pair ..

s=["apple","google","yahoo","facebook","yelp","flipkart","gmail","instagram","microsoft"]
s1=[(var_name,len(var_name)) for var_name in s]
print(s1)
print()

#8..build a list only with even length string ..

s=["apple","google","yahoo","facebook","yelp","flipkart","gmail","instagram","microsoft"]
s1=[var_name for var_name in s if len(var_name)%2==0]
print(s1)
print(" ")

#9..generate list of PI values with increasing decimal point numbers..

from math import pi
print(pi)
l1=[round(pi,i) for i in range(1,10)]
print(l1)
print()


#10..list comprehesion to sum the factorial of number from 1-5

from math import factorial
l=[factorial(i) for i in range(1,6)]
print(sum(l))
print()

#using normal .....same above quesion

l=[]
sum_=0
for i in range(1,6):
    l1.append(factorial(i))
    sum_=sum_+factorial(i)
print(sum_)


#11..reverse the item of a list if a item of odd length string


s=["apple","google","yahoo","facebook","yelp","flipkart","gmail","instagram","microsoft"]
s1=[var_name[::-1] for var_name in s if len(var_name)%2!=0]
print(s1)
print()

#12..reverse the item of a list if a item of odd length string otherwise keep as it is


s=["apple","google","yahoo","facebook","yelp","flipkart","gmail","instagram","microsoft"]
s1=[var_name[::-1] if len(var_name)%2!=0 else [var_name] for var_name in s ]
print(s1)
print()
