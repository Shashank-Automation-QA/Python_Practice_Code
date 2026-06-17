#                                                                                   Exception handling

#handling error and giving hardcoded msz......                                 one try with one except block          

a=1
b=0
try:
    print(a/b)
    l.append(10)

except:
    print("error handled")
    print()

#printing msz as t is .....                                                 one try with multiple except block

a=1
b=0
try:
    print(a/b)
    l.append(10)

except ZeroDivisionError as msg:
    print(msg)
    print()
except NameError as msg:
    print(msg)
    print()

#handling two error at a time....                                        writing more then one exception together 

a=1
b=2
try:
    print(a/b)
    l.append(10)

except (ZeroDivisionError, NameError)as  msg:
    print(msg)
    print()

