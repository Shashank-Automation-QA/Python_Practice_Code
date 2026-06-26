###################################### Simple If Else #########################################################
#WAP to check if the given character is a special character
a=input("Input character:")
if not a.isalnum():
    print(f"{a} is a special character")

#WAP to check if the iterable is empty or not
l=[1,2,3]
if l:   # bool(l)   ==>   If l is not empty means bool value "True"   ==>    If l is empty means bool value "False"
    print("l is not empty")
else:
    print("l is empty")

#WAP to check if the key is present in the dictionary or not
d={"a":1, "b":2, "c":3}
key='a'
if key not in d:
    print(f"{key} key is not present is d")
else:
    print(f"{key} key is present is d")

#WAP to check no. of keys on dict if the no. is even print dict as it is else add a new key to make it even and print it
d={"a":1, "b":2, "c":3}
if len(d)%2==0:
    print(d)
else:
    d["d"]=4
    print(d)

# WAP to check if the given number is leap year or not
Year=2028
if (Year % 4==0 and Year % 100!=0) or (Year % 400==0):
    print("leap year")
else:
    print("not a leap year")

# WAP to check if enter character is vowel or not if it is vowel then create a dict with char and it ascii value
c='a'
if c in "aeiouAEIOU":
    d=dict.fromkeys(c,ord(c))
    print(d)
else:
    print("the given char is not vowel")


###################################### in Line if #############################################################

# Syntax =>  { if condition: statement1; statement2....etc }
# ***Warning***  in line if cant be written inside the print()

a=3
if a < 5 and a % 2 != 0: print("a is lessthen 5"); print("a is odd number")

###################################### in Line if else ########################################################

# Syntax =>  { (True Block) if condition else (false block) }
# ***Advise*** this could be write in side the print()

#WAP to check if the value of number is greater or not
number=3
print("grater" if number>1 else "not grater")

#WAP to check if the key is present in the dictionary or not
d={"a":1, "b":2, "c":3}
key='a'
print(f"{key} key is not present is d" if key not in d else f"{key} key is present is d")

#WAP to check if the value is string or not
s = "Shashank"
print("Value is string" if isinstance(s,str) else "value is not string")

#WAP to check if the last letter of value is vowel or not
s = "Shashank"
print("Value is vowel" if s[-1] in ("A","E","I","O","U","a","e","i","o","u") else "value is not vowel")

#WAP to check if the list has even numbers of elements
l=[1,2,3,4,5,6,7,8]
print("even number" if len(l)%2==0 else "odd number")

#WAP to check if the first number is even or odd
n = 23456
print("even" if isinstance(n,(int, str)) and int(str(n)[0])%2 == 0 else "odd")

###################################### if elif else ########################################################

#WAP to check greatest of 3 of numbers
a=10
b=20
c=30
if a>b and a>c:
    print("a is greatest")
elif b>a and b>c:
    print("b is greatest")
else:
    print("c is greatest")

#WAP to conver upper case to lower and lower case to upper
#First method
s="Hello"
print(ord('a'))
print(ord('A'))
for i in s:
    if 'a'<= i <= 'z':
        print(chr(ord(i)-32), end="")
    elif 'A'<= i <= 'Z':
        print(chr(ord(i) + 32), end="")

#Second Method
s="Hello"
print(s.swapcase())



