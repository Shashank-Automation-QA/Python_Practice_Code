#  Exampl  of generators                                                                            generator

def func(a,b):
    yield a+b
    yield a*b
    yield a-b
res=func(1,2)
print(next(res))
print(next(res))
print(next(res))
res=func(4,6)
print(next(res))
print(next(res))
print(next(res))
print()

#genarate square numbers of given list.......
l=[1,2,3,4]
def func(a):
    for i in a:
        yield i*i
print(list(func(l)))

#using generator function

g=(i*i for i in [1,2,3,4])
print(list(g))
print()

#wa n fibbonici series usng generators.
a=0
b=1
def fibb(n):
    global a
    global b
    for i in range(n):
        yield a
        c=a+b
        a=b
        b=c
print(list(fibb(10)))
print()


#wa nth fibbonici series usng generators.
a=0
b=1
def fibb(n):
    global a
    global b
    for i in range(n-1):
        c=a+b
        a=b
        b=c
    yield a
print(list(fibb(10)))
print()



#WA function generate only the string with odd length in the given list ........

names=["bob","steve","alex","maya","john"]
d=(i for i in names if len(i)%2!=0)
print(list(d))
print()    

#generate tuple of numeric values given in list ..........

items=["flipkart",2021,"gmail",1.2,[1,2,3],2+3j,True]
l=(i for i in items if isinstance(i,int))
print(tuple(l))
print()
                                  

#generate a list if individual datatype , reverse it else keep it as it is....

items=["flipkart",2021,"gmail",1.2,[1,2,3],2+3j,True]
l=( str(i)[::-1] if isinstance (i,(int,float,complex)) else i for i in items)
print(list(l))
print()

#generate a list of pi values with increasing decimal point numbers up to the user defined number .....

from math import pi

def pi_(n):
    for i in range(n):
        yield round(pi,i)
print(list(pi_(4)))
print()

#using generator function

print(list((round(pi,i) for i in range(1,4))))
print()

















