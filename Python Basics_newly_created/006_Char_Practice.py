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
