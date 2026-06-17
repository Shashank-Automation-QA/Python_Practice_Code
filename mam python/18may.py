#                                                       ****************************pattern printing************************

#WAP to print pattern ->
'''
*
**
***
****
*****
'''

#1st method

for row in range(5):
    for col in range(row+1):
        print("*", end=" ")
    print()

print()


#2nd method

for row in range(1,5+1):
    print("* "*row)

print()

'''

    *
   **
  ***
 ****
*****

'''

for row in range(1,6):
    print(f'{"* "*row:>10}')    
print()

'''
    *
   * *
  * * *
 * * * *
* * * * *
'''


for row in range (1,6):
    print(f'{"* "*row:^10}')

print()
'''
*
*
*
**
*
***
*
****
'''

for row in range (1,5):
    print("*")
    print("*"*row)
print()

'''
*****
****
***
**
*
'''


for row in range(5,0,-1):
    print("* "*row)

print()

'''
*****
 ****
  ***
   **
    *
'''
for row in range(5,0,-1):
    print(f'{"* "*row:>10}')
print()

'''
* * * * *
 * * * *
  * * *
   * *
    *
'''

for row in range(5,0,-1):
    print(f'{"* "*row:^10}')
print()

'''
    *
   * *
  * * *
 * * * *
* * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''
for row in range (1,6):
    print(f'{"* "*row:^10}')
for row in range(4,0,-1):
    print(f'{"* "*row:^10}')
print()

'''
a
ab
abc
abcd
abcde
'''
#1st method..

for row in range(5):
    n=0
    for col in range(row+1):
        print(chr(ord("a")+n), end=" ")
        n+=1
    print()

print()

#2nd method..

pat=""
start="a"
for row in range(4):
    var=chr(ord(start)+row)   #ascci(97)+ row(0) =97  ==> a
    pat=pat+var+" "
    print(pat)














































#palindrome

    

s="kunal bhiya"
s1=s[::-1]
if s==s1:
    print("no is palindrome")
else:
    print("no is not palindr")

print(s.split())























