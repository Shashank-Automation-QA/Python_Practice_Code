'''
#WAP to count the no. of alphabets and numbers occurence ....

s1=0
s2=0
def count_(s):
    global s1,s2
    for var_name in s:
    
        if ord("a") <= ord(var_name) <= ord("z")or ord("A")<=ord(var_name)<=ord("Z"):
            s1 +=1
        elif (ord("0"))<=(ord(var_name))<=(ord("9")):
            s2 +=1
    print ("no of alphabets :",s1)
    print ("no of numbers :",s2)

count_("shashank123")    
print(" ")


#write a program to count of no. of words in a sentence....

def count1_(s):
    l=s.split(" ")
    l1=len(l)
    print(l1)

count1_("hi how are you")
print(" ")



#write a program for repeated characters....

def count2_(s):
    for var_name in set(s):
        if s.count(var_name) > 1:
            print(var_name,end=" ")
count2_("hello world")

print(" ")


#write a program to remove the duplicate or repeated characters in the given string.....

def count3_(s):
    res=" "
    for var_name in s:
        if var_name not in res:
            res +=var_name
    print(res)

count3_("hello world")

print(" ")
    
#WAP print duplicate characters without using inbuilt methods...

def count4_(s):
    res=" "
    count=0
    for var_name in s:
        if var_name in res:
            count +=1
            if count > 1:
                print(var_name, end=" ")
        else:
            res=res+var_name
count4_("hello world")

print(" ")


#wap to print all the indices in the given sub string....

def count5_(s,ch):

    for i in range(len(s)): #without using inbuilt function....
        if s[i] == ch:
            print(i,end=" ")
count5_("hello world","o")

print(" ")


#first accurance of the index of the sub string.....

def count6_(s,ch):
    print(s.index(ch))
count6_("hello world","o")



print(" ")     #using inbuilt function....

'''

#first accurance of the index of the sub string.....


def count7_(s,ch):
    count=0
    for i in range(len(s)): #without using inbuilt function.....
        if s[i] == ch:
            count +=1
            if count == 2:
                print(i,end=" ")
count7_("hello world","o")
print(" ")

'''

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




#WAP to create dictonary with vales of integer data type .....

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


'''
