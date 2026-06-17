#WAP to count the no. of alphabets and numbers occurence ....

s="shashank123"
s1=0
s2=0
for var_name in s:
    
    if ord("a") <= ord(var_name) <= ord("z")or ord("A")<=ord(var_name)<=ord("Z"):
        s1 +=1
    elif (ord("0"))<=(ord(var_name))<=(ord("9")):
        s2 +=1
print ("no of alphabets :",s1)
print ("no of numbers :",s2)
print(" ")

#write a program to count of no. of words in a sentence....

s="hi how are you"
l=s.split(" ")
l1=len(l)
print(l1)
print(" ")

#write a program for repeated characters....

s="hello world"
for var_name in set(s):
    if s.count(var_name) > 1:
        print(var_name,end=" ")
print(" ")

#write a program to remove the duplicate or repeated characters in the given string.....

s="hello world"
res=" "
for var_name in s:
    if var_name not in res:
        res +=var_name
print(res)
print(" ")
    
#WAP print duplicate characters without using inbuilt methods...

s="hello world"
res=" "
count=0
for var_name in s:
    if var_name in res:
        count +=1
        if count > 1:
            print(var_name, end=" ")
    else:
        res=res+var_name

print(" ")


#wap to print all the indices in the given sub string....

s="hello world"
ch="o"

for i in range(len(s)): #without using inbuilt function....
    if s[i] == ch:
        print(i,end=" ")

print(" ")


#first accurance of the index of the sub string.....

s="hello world"
ch="o"

print(s.index(ch))

print(" ")     #using inbuilt function....


#first accurance of the index of the sub string.....

s="hello world"
ch="o"
count=0
for i in range(len(s)): #without using inbuilt function.....
    if s[i] == ch:
        count +=1
        if count == 2:
            print(i,end=" ")

print(" ")
print(" ")


#wap to print words starting with vowels....

s="apple is good for health"
l=s.split(" ")
for var_name in l:
    if var_name[0] in "aeiouAEIOU":
        print(var_name)
    else:
        print(var_name,"is not start with vowel")

print("")


#create a list with an even length words.....

s= "hai good afternoon, welcome to afternoon session"
result_list=[]
l=s.split(" ")
for var_name in l:
    if len(var_name)%2==0:
        result_list.append(var_name)
print(result_list)

print(" ")


#WAP to create a list with words ending with vowels....

s="hai good afternoon, welcome to afternoon session"
l=s.split(" ")
result_list=[]
for var_name in l:
    if var_name[-1] in "aeiouAEIOU":
        result_list.append(var_name)
print(result_list)


#WAP to create a set with words ending with vowels....

s="hai good afternoon, welcome to afternoon session"
l=s.split(" ")
result_list=set()
for var_name in l:
    if var_name[-1] in "aeiouAEIOU":
        result_list.add(var_name)
print(result_list)

print(" ")


#WAP to create a list of tuples with words and its length pair.....

s="hai good afternoon, welcome to afternoon session"
l=s.split(" ")
result_list=[]
for var_name in l:
    result_list.append((var_name,len(var_name)))
print(result_list)
    

#WAP to create a dictonary with word and length pair only if the word started with the vowel....

s="apple is good fo health"
l=s.split(" ")
d={}
for var_name in l:
    
    if var_name[0] in "aeiouAEIOU":
        d[var_name]= len(var_name)
print(d)

print(" ")


#create a dictonary with letter and the word starting with that letter pair....

s="apple is a very good fruit for health"
l=s.split(" ")
d={}
for var_name in l:
    if var_name[0] not in d:
        d[var_name[0]]= [var_name]
    else:
        d[var_name[0]].append(var_name)
print(d)

print(" ")

#WAP to create a dictonary of character and its indices pair.....

s="apple is good fo health"
d={}
for var_name in range(len(s)):
    if s[var_name] not in d:
        d[s[var_name]]=[var_name]
    else:
        d[s[var_name]].append(var_name)
print(d)

print(" ")
s


#WAP to create a dictoary with character and its ascii value ....


s="hello world"
d={}
for var_name in s:
    d[var_name]=ord(var_name)
print(d)

print(" ")




#WAP to create dictonary with values of integer data type .....

d={"a":1, "b": "hello" ,"c": 85, "d": 12.3, "e": [1,2,3]}
d1={}
for var_name in d:
    if isinstance(d[var_name],int):
        d1[var_name] = d[var_name]
print(d1)
print(" ")

#2 nd method of above program
d={"a":1, "b": "hello" ,"c": 85, "d": 12.3, "e": [1,2,3]}
d1={}
for key,value in d.items():
    if isinstance(value,int):
        d1[key]=value
print(d1)
print(" ")


#WAP to create a dictonary if the values are string data type reverse it and if other data type then keep at is it .....

d={"a":1, "b": "hello" ,"c": 85, "d": 12.3, "e": [1,2,3]}
d1={}
for key,value in d.items():
    if isinstance(value,str):
        d1[key] = value[::-1]
    else:
        d1[key] = value
print(d1)
print(" ")

###

res=lambda num:num[1]+num[0]

print(res((1,2)))
############################3

l=[[1,2,3],[4,5,6],[7,8,9]]
l1=[]
s=0
for i in l:
    for j in i:
        s=s+j
    l1+=[s]
print(l1)
print(sum(l1))

#################################
l=[1,23,5,4,68,9,3,2,11,12]
for word in l:
    sorted_word=sorted(word,key=len)
    word2=" ".sorted_word()
    

##############################################################################               ###############################################################################


















