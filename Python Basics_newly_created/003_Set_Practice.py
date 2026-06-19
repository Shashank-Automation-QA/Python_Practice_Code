#Set is having 12 methods add(x), update(iterable), remove(x), discard(x), pop(), clear(), union(t), intersection(t), difference(t), issubset(t) and issuperset(t) check below how these methods are used

#Set without element
# s = set()

#Set with one element
# s={1} or s={"Shashank"} or s={a} or s={3.5}

#List with one element using constructor
# s = set([10])

# s={1}
# print(type(s))

# #below we can see the add() example here add method can add only one value and the adding place is random because set is unordered data type
# S={1, 2, 3, 5, 6, 7, 8}
# S.add(4)
# S.add(9)
# S.add(10)
# print(S)

# #below we can see the update() example update method can add multiple value at same time
# S={1, 2, 3, 5, 6, 7, 8}
# S.update([4,5,6])
# print(S)

# #below we can see the remove() example remove() will give key error if given element not found
# S={1, 2, 3, 5, 6, 7, 8}
# S.remove(2)
# print(S)

# #below we can see the discard() example discard() will not give any error if given element not found
# S={1, 2, 3, 5, 6, 7, 8}
# S.discard(2)
# print(S)

# #below we can see the pop() example pop() will remove the random value
# S={1, 2, 3, 5, 6, 7, 8}
# S.pop()
# print(S)

# #below we can see the clear() example clear() will remove all the elements present inside the set and return empty set
# S={1, 2, 3, 5, 6, 7, 8}
# S.clear()
# print(S)

# #below we can see the union() example union() will Combine both sets and remove all the duplicate elements
# S={1, 2, 3}
# S1={3, 4, 5}
# S3=set()
# S3.update(S.union(S1))              #we cant use Add method here because set allows only immutable objects inside to add
# print(S3)

# #below we can see the intersection() example intersection() will put only common values of both sets
# S={1, 2, 3}
# S1={3, 4, 5}
# S3=set()
# S3.update(S.intersection(S1))
# print(S3)

# #below we can see the difference() example difference() will only put unique values of first set
# S={1, 2, 3}
# S1={3, 4, 5}
# S3=set()
# S3.update(S.difference(S1))
# print(S3)

# #below we can see the symmetric_difference() example symmetric_difference() will only put unique values of both set
# S={1, 2, 3}
# S1={3, 4, 5}
# S3=set()
# S3.update(S.symmetric_difference(S1))
# print(S3)

##########################################Activity#################################################
#Difference b/w pop, remove, discard ?
#Difference b/w difference and symmetric_difference
#If a={"apple","yahoo","google"}    a.add({"facebook"})   then    a=?   and   a[1]=?
#If s={1,2,3,4,5,6,7}      s.add([10,20,30])= ?    and  s.update([10,20,30])


#Difference b/w pop, remove, discard ?
# s.remove(x)      None                 Remove element   (It will give error if element not found)
# s.discard(x)     None                 Remove safely     (It will not give error if element not found)
# s.pop()          Element              Remove random element     (Remove random element)


#Difference b/w difference and symmetric_difference
a={1,2,3,4}
b={3,4,5,6}
print(a.difference(b))   #{1,2}

a={1,2,3,4}
b={3,4,5,6}
print(a.symmetric_difference(b))   #{1,2,5,6}

#If a={"apple","yahoo","google"}    a.add({"facebook"})   then    a=?   and   a[1]=?
a={"apple","yahoo","google"}
a.add("facebook")
print(a)            #{"apple","yahoo","google","facebook"}
# print(a[1])       This statement will give error because set is not ordered

#If s={1,2,3,4,5,6,7}      s.add([10,20,30])= ?    and  s.update([10,20,30])
s={1,2,3,4,5,6,7}
# s.add([10,20,30])    # this is not possible because list is mutable and add method does not allow mutable objects to add on set
s.update([10,20,30])   #this is possible because it will remove list and add these object as int which is not mutable
print(s)               #{1, 2, 3, 4, 5, 6, 7, 10, 20, 30}