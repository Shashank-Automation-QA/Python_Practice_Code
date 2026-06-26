#There are multiple concepts are here which is possible to understand with the help of string datatype
#****************************************** slicing ***************************************************
   # 012345678910
s = "hello world"
print(s[0:len(s):1])   #==>  'hello world'
print(s[::])           #==>  'hello world'
print(s[0:5])          #==>  'hello'
print(s[:5])           #==>  'hello'
print(s[6:len(s):1])   #==>  'world'
print(s[6::])          #==>  'world'
print(s[1:len(s):2])   #==>  'el ol'
print(s[::2])          #==>  'hlowrd'
print(s[::3])          #==>  'hlwl'
print(s)               #==>  'hello world'
#Below once are Important
print(s[-1:len(s):1])  #==>  'd'
print(s[-1:-len(s):1])  #==>  ''
print(s[-1:-11:1])     #==>  ''
print(s[-1::-1])        #==>  'dlrow olleh'
print(s[::-1])         #==>  'dlrow olleh'
print(s[3:19])         #==>  'lo world'
print(s==s[::-1])    #==>  'False'

#*********************************************** object assignment Strings **************************************************************
#String is immutable so we can not assign objects
# s[1] = "z"
# Traceback (most recent call last):
#   File "<pyshell#97>", line 1, in <module>
#     s[1] = "z"
# TypeError: 'str' object does not support item assignment

#*********************************************** String all methods **************************************************************
print(dir(s)) #==>  ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count',
# 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
# 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace',
# 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


#********************************** string methods practise *********************************************

#************** upper(), lower() and swapcase() ***************
s = "hello world"
print(s.upper())  #==>   'HELLO WORLD'
b= s.upper()
print(b)          #==>   'HELLO WORLD'

print(id(s))      #==>    2871000450160
print(id(b))      #==>    2870959834480
print(b)          #==>   'HELLO WORLD'

print(b.upper())  #==>   'HELLO WORLD'
print(b.lower())  #==>   'hello world'

s = "Hello World"
print(s.swapcase())  #==>  'hELLO wORLD'

#WAP to check whether a character is vowel or not and swap its case in the sentence
s="hAi goOd morning"        # o/p should be ==>  "haI gOod mOrning"
s1=""
for i in s:
    if i in "AEIOUaeiou":
        s1=s1+i.swapcase()
    else:
        s1 = s1 + i
print(s1)

#******************* count() ********************
s = 'Hello World'
print(s.count("o"))                       #==>2
print(s.count("o", 5))          #==>1
print(s.count("o", 5, 7))  #==>0

#****************** index(), find(), rindex(), rfind() **********************
print(s.index("e"))                       #==>1
print(s.index("l"))                       #==>2
print(s.index("World"))                   #==>6

# print(s.index("l", 5, 9))  #==> give below mention error
# Traceback (most recent call last):
#   File "<pyshell#126>", line 1, in <module>
#     s.index("l", 5, 9)
# ValueError: substring not found

print(s.find("l", 5, 9))   #==>  -1
print(s.rindex("l"))                      #==>   9
print(s.rfind("o"))                       #==>   7
print(s.rfind("iu"))                      #==>  -1

#*********************** replace() ************************
s = 'Hello World'
print(s.replace("e", "z"))             #==> 'Hzllo World'

s = 'Hello World'
print(s.replace("l", "z", 1))    #==> 'Hezlo World'
print(s.replace("l", "z"))             #==>  'Hezzo Worzd'
print(s.replace("l", "z", 2))    #==> 'Hezzo World'

#*********************** startswith(), endswith() *********************
s = 'Hello World'
print(s.startswith("h"))      #==>  False
print(s.startswith("H"))      #==>  True
print(s.endswith("o"))        #==>  False
print(s.endswith("ld"))       #==>  True

#************************   isalnum() **********************************
#WAP to check if the given character is a special character
a=input("Input character:")
if not a.isalnum():
    print(f"{a} is a special character")

#************************   isinstance() **********************************
#WAP to check if the value is string or not
s = "Shashank"
print("Value is string" if isinstance(s,str) else "value is not string")

#******************************** split() , rspit() *****************************
#split()
sentence = "python is a programming language"
print(sentence.split(" "))                     #==>   ['python', 'is', 'a', 'programming', 'language']
print(sentence.split())                        #==>   ['python', 'is', 'a', 'programming', 'language']
print(sentence.split("z"))                     #==>   ['python is a programming language']
print(sentence.split(" ", 2))     #==>   ['python', 'is', 'a programming language']

#rsplit()
print(sentence.rsplit(" ", 2))    #==>   ['python is a', 'programming', 'language']
print(sentence.split(" "))                     #==>   ['python', 'is', 'a', 'programming', 'language']

print(len(sentence.split(" ")))                #==>   5
print(sentence.split(" ", 2))     #==>   ['python', 'is', 'a programming language']

#rsplit()
print(sentence.rsplit(" ", 2))    #==>   ['python is a', 'programming', 'language']
print(sentence.split())                        #==>   ['python', 'is', 'a', 'programming', 'language']
print(sentence.rsplit())                       #==>   ['python', 'is', 'a', 'programming', 'language']

sentence = 'python,is,a,programming,language'
print(s.split(","))             #==>  ['python', 'is', 'a', 'programming', 'language']

#*************************** join() ******************************
s = "hello"
print("-".join(s))              #==>  'h-e-l-l-o'
print("%".join(s))              #==>  'h%e%l%l%o'
print("ABC".join(s))            #==>  'hABCeABClABClABCo'

sentence1 = "python is a programming language"
l = sentence1.split()
print(l)                        #==>  ['python', 'is', 'a', 'programming', 'language']
print(" ".join(l))              #==>  'python is a programming language'

#**************************** strip() *******************************
s = "      hello     "
print(s.strip())                #==>  'hello'

s = "****#hai*****"
print(s.strip("*#"))            #==>   'hai'
print(s.strip("#"))             #==>   '****#hai*****'

#************************************************** format strings ********************************************************
#############################  {} method  #########################
a= input("enter the name:")
print(f"My name is {a}")

#############################  format method  #########################
a= input("enter the name:")
print("My name is {}".format(a))

###########################  "   %s" % method  #########################
a= input("enter the name:")
print("My name is %s" % a)
