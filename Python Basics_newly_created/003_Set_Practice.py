# #Set is having 12 methods add(x), update(iterable), remove(x), discard(x), pop(), clear(), union(t), intersection(t), difference(t), issubset(t) and issuperset(t) check below how these methods are used
#
# #Set without element
# # s = set()
#
# #Set with one element
# # s={1} or s={"Shashank"} or s={a} or s={3.5}
#
# #List with one element using constructor
# # s = set([10])
#
# # s={1}
# # print(type(s))
#
# # #below we can see the add() example here add method can add only one value and the adding place is random because set is unordered data type
# # S={1, 2, 3, 5, 6, 7, 8}
# # S.add(4)
# # S.add(9)
# # S.add(10)
# # print(S)
#
# # #below we can see the update() example update method can add multiple value at same time
# # S={1, 2, 3, 5, 6, 7, 8}
# # S.update([4,5,6])
# # print(S)
#
# # #below we can see the remove() example remove() will give key error if given element not found
# # S={1, 2, 3, 5, 6, 7, 8}
# # S.remove(2)
# # print(S)
#
# # #below we can see the discard() example discard() will not give any error if given element not found
# # S={1, 2, 3, 5, 6, 7, 8}
# # S.discard(2)
# # print(S)
#
# # #below we can see the pop() example pop() will remove the random value
# # S={1, 2, 3, 5, 6, 7, 8}
# # S.pop()
# # print(S)
#
# # #below we can see the clear() example clear() will remove all the elements present inside the set and return empty set
# # S={1, 2, 3, 5, 6, 7, 8}
# # S.clear()
# # print(S)
#
# # #below we can see the union() example union() will Combine both sets and remove all the duplicate elements
# # S={1, 2, 3}
# # S1={3, 4, 5}
# # S3=set()
# # S3.update(S.union(S1))              #we cant use Add method here because set allows only immutable objects inside to add
# # print(S3)
#
# # #below we can see the intersection() example intersection() will put only common values of both sets
# # S={1, 2, 3}
# # S1={3, 4, 5}
# # S3=set()
# # S3.update(S.intersection(S1))
# # print(S3)
#
# # #below we can see the difference() example difference() will only put unique values of first set
# # S={1, 2, 3}
# # S1={3, 4, 5}
# # S3=set()
# # S3.update(S.difference(S1))
# # print(S3)
#
# # #below we can see the symmetric_difference() example symmetric_difference() will only put unique values of both set
# # S={1, 2, 3}
# # S1={3, 4, 5}
# # S3=set()
# # S3.update(S.symmetric_difference(S1))
# # print(S3)
#
# ##########################################Activity#################################################
# #Difference b/w pop, remove, discard ?
# #Difference b/w difference and symmetric_difference
# #If a={"apple","yahoo","google"}    a.add({"facebook"})   then    a=?   and   a[1]=?
# #If s={1,2,3,4,5,6,7}      s.add([10,20,30])= ?    and  s.update([10,20,30])
#
#
# #Difference b/w pop, remove, discard ?
# # s.remove(x)      None                 Remove element   (It will give error if element not found)
# # s.discard(x)     None                 Remove safely     (It will not give error if element not found)
# # s.pop()          Element              Remove random element     (Remove random element)
#
#
# #Difference b/w difference and symmetric_difference
# a={1,2,3,4}
# b={3,4,5,6}
# print(a.difference(b))   #{1,2}
#
# a={1,2,3,4}
# b={3,4,5,6}
# print(a.symmetric_difference(b))   #{1,2,5,6}
#
# #If a={"apple","yahoo","google"}    a.add({"facebook"})   then    a=?   and   a[1]=?
# a={"apple","yahoo","google"}
# a.add("facebook")
# print(a)            #{"apple","yahoo","google","facebook"}
# # print(a[1])       This statement will give error because set is not ordered
#
# #If s={1,2,3,4,5,6,7}      s.add([10,20,30])= ?    and  s.update([10,20,30])
# s={1,2,3,4,5,6,7}
# # s.add([10,20,30])    # this is not possible because list is mutable and add method does not allow mutable objects to add on set
# s.update([10,20,30])   #this is possible because it will remove list and add these object as int which is not mutable
# print(s)               #{1, 2, 3, 4, 5, 6, 7, 10, 20, 30}
#
# ############################################ Basic Level (Start here) ######################################
# # Create an empty set
# s={1,}
# s1=set('2')
# print(type(s1))
#
# # Create a set with values: 1, 2, 3, 4
# s={1,2,3,4}
#
# # Add an element to a set
# s={1,2,3,4}
# s.add(5)
# print(s)
#
# # Remove an element using remove()
# s={1,2,3,4}
# s.remove(4)
# print(s)
#
# # Remove an element using discard()
# s={1,2,3,4}
# s.discard(4)
# print(s)
#
# # Find length of a set
# s={1,2,3,4}
# print(len(s))
#
# # Check if element exists in a set
# s={1,2,3,4}
# e=2
# if e in s:
#     print ("element is present")
#
# # Iterate over a set
# s={1,2,3,4}
# for i in s:
#     print(i)
#
# # Clear all elements from a set
# s={1,2,3,4}
# s.clear()
# print(s)
#
# # Copy a set
# s={1,2,3,4}
# s2=s.copy()
# print(s2)
#
# ############################################### Intermediate Level ########################################
# # Find union of two sets
# s={1,2,3,4}
# s1={5,6,7,8}
# print(s.union(s1))
#
# # Find intersection of two sets
# s={1,2,3,4}
# s1={3,4,7,8}
# print(s.intersection(s1))
#
# # Find difference between two sets
# s={1,2,3,4}
# s1={3,4,7,8}
# print(s.difference(s1))
#
# # Find symmetric difference
# s={1,2,3,4}
# s1={3,4,7,8}
# print(s.symmetric_difference(s1))
#
# # Check if one set is subset of another
# s={1,2,3,4}
# s1={1,2}
# print(s1.issubset(s))
#
# # Check if one set is superset
# s={1,2,3,4}
# s1={1,2}
# print(s.issuperset(s1))
#
# # Check if two sets are disjoint
# s={1,2,3,4}
# s1={5,6,7,8}
# print(s.isdisjoint(s1))
#
# # Remove duplicates from a list using set
# s=[1,2,4,1,3,4]
# print(list(set(s)))
#
# # Convert list → set → list
# s=[1,2,3,4]
# print(type(s))
# print(type(set(s)))
# print(type(list(set(s))))
#
# # Find max and min element in a set
# s={1,2,3,4}
# print(max(s))
# print(min(s))
#
# ########################################### Advanced Level (Interview 🔥) ################################
# # Find common elements in multiple sets
# s={1,2,3,4}
# s1={1,2,5,6}
# s2={1,2,7,8}
# s3=s.intersection(s1)
# print(s3.intersection(s2))
#
# # Find unique elements between two datasets
# s={1,2,3,4}
# s1={1,2,5,6}
# print(s.symmetric_difference(s1))
#
# # Count frequency using set + list
# l=[1,1,2,2,2,3,3,4,4,4,4]
# for i in set(l):
#     print(i, l.count(i), "times")
#
# # Create set using comprehension (squares of numbers)
# s={1,2,3,4}
# print(set(i**2 for i in s))
#
# # Find missing numbers from a list using set
# l=[1,4,5,6,7]
# l1=[]
# for i in range(min(l),max(l)):
#     l1.append(i)
# print(set(l1).difference(l))
#
# # Check if two lists contain same elements
# l1=[1,2,3,4,5]
# l2=[2,1,3,5,4]
# if l1.sort() == l2.sort():
#     print("lists are equal")
# else:
#     print("lists are not equal")
#
# # Remove duplicates while maintaining same given order
# l=[1,3,2,1,2,4]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)
#
# # Find pair of elements whose sum = target (use set)
# l = [2, 11, 7, 15]
# target = 18
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if (l[i]+l[j]) == target:
#             print([l[i],l[j]])
#         else:
#             pass
#
# # Detect duplicate values efficiently
# l = [1, 2, 3, 2, 4, 1, 5]
# l1=set()
# for i in l:
#     if l.count(i)>1:
#         l1.add(i)
# print(list(l1))
#
# Use frozenset and explain use case
