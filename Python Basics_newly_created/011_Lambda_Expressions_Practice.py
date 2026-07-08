#*************************    Lambda Expression / Anonymous Functions  ******************************

#A function which is defined by without name called anonymous function or lambda function

#Syntax:    lambda[args 1, [args 2.....args n]] : expression

#Normal addition function
def add(a,b):
    return a+b
print(add(4,5))

#With Lambda Expression / Anonymous Functions addition
add= lambda a,b : a+b
print(add(3,6))

#With Lambda Expression that return the square of numbers
square= lambda a: a**2
print(square(5))

#With Lambda Expression that return the last element of any sequence
last_element= lambda a: a[-1]
print(last_element([1,2,3,4]))

#With Lambda Expression that return the last n elements of any sequence
last_n_element= lambda seq,n: seq[n::]
print(last_n_element([1,2,3,4],2))

#With Lambda Expression check if the given number is even or odd
even_odd= lambda num: "even" if num%2==0 else "odd"
print(even_odd(5))

#With Lambda Expression return the square and cube of number
square_cube= lambda num: (num**2, num**3)
print(square_cube(5))

#With Lambda Expression check if the given statement is palindrome or not
palindrome= lambda statement: "palindrome" if statement==statement[::-1] else "not palindrome"
print(palindrome("dad"))

#*****************************************    Map()  ****************************************************

#Syntax:   map(function_to_apply, list_of_inputs)

# write a program to check if the numbers are even or odd in the given list using map
l = list(range(10))
even_odd = lambda num: "even" if num % 2 == 0 else "odd"
res = map(even_odd, l)
print(list(res))

# write a program to check if the string is palindrome or not
l = ["madam", "dad", "hello", "google", "level"]
map_palindrome = lambda word: "palindrome" if word==word[::-1] else "not palindrome"
res = map(map_palindrome, l)
print(list(res))

# write a program to create a list of square numbers of the
# numbers in the list
l = [1, 2, 3, 4, 5]
_square=lambda i: i**2
print(list(map(_square, l)))

#to convert the strings to upper case
list_ = ["madam", "dad", "hello", "google", "level"]
upper_=lambda word:word.upper()
print(list(map(upper_,list_)))
#           OR
print(list(map(str.upper,list_)))

# to swap case of the words in the given sentence
sentence = "This IS a BunCh of WORDS"
l=sentence.split()
print(list(map(str.swapcase,l)))

# to convert the negative numbers into positive in the list
numbers = [-9, 2, 5, -4, 8, -2, 7, -12]


# to return the pair of word and its length in the sentence
sentence = "This IS a BunCh of WORDS"

#*****************************************    Filter()  ****************************************************

#Syntax:   filter(function_to_apply, list_of_inputs)

#WAP to extract only even numbers from the given list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
def even_(num):
    if num % 2 == 0:
        return num ** 2
print(list(map(even_, numbers)))      # ==>>  [None, 4, None, 16, None, 36, None, 64]
print(list(filter(even_, numbers)))   # ==>>  [2, 4, 6, 8]

# extract the names which have length > 4
names = ["greg", "steve", "bob", "alexa"]


# Build a list with only even length strings using filter class
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram']

# Return the string if the string is starting with a vowel character"
names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']

# Program to return only positive values in the list using filter class
numbers = [-2, -1, 0, 1, 2]
