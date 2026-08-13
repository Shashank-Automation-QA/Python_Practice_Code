#*********************************    First-Class Object   ****************************************************
#
# In Python, a first-class object is an object that can be treated like any other value. This means it can:
#  ✅ Be assigned to a variable
#  ✅ Be passed as an argument to another function
#  ✅ Be returned from a function
#  ✅ Be stored in data structures like lists, tuples, and dictionaries
#  ✅ Be created at runtime

#Assign a Function to a Variable Example
def greet():
    return "hello"
v = greet            #Above created function is assigned to a variable
print(v())           #Calling one function with some other name, variable this is also called monkey patching

#Pass a Function as an Argument
def funct1(name):
    return f"hello {name}"

def funct2(function,name):
    print(function(name))

funct2(funct1,"Shashank")

#Return a Function from Another Function
def outer():
    def inner():
        return "inside inner"
    return inner
f=outer()
print(f())

#******************************************  Decorator  ******************************************************

#Decorator is used to add some extra functionality on function without changing function itself

#Syntax >>
             # def decorator(func):                #Step 2 we created decorator for step 1 function
             #      def wrapper():                    # This is inner function which is adding extra functionality to our main step 1 function
             #         print("Before Function")       # This is extra functionality
             #         res = func()                   # This is our main function called inside the inner function
             #         print("After function")        # This is extra functionality
             #         return res
             #      return wrapper                    # Returning the response with extra functionality (main function + Inner function)
             #
             #
             # @decorator
             # def main_func():              #Sep 1 we created simple function
             #     return "main function"
             #
             #
             # print(main_func())            #Step 3 Calling decorator through the name main_func

# Note: Whenever we call (main function) it will give result with (decorator + main function) but if we want the
#         output of (main function) as well as (decorated main function) in that case we can follow below syntax

#Syntax >>
             # def decorator(func):                #Step 2 we created decorator for step 1 function
             #      def wrapper():                    # This is inner function which is adding extra functionality to our main step 1 function
             #         print("Before Function")       # This is extra functionality
             #         res = func()                   # This is our main function called inside the inner function
             #         print("After function")        # This is extra functionality
             #         return res
             #      return wrapper                    # Returning the response with extra functionality (main function + Inner function)
             #
             #
             # def main_func():           #Sep 1 we created simple function
             #     return "main function"
             #
             # original_main_func = main_func                               #Step 3 we have to store our main function inside some variable
             # decorated_main_function = decorator(main_func)      #Step 4 we have to store our decorated main function inside the variable
             #
             # print(original_main_func())                    #Step 5 calling main function without extra code
             # print(decorated_main_function())               #Step 6 calling decorator function with extra code

#*************************************    Activity  ***********************************************************

#WAP to log message before any function execution using decorator
def log_message(funct):
    def message(*args,**kwargs):
        print(f"Hi this is the correct answer for {funct.__name__}")
        res = funct(*args,**kwargs)
        return res
    return message

@log_message
def addition_(a,b):
    return a+b

@log_message
def multiplication_(a,b):
    return a*b

print(addition_(1,2))
print(multiplication_(1,2))

#WAP to put delay of 5 sec before any function execution
import time
def delay(funct):
    def delay_time(*args, **kwargs):
        time.sleep(5)
        res = funct()
        return res
    return delay_time

@delay
def main_funct():
    return "Printing hello"

print(main_funct())

#WAD that execute any program 3 times
def multi_execution(funct):
    def wrapper(*args,**kwargs):
        for i in range(3):
            funct(*args,**kwargs)
    return wrapper

@multi_execution
def addition_(a,b):
    print(a+b)

addition_(2,5)

#WAD that calculates the execution time of any program
import time
def execution_time_calculator(funct):
    def time_calculator(*args,**kwargs):
        start_time = time.time()
        print(funct())
        end_time = time.time()
        return end_time-start_time
    return time_calculator

@execution_time_calculator
def just_function():
    return "function executed"

print(just_function())

#WAD that calculates the no of arguments pass in the function
def arg_len_calculator(funct):
    def len_calculator(*args,**kwargs):
        funct(*args,**kwargs)
        print(len(args), len(kwargs))
    return len_calculator

@arg_len_calculator
def arg_function(a,b,c,d,e,f,g,name="none",age="none" ):
    pass

arg_function(1,2,3,4,5,6,7, name="shashank",age="32" )

#WAD that return only positive values while doing substraction
def only_positive_value(funct):
    def positive_value(*args,**kwargs):
        res=funct(*args,**kwargs)
        return abs(res)
    return positive_value

@only_positive_value
def sub_(a,b):
    return a-b

print(sub_(5,10))

#WAD that counts the number of calls of main function
count=0
def call_counter(funct):
    def counter_(*args,**kwargs):
        global count
        count+=1
        res=funct()
        return res
    return counter_

@call_counter
def spam_():
    return "spam"

print(spam_())
print(spam_())
print(spam_())
print(count)

