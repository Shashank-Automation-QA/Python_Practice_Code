#print number of accurance of character..........
s="AABBCCCDAACDA "
s1=""
count=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        s1=s1+str(count)+s[i]
        count=1
print(s1)
print("**********************************************************************************")
print()

# print emojie ...................
for i in range(5):
    print("\U0001F917" ,end=" ")
for i in range(5):
    print("\U0001F62A" ,end=" ")
for i in range(5):
    print("\U0001F637" ,end=" ")
for i in range(5):
    print("\U0001F618" ,end=" ")
for i in range(5):
    print("\U0001F600" ,end=" ")
    
print()
print("************************************************************")
print()

#prime no normal program ............

num=int(input("enter a number "))
for i in range(2,num):
    if num%i==0:
        print("num is not prime")
        break
else:
    print("num is prime")
print("***********************************************************")
print()

#prime no in range of 0 to 50...........

for num in range(2,50):
    for i in range(2,num):
        if num%i==0:
            print(f"{num} is not prime") #if you want to print only prime no then comment this line
            break
    else:
        print(f"{num} is prime")
print("***********************************************************")

            
    


