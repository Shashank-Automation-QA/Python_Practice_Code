# WAF that return last dgit of an integer...

def count_1(num):
    b=num%10
    print(b)
count_1(102)
print()

#create a function named tail that takes a sequence and a number n as input and returns the last n elements from the given sequence as a list...

def tail(l,n):
    print(l[-n::])
tail([1,2,3,4],3)
print()    

#WAF to check if the given no is fibbonici no.........

def check_fib_no(number):
    a=0
    b=1
    while a<= number:
        if a == number:
            return f"{number} is a fibo number"
        c=a+b
        a=b
        b=c
    else:
        return f"{number} is not a fibo number"
            
print(check_fib_no(5))
print()




                                                    #***************************lambda expression*************************





#WA lambda function that retuns a square of a function .....

square=lambda num:num**2
print(square(12))
print()

#WA lambda expression to return last element of any sequence........

last=lambda l:l[-1]
print(last([1,2,3,4]))
print()

#WA lambda expression to return last n element of any sequence........

last_n=lambda l,n:l[-n::]
print(last_n([1,2,3,4],2))
print()

#Lambda expressin to check whether the given no is even or odd......

even_odd=lambda num: f"{num} is even" if num%2==0 else  f"{num} is odd"
print(even_odd(4))
print()


#wA lambda expression to return  square and cube of the given number.....
sq_cube= lambda num:(num**2,num**3)
print(sq_cube(4))
print()


#WA lambda expression to check if the given string is palindrome ofr not.....

palindrome=lambda s: "palindrome" if s==s[::-1] else "not palindrome"
print(palindrome("helo"))
print()




                                                    #************************map***************************map class is work similar as for loop






#WAP to check for even and odd numbers in the given list.....................

l=[1,3,4,5,78,6,5]
even_odd=lambda num : "even" if num%2==0 else "odd"
res=map(even_odd,l)
print(list(res))
print()


#wap to check the string is palindrome or not?..........

list_=["madam","dad","hello","level"]
palindrome=lambda element: "palindrome" if element==element[::-1] else "not palindrome"
res=map(palindrome,list_)
print(list(res))
print()

#WAP to convert the string present in the list to upper case.........

list_=["madam","dad","hello","level"]
upper_case=lambda element: element.upper()
res=map(upper_case,list_)
print(list(res))
print()
                                                 #or we can use inbuilt function directly by using class name


print(list(map(str.upper,list_)))
print()


#WAP the program to swap the cases of the wordin the given sentence.....
sentence="This IS a BUnch of WORds"
l=sentence.split()
print(list(map(str.swapcase,l)))
print()

#WAP to convert the negative numbers in to positive in the given list......
numbers=[-9,-5,2,-6]
print(list(map(abs,numbers)))

#WAP to return the word and its length pair in the given string ........

s="hi hello how are you "
l=s.split()
word_len_pair=lambda l: (l,len(l))
print(list(map(word_len_pair,l)))


#to add the element of two list......

l1=[1,2,3,4]
l2=[9,8,5,6]
add_=lambda num:num[0]+num[1] 
print(list(map(add_,zip(l1,l2))))
print()


#WAP to raise the elements of the list to the power of their indecies

l=[1,2,3,4]
power=lambda num: num[1]**num[0]
#note [(0,1),(1,2),(2,3),(3,4)]
print(list(map(power,enumerate(l))))
print()
                                                    #*****************************filter condition***********************



#wap to check no is even or odd......

l=[1,2,3,4]

def even_(num):
    if num %2==0:
        return num**2
print(list(filter(even_,l)))
print(list(map(even_,l)))


#NOTE:- filter will remove the default values[None] and if in return function do some operation (return num**2) it will not work for filter condition but it work for map

#WAP to extract the name which has length more the 4...

l=["shashank","nitin","gaurav","neha"]
def check_len(name):
    if len(name)>4:
        return name
print(list(filter(check_len,l)))
print()

#WAP to build a list with ony even length strings using filter class...........

l=["shashank","nitin","gaurav","neha"]
def even_len(name):
    if len(name)%2==0:
        return name
print(list(filter(even_len,l)))
print()

#same above one using lambda..

even_length=lambda name:len(name)%2==0
print(list(filter(even_length,l)))
print()

#WAP to build a list with only starting with vowel strings using filter class...........

l=["shashank","nitin","gaurav","neha","abhinash"]
def vowel_Start(name):
    if name[0] in "aeiouAEIOU":
        return name
print(list(filter(vowel_Start,l)))
print()

#WAP to build a list only with positive value using filter class...........

l=[-1,-2,3,4,0,5,8,-10]
def positive(number):
    if number >0:
        return number
print(list(filter(positive,l)))
print()

#factorial

def fact(n):
    b=1
    for i in range(1,n+1):
        b=b*i
    print(b)
fact(5)


#
l=[1,2,3,4]
a=lambda n:n**2
print(list(map(a,l)))
#
a= lambda *n:[i**2 for i in n if i%2==0]
print(a(1,2,3,4,5,6,7,8))


#
l=[1,2,3,4]
def fun(n):
    if n%2==0:
        return n
    else:
        return 1
    
print(list(filter(fun,l)))

