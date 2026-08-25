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
a="$"
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

#************************************************** format strings **********************************************
#############################  {} method  #############################
a= input("enter the name:")
print(f"My name is {a}")

#############################  format method  #########################
a= input("enter the name:")
print("My name is {}".format(a))

###########################  "   %s" % method  ########################
a= input("enter the name:")
print("My name is %s" % a)

#*********************************  Reversing string with 4 different methods  **********************************
#********* Slicing Method *********
s="Shashank"
print(s[::-1])

#********* Range Method ***********
s="Shashank"
for i in range(-1,-len(s)-1,-1):
    print(s[i], end="")
print(end='\n')

#********* Concatenation ***********
s="Shashank"
res=""
for i in s:
    res=i+res
print(res)

#*********   Reversed()  ***********
s="Shashank"
for i in reversed(s):
    print(i, end='')

# WAP to validate below scenario
'''
test_password_1 = "Python2026"  # Should pass
test_password_2 = "python 20"   # Should fail (has space, no uppercase)
test_password_3 = "PYTHONCODE"  # Should fail (no lowercase, no number)
'''

password =  "python2026"
small_alpha_count=0
capital_alpha_count=0
num_count=0

if " " in password:
    print("Space not allowed in password")
else:
    for i in password:
        if ord('a')<=ord(i)<=ord('z'):
            small_alpha_count+=1
        elif ord('A')<=ord(i)<=ord('Z'):
            capital_alpha_count+=1
        elif i in "0123456789":
            num_count+=1
    else:
        if small_alpha_count >0  and capital_alpha_count >0 and num_count >0:
            print("pass is correct")
        else:
            print("include capital letter, small letter and numbers in your password")

# WAP to validate below scenario
'''
user_input_1 = "+1 (555) 123.4567 "
user_input_2 = "555-123-ABCD"
'''
phone = "+1 (555) 123.4567 "
phone = phone[::-1]
correct_number=""
count=0
for i in phone:
    if i.isdigit():
        correct_number = i + correct_number
        count+=1
        if count>9:
            break
    elif i.isupper() or i.islower():
        print("incorrect phone number")
        break
print(correct_number)

#Wap to validate below scenario
server_logs = """INFO: 2026-08-24 - System booted up normally.
CRITICAL: 2026-08-24 - Database connection lost.
WARNING: 2026-08-24 - High memory usage detected.
CRITICAL: 2026-08-24 - Payment Gateway timeout, database is locked.
INFO: 2026-08-24 - User admin logged in."""

data_base_count=0
list_server_logs = server_logs.split("\n")
for msg in list_server_logs:
    if "CRITICAL:" in msg:
        list_msg= msg.lower().split()
        data_base_count+=list_msg.count("database")
print(data_base_count)

# Practice Challenge 6: "The Receipt Printer"
# You are building the software for a coffee shop register. You need to print a receipt that
# is exactly 30 characters wide.
# The title must be perfectly centered with = padding.
# The item name must align to the left.
# The price must align to the right, and the price needs to be padded with zeros (e.g., $04.50).

# Goal Output:
# Plaintext
# =========== RECEIPT ==========
# Cappuccino              $04.50

# receipt_width = 30
# title = " RECEIPT "
# item = "Cappuccino"
# price = "4.5"  # Needs to become $04.50

Name= input("Enter purchase item name")
Price= input("Enter purchase item price")
total_item_len= len(Name)+len(Price)
space_len = 30-total_item_len
space_len = " "*(space_len-1)
print(f"=========== RECEIPT ==========\n{Name}{space_len}${Price}")

# Challenge 3: The Credit Card Masker
# For security, you must never display a full credit card number on a receipt or screen.
# Goal: Hide all numbers except the last 4, replacing the hidden ones with *.
# Expected Output: ************5566
# cc_number = "1234567891015566"

cc_number = "1234567891015566"
last_digit = cc_number[len(cc_number)-4:len(cc_number):]
print( (len(cc_number)-4)*"*" + str(last_digit) )

# Count repeated characters of the String
# text="Indepedence"

text= "Indepedence"
for i in text:
    if text.count(i)>1:
        print(i,text.count(i))

# get repeated word count
# text = "Python is easy and Python is powerful"
text = "Python is easy and Python is powerful"
lis_text = text.split()
for word in lis_text:
    if lis_text.count(word) > 1:
        print(word,lis_text.count(word))

#ger vowels count of the string
# text = "Python is easy and Python is powerful"
text = "Python is easy and Python is powerful"
count=0
for i in text:
    if i in "AEIOUaeiou":
        count+=1
print(count)


