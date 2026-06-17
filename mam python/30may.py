                                                                        #decorator



#write a decorator function to log a msz in (function _name ) before executing any function........

def outer(func):
    def inner(*args,**kwargs):
        print("function name:",func.__name__)
        res=func(*args,**kwargs)
        return res
    return inner

@outer  # multiply = outer(multilpy)
def multiply(a,b):
    return a*b
print(multiply(7,3))
print()

#WA decorator function to input 5 seconds of delay before executing any function...

import time
def delay(func):
    def wrapper(*args,**kwargs):
        time.sleep(0)
        func(*args,**kwargs)
    return wrapper
@delay  #push=delay(push)
def push(element):
    l=[]
    l.append(element)
    print(l)

push("hello")
print()

#WA decorator function that execute any function for 3 time......

def repeat_(func):
    def wrapper(*args,**kwargs):
        for _ in range(3):
            func(*args,**kwargs)
    return wrapper
@repeat_ #spam=repeat_(spam)
def spam():
    print("in spam")
spam()
print()


#WA decorator function which calculates the execution time of any function.......

def execition_time(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        func(*args,**kwargs)
        end=time.time()
        return f"the function {func.__name__} is executed in {end-start} seconds"
    return wrapper
@execition_time
def display():
    time.sleep(0)
    print("in display")
print(display())
print()


#WA decorator function which count the no of arguments pass to a function.......


def count_(func):
    def wrapper(*args,**kwargs):
        print(f"number of args given to {func.__name__} is /are:" ,len(args)+len(kwargs))
        func(*args,**kwargs)
    return wrapper
@count_
def add(a,b,c,d):
    print(a+b+c+d)
add(1,2,3,4)
print()

#WA decorator that returns only the positive value on performing substraction......

def positive(func):
    def wrapper(*args,**kwargs):
        return abs(func(*args,**kwargs))
    return wrapper
    
@positive
def sub_(a,b):
    return a-b
print(sub_(4,5))
print()

#WA decorator function to count the no of function call of the main function ..........

count=0
def no_of_function_calls(func):
    def wrapper(*args,**kwargs):
        global count
        count += 1                  #defines how many times we calling function
        func(*args,**kwargs)
    return wrapper
@no_of_function_calls
def sub(a,b):
    print(a-b)

sub(1,6)
sub(1,5)
sub(1,4)
print(count)
print()

                                                                            #delay of n seconds ....




import time
def n_delay(n):
    def delay(func):
        def wrapper(*args,**kwargs):
            time.sleep(n)
            func(*args,**kwargs)
        return wrapper
    return delay

@n_delay(1)  #@delay    #push=delay(push)
def push(element):
    l=[]
    l.append(element)
    print(l)

@n_delay(0)
def display():
    print("in display")

push("hello")
display()

#WA decorator function to execute a function for n numbers of times......

def n_times(n):
    def repeat_(func):
        def wrapper(*args,**kwargs):
            for _ in range(n):
                func(*args,**kwargs)
        return wrapper
    return repeat_

@n_times(3)
def display():
    print("in display")
display()
print()


#WA decorator function to count the no of decorated function ......

count=0
def count_(func):
    global count
    count+=1                    #defines how many functions are we calling 
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
    return wrapper
@count_
def add_(a,b):
    print(a+b)

@count_
def multiply(a,b):
    print(a*b)

add_(2,3)
add_(4,3)
multiply(2,1)
multiply(3,2)
print(count)
print()
#WA decorator function to create a dictonary of function name as key and function call no as a value.........

d={}
def dict_creater(func):
    def wrapper(*args,**kwargs):
        if func.__name__ not in d:
            d[func.__name__]=1
        else:
            d[func.__name__]+=1
        func(*args,*kwargs)
    return wrapper
@dict_creater
def add(a,b):
    print(a+b)
    
@dict_creater
def sub(a,b):
    print(a-b)

@dict_creater
def multiply(a,b):
    print(a*b)
add(1,2)
sub(3,5)
multiply(5,1)
print(d)
        

#wa decorator function to check if the no is positive add else perform multiplication...
sum_=0
mul=0
def check_(func):
    def wrapper(*args):
        global sum_
        global mul
        for i in args:
            if i >0:
                sum_=sum_+i
            else:
                mul=mul*i
        func(*args)
    return wrapper
@check_
def values(*args):
    print(sum_,mul)
values(2,5,-5,8)
print()


#wa decorator function to check if the arguments are iterable or not if iterable return length else return not terable........
def check_iterable(func):
    def wrapper(*args,**kwargs):
        if isinstance(args,(str,list,tuple,set,dict)):
            return len(*args)
        else:
            return "not iterable"
        func(*args,**kwargs)
    return wrapper
@check_iterable
def display(*args):
    l=[]
    for i in args:
        l.append(i)
    print(l)

print(display([1,2,34,56]))
print()
    
#WA decorator function to reverce the string and give delay of some seconds....
import time 
def reverse_(func):
    def wrapper(*args):
        time.sleep(0)
        func(*args)
    return wrapper
@reverse_
def values1_(var_name):
    print(var_name[::-1])
    
values1_("shashank")
print()
    
