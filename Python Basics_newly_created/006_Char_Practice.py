# There are two most use full methods in python to handle char data type

################################################  ord()  #######################################################
a="A"
print(ord(a))  #==> 65 Basically it will print the ascii value of Capital "A"

################################################  chr()  #######################################################
a="65"
print(chr(65))  #==> A Basically it will print the char of ascii value of "65"

##############  Activity #####################

#WAP to print the asci value of each character
s="Hi Hello How are you"
l=s.split()
for i in l:
    for k in i:
        print(k, ord(k), end=" ")
print(end='\n')

#WAP to count number of digits and alphabet in the string.
#First Method
s="091Singhshashank091"
alphabet=0
number=0
for i in s:
    if ord('a')<=ord(i)<=ord('z') or ord('A')<=ord(i)<=ord('A'):
        alphabet+=1
    else:
        number+=1
print(alphabet, number)

#Second Method
s="091Singhshashank091"
alphabet=0
number=0
for i in s:
    if i.isalpha():
        alphabet+=1
    elif i.isdigit():
        number+=1
print(alphabet, number)