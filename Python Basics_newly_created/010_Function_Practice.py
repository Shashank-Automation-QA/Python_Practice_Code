# *******************************************  Function ************************************************************
# Function is basically a block of code which only runs when it is called

# Function Syntax:  ===>>>     def function_name(parameters):
                                 #statement 1
                                 #statement 2
                                 #statement 3
                                 #return data

# Function Calling: ===>>>     function_name(arguments)

def greet(name,age):
    print(f"My name is {name} and age is {age}")

# **************************************  Passing Arguments   *******************************************************

####################################    Passing Positional Arguments   ###############################################
greet("Shashank", 32)

####################################    Passing Keyword Arguments      ##############################################
greet(name="shashank",age=32)

###########################    combination of Passing Keyword and positional Arguments   ############################
greet("shashank", age=32)
# greet( age=32,"shashank",)   ==>>>  It will give syntax error

#** Note ==>> always positional value pass first then keyword otherwise get syntax error

####################################    positional only arguments   ##################################################
def greet(name,age,/):
    print(f"My name is {name} and age is {age}")

greet("shashank", 32)
# greet(name="shashank", age=32)     ==>> It will give syntax error

def greet(name,/,age):
    print(f"My name is {name} and age is {age}")

greet("shashank", 32)
greet("shashank", age=32)
# greet(name="shashank", 32)         ==>> It will give syntax error
# greet(name="shashank", age= 32)    ==>> It will give syntax error

#** Note ==>> before / all the arguments should be positional and should not be keyword

####################################    keyword only arguments   ##################################################
def greet(*,name,age):
    print(f"My name is {name} and age is {age}")

greet(name="shashank", age= 32)
# greet("shashank", 32)              ==>> It will give syntax error
# greet("shashank", age=32)          ==>> It will give syntax error
# greet(name="shashank", 32)         ==>> It will give syntax error

# ** Note ==>> after * all the arguments should be keyword not positional and before * arguments could be positional as well as keyword

################################  Combination of keyword only and positional only   ###############################
def greet(name,/,*,age):
    print(f"My name is {name} and age is {age}")

greet("shashank", age=32)
# greet(name="shashank", age= 32)    #==>> It will give syntax error
# greet("shashank", 32)              #==>> It will give syntax error
# greet(name="shashank", 32)         #==>> It will give syntax error

################################  Variable Number of positional arguments   ##########################################
def function(*args):
    print(args)
    print(*args)

function(1,2,3,4)
function(1)
function()

#**Note ==> *args store all the values inside a tuple

################################  Variable Number of keyword arguments   ##########################################
def function(**kwargs):
    print(kwargs)          #This will provide the dictionary
    print(*kwargs)         #This will provide the only keys
    # print(**kwargs)       This will throw error because we can't unpack dictionary

function(a=1,b=2,c=3,d=4)
function(a=1)
function()

#**Note ==> **kwargs store all the values in dictionary form but we need to pass all the arguments in pair

###########################################  Default parameter   #################################################
def add(a,b,c=0):
    print(a+b+c)

add(1,2)
add(1,2,3)
# print(add())              This will give the syntax error because a and b is not having there default values
