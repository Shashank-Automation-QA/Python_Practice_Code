#WAF to create a dictonary with character and its ascii value pair..
def char_ascii(string):
    d={char: ord(char) for char in string}
    return d
print(char_ascii("hello"))
print()


#waf to return length of any iterable without using any inbuilt function..

def length(iterable):
    count =0
    for _ in iterable:
        count +=1
        return count
print(length("hello world"))
print()

#WAP to search for a character in a given string and return the currosponding index..

#using inbuilt method

def liner_search(sequence,value):
    return sequence.index(value)

print(liner_search("hello","h"))
print()

#without using inbuilt function...

def linear_search1(sequence,value):
    for index,item in enumerate(sequence):
        if value == item:
            return f"{value} is present in position {index}"
    else:
        return f"{value} is not present in {sequence}"
    
print(linear_search1("hello","z"))
print()

#WAF to count the no of positional and keyword arguments passed to it...

def count_(*args , **kwargs):
    print(len(args),"length of positional arguments")
    print(len(kwargs),"length of keyword arguments")

count_(1,2,3,4,a=10,b=20,c=30)
print()    
    

#WAF to print  message "Hai Everyone" if the user input is not present and if the user input .

def print_msg(msg="hai everyone"):
    print(msg)

#print_msg("good morning")


# a function take variable number of position argments as input . how to check if the arguments that are passed are more than 5

def greet(*args):
    if (len(args))>5:
        print("more then 5 times")

greet(1,2,3,4,5,6)
print()

#***************************************************RECURSION****************************************************************


#WAP to print hello 3 times using recursion


def recursion_(count=0):
    if count==3:
        return
    print("hello")
    count+=1
    recursion_(count)
recursion_()
print()

#WAP to print no from 1 to 10 using recurssion...

def print_no(count=1):
    if count>10:
        return
    print(count)
    count+=1
    print_no(count)
print_no()
print()

#WA recurssion function to print a factorial of number...

def factorial(n, fact=1,i=1):
    if i>n:
        return fact
    fact *=i
    i+=1
    return factorial(n,fact,i)
print(factorial(5))














