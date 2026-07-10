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

# WAF to add the elements of two lists.
l1=[1,2,3,4]
l2=[9,5,4,6]
list_addition = lambda num1,num2: num1+num2
print(list(map(list_addition,l1,l2)))
#               OR
list_addition1 = lambda num:num[0]+num[1]
print(list(map(list_addition1,zip(l1,l2))))

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
positive= lambda num: abs(num)
print(list(map(positive,numbers)))
#           OR
print(list(map(abs,numbers)))

# to return the pair of word and its length in the sentence
sentence = "This IS a BunCh of WORDS"
l=sentence.split()
word_length= lambda l:(l,len(l))
print(list(map(word_length,l)))

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
grater_len=lambda word: len(word)>4
print(list(filter(grater_len,names)))

# Build a list with only even length strings using filter class
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram']
even_len= lambda word: len(word)%2==0
print(list(filter(even_len,names)))

# Return the string if the string is starting with a vowel character"
names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']
vowel_starting=lambda word: word[0] in "AEIOUaeiou"
print(list(filter(vowel_starting,names)))

# Program to return only positive values in the list using filter class
numbers = [-2, -1, 0, 1, 2]
positive_value=lambda value: value>=0
print(list(filter(positive_value,numbers)))

#*****************************************    Sorted()  ****************************************************

#Syntax:        sorted(iterable,*,key=none,reverse=false)

#WAP to sort a string value and create new list and also reverse the string value
s="python"
r=sorted(s)
r=sorted(s,reverse=True)
print(r)

#WAP to sort a list value and create new list and also reverse the string value
name=["google", "amazon", "gmail", "walmart", "flipkart", "microsoft", "apple"]
s_names= sorted(name)
print(s_names)
s_names= sorted(name, reverse=True)
print(s_names)
s_names= sorted(name, reverse=True, key=len)
print(s_names)

#*****************************************    Custom Sorted()  ************************************************
#WAP to sort a list on the base of first character of each elements given in list.
name=["google", "apple", "amazon", "gmail"]
#############Default sorting
s_name= sorted(name)
print(s_name)   # ==>> ['amazon', 'apple', 'gmail', 'google']

#############Normal function for key
def first_char(string):
    return string[0]
s_name=sorted(name,key=first_char)
print(s_name)   # ==>> ['apple', 'amazon', 'google', 'gmail']

#############Lambda expression for key
first_char = lambda character:character[0]
s_name=sorted(name,key=first_char)
print(s_name)   # ==>> ['apple', 'amazon', 'google', 'gmail']

#WAP to sort a list on the base of last character of each elements given in list using lambda function
name=["google", "apple", "amazon", "gmail"]
last_character= lambda character:character[-1]
s_name=sorted(name, key=last_character)
print(s_name)

#WAP to sort the list based on the 1st element of each tuple.
l=[("google",2), ("apple",5),("amazon",6),("gmail",4)]
first_element = lambda ele:ele[0][0]
s_list= sorted(l,key=first_element)
print(s_list)

#WAP to sort the dictionary based on the keys
d={"acme":45.23, "apple":612.5, "ibm":78, "hpq":89.25}
sorted_keys = sorted(d)
print(sorted_keys)      # ==>>  ['acme', 'apple', 'hpq', 'ibm']

sorted_keys = sorted(d.items())
print(sorted_keys)      # ==>>  [('acme', 45.23), ('apple', 612.5), ('hpq', 89.25), ('ibm', 78)]

dict_key_sort = lambda value:value[1]
sorted_keys = sorted(d.items(),key=dict_key_sort)
print(sorted_keys)      # ==>>  [('acme', 45.23), ('ibm', 78), ('hpq', 89.25), ('apple', 612.5)]

#WAP to group anagram
words = ['eat', 'silent', 'ate', 'hello',  'listen', 'tea']
d = {}
for word in words:
    key="".join(sorted(word))
    if key not in d:
        d[key]=[word]
    else:
        d[key].append(word)
print(d)

