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