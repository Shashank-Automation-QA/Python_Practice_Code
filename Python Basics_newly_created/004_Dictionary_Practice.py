# #Dictionary is having 11 methods get(), keys(), values(), items(), update(), setdefault(), fromkeys(), pop(), popitem(), clear(), copy() check below how these methods are used
#
# #Dictionary without element
# # d = {}    or   d = dict()
#
# #Dictionary with one element
# # Method                  Example
# # {}                      {"a":1}
# # dict() keyword          dict(a=1)
# # tuple                   dict([("a",1)])
# # zip                     dict(zip(["a", "b"],[1, 2]))    ==>> all keys inside one lista and all values inside another list
# # fromkeys                dict.fromkeys(["a", "b"],1)   ==> when values are same for multiple keys {"a":1, "b":1}  all keys will share the same memory for values
# # assignment              d["a"]=1   ==>> dynamic memory allocation we use this method on loops
#
# #Dict with one element using constructor
# # d = dict(a=1)
# # print(d)
#
# d = {'a': 1, 'b': 2, 'c': 3}
# # print(d.get('a'))  # 1
# # print(d.keys())    # ['a', 'b', 'c']
# # print(d.values())  # ['1', '2', '3']
# # print(d.items())   # [('a', 1), ('b', 2), ('c', 3)]
#
# # d.update({'d':4})
# # print(d)
#
# # d.setdefault('a',0)
# # d.setdefault('d',4)
# # print(d)
#
# # #fromkeys method always use inside the update method otherwise it will just only assign the values to keys but not add in empty dict
# # d1={}
# # d1.update(d1.fromkeys(['e','f','g'],0))
# # print(d1)
#
# # print(d.pop('a'))
# # print(d)
#
# # d.popitem()
# # print(d)
#
# # d2 = d.copy()
# # print(d2)
#
# # del d['a']
# # print(d)
#
# ##########################################Activity#################################################
# #If points={'a':1,'b':2,'c':3} then increment the value of b
# #Difference b/w pop() and popitem()
# #If l=['a','b','c','d'] create a dictionary with "No Value" as value for all keys.
# #If D1={'a':1,'b':2,'c':3} and D2={'c':1,'d':2,'e':3} then D3={**D1,**D2} or D3=D1/D2 what is the o/p D3=?
# #If points={'a':1,'b':2,'c':3} then add one more key 'd' with value 4
#
# #If points={'a':1,'b':2,'c':3} then increment the value of b
# points={'a':1,'b':2,'c':3}
# points.update({'b':points.get('b') + 1})
# print(points)
# # Second Logic without inbuilt function
# points['b']= points['b']+1
# print(points)
#
# #Difference b/w pop() and popitem()
# points={'a':1,'b':2,'c':3}
# print(points.pop('a'))        #pop method is removing specified "a" value from dict and also returning value 1
# print(points.popitem())       #popitem method is removing last value from dict and also returning key and value in
#                               # form of tuple ('c',3)
#
# #If D1={'a':1,'b':2,'c':3} and D2={'c':1,'d':2,'e':3} then D3={**D1,**D2} or D3=D1|D2 what is the o/p D3=?
# D1={'a':1,'b':2,'c':3}
# D2={'d':1,'e':2,'f':3}
# print({**D1,**D2})
# print(D1|D2)
#
# #If points={'a':1,'b':2,'c':3} then add one more key 'd' with value 4
# # without inbuilt method
# points = {'a':1,'b':2,'c':3}
# points['d']=4
# print(points)
#
# # with inbuilt method
# points.update({'e':4})
# print(points)
#
# # with inbuilt method if key will not be present then only it will add the new key
# points.setdefault('f',5)
# print(points)

############################################ Basic Level #################################################

# Create a dictionary with keys: name, age, city
d={"name":"Shashank", "age":31, "city":"Banglore"}
print(d)

# Add a new key-value pair to a dictionary
d={"name":"Shashank", "age":31, "city":"Banglore"}
d.update({"Sex":"male"})
print(d)

# Update value of an existing key\
d={"name":"Shashank", "age":31, "city":"Banglore"}
d.update({"name":"Lavi"})
print(d)

# Remove a key using del
d={"name":"Shashank", "age":31, "city":"Banglore"}
del(d["name"])
print(d)

# Remove a key using pop()
d={"name":"Shashank", "age":31, "city":"Banglore"}
d.pop("city")
print(d)

# Check if a key exists in dictionary
d={"name":"Shashank", "age":31, "city":"Banglore"}
if "name" in d.keys():
    print("key exist")

# Get all keys, values, items
d={"name":"Shashank", "age":31, "city":"Banglore"}
print(d.keys())
print(d.values())
print(d.items())

# Find length of dictionary
d={"name":"Shashank", "age":31, "city":"Banglore"}
print(len(d))

# Access value safely using get()
d={"name":"Shashank", "age":31, "city":"Banglore"}
print(d.get("name"))

# Clear entire dictionary
d={"name":"Shashank", "age":31, "city":"Banglore"}
d.clear()
print(d)

############################################## Intermediate Level ############################################

# Merge two dictionaries
d1={"name":"Shashank", "age":31}
d2={"city":"Banglore", "sex":"male"}
print({**d1,**d2})

# Convert two lists into dictionary (keys + values)
l1=["Name", "Age", "City"]
l2=["Shashank", "31", "banglore"]
d={}
for i in range(len(l1)):
    d[l1[i]]= l2[1]
print(d)

# Count frequency of elements using dictionary
l=[1,2,3,1,2,2,3,4]
d={}
for i in set(l):
    d.update({i:l.count(i)})
print(d)

# Find key with maximum value
d={"Rohit":1, "Ravi":2, "Rahul":6, "Rishi":3}

# Sort dictionary by key
# Sort dictionary by value
# Filter dictionary based on value condition
# Copy dictionary and modify without affecting original
# Create dictionary using comprehension
# Invert a dictionary (swap key-value)


####################################### Advanced Level (Interview 🔥) #########################################

# Count words in a sentence using dictionary
# Group elements by category
# Merge two dictionaries with common keys (sum values)
# Find duplicate values in dictionary
# Flatten a nested dictionary
# Create nested dictionary from list
# Remove keys with specific value
# Find common keys between two dictionaries
# Convert list of tuples into dictionary
# Find missing keys between two dictionaries


