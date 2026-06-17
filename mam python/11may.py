
#1..create a dictonary with words and it length value...

s="hello hi good afternoon"
l=s.split()
d={}

for var_name in l:
    d[var_name]=len(var_name)
print(d)
print()

#same question through comprehension...

s="hello hi good afternoon"
l=s.split()
d={var_name : len(var_name)for var_name in l}
print(d)
print()


#2..create a dictonary with word and its length par only if it is a even length...

s="hello hi good afternoon"
l=s.split()
d={var_name : len(var_name) for var_name in l if len(var_name)%2==0}
print(d)
print()


#3..WAP to print index and its word pair if the word is of even length keep as it is otherwise reverse it...

s="hello hi good afternoon"
l=s.split()
d={index:word if len(word)%2==0 else word[::-1] for index,word in enumerate(l)}
print(d)
print()

#4..create a dictonary with character and its ascci value....

s="hello hi good afternoon"
d={var_name : ord(var_name) for var_name in s}
print(d)
print()



#5..WAP to reverse the values in the dictonary if the value is of type string.....

d={"a":1,"b":"hello","c":85,"d":12.3,"e":[1,2,3]}
d={key : var_name[::-1] if isinstance(var_name,str) else var_name for key,var_name in d.items()}
print(d)
print()


#6..create a dictonary of its word and count pair..
s="hello  hello  hi hi good good afternoon"
l=s.split()
d={var_name:l.count(var_name)for var_name in l}
print(d)
print()


#7..WAP to flip the keys and values...

d={"a":1,"b":"hello","c":85,"d":12.3,"e":(1,2,3)}
d1={var_name : key for key,var_name in d.items()}
print(d1)
print()


#8..convert two list in to dictonary

l1=["hello","world"]
l2=[10,20]
d={key:value for key,value in zip(l1,l2)}
print(d)
print()


#9..print first 10 fibbonicci no using for loop......


a=0
b=1
for i in range(10):

    print(a, end=" ")
    c=a+b
    a=b
    b=c
    
print()


#10..for nth fibbonicci number....

a1,b1 =0,1
n=10
for i1 in range(n-1):
    a1,b1=b1,a1+b1
print(a1, end="")
print()

#using while loop
a=0
b=1
i=10-1
count=0
while count<i:
    c=a+b
    a=b
    b=c
    count+=1
if count==i:
    print(a)
print("******************************")

#11..WAP to print a largest number given in the list....

l=[98,14,62,17,56,1,5,96,-2]
first_num_of_list=l[0]

for list_num in l:
    if first_num_of_list<list_num:
        first_num_of_list=list_num
print(first_num_of_list)
print()
    

#using 2nd method
l=[98,14,62,17,56,1,5,96,-2]
for i in range (len(l)-1):
    if l[i]>l[i+1]:
        l[i],l[i+1]=l[i+1],l[i]
print(l[-1])

print(max(l))
print(l.sort())
print(l)
print(l[-1])


#12..WAP to print nth largest number..

l=[98,14,62,17,56,1,5,96,-2]
n=5

for _ in range(n):  
    for i in range (len(l)-1):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
print(l[-n])


#grouping flowers and animal in the below list..

items = ["lotus-flower","lilly-flower","cat-animal","sunflower-flower","dog-animal"]
d={}
for var_name in items:
    word=var_name.split("-")
    value, key=word
    if key not in d:
        d[key]=[value]
    else:
        d[key]+=[value]
print(d)

#using defaultdict

from collections import defaultdict

dd=defaultdict(list)
for element in items:
    w=element.split("-")
    value,key=w
    dd[key]+=[value]  #dd[key].append(value)
print(dd)


#grouping even and odd numbers...

items = [1,2,3,4,5,6,7,8,9,10]
from collections import defaultdict
d=defaultdict(list)
for i in items:
    rem=i%2
    if rem==0:
        d[rem]+=[i]
    else:
        d[rem]+=[i]
print(d)
#

n=10
for i in range(n):
    if i>1:
        for k in range(2,i):
            if i%k==0:
                break
        else:
            print(i)

