# #Tuple is heaving 2 methods count() and index() check below how these methods are used
#
# #Tuple without element
# # t=()
#
# #Tuple with one element
# # t=(1, )
#
# #Tuple with one element using constructor
# # t=tuple("a")
#
# #Tuple with brackets and without brackets
# # t=(1, 2, 3, 4, 5, 2)
#         #or
# # t = 1, 2, 3, 4, 5, 2
# #
# #
# # print(t.count(2))
# #
# # #without arguments
# # print(t.index(2))
# #
# # #with start index arguments
# # print(t.index(2, 1))
# #
# # #with start and stop index arguments
# # print(t.index(2, 2, len(t)))
#
# ##########################################Activity#################################################
#
# #How to create single value tuple?
# #If T1=(1,2) and T2=(3,4) then what is the output of C = (*T1,*T2)
# #If T=(1,2,3,4,["hai", "hellow", 23], "python") then output for T[4][0][-1]=?
# #T[1:3]=["hai", 10] then T=?
# #If a=[1,2,3] and b[4,5,6] then print([a,b])=? and print((a,b))=?
#
#
# #How to create single value tuple?
# t=(1,)
# print(type(t))
# print(t)
#
# #If T=(1,2,3,4,["hai", "hellow", 23], "python") then output for T[4][0][-1]=?
# T=(1,2,3,4,["hai", "hellow", 23], "python")
# print(T[4][0][-1])   # i
#
# #If a=[1,2,3] and b=[4,5,6] then print([a,b])=? and print((a,b))=?
# a=[1,2,3]
# b=[4,5,6]
# # print([a,b])    #It became list of list ==>>  [  []      []    ]
# # print((a,b))    #It became tuple of list ==>>  (  []      []    )
#
# # BASIC LEVEL
#
# # 1. Create a tuple with 5 elements and print first and last element.
# t=(1,2,3,4,5)
# print(t[0])
# print(t[-1])
#
# # 2. Create a single element tuple and print its type.
# t = (1,)
# print(type(t))
#
# # 3. Given t = (10, 20, 30, 40, 50), print the 3rd element.
# t = (10, 20, 30, 40, 50)
# print(t[2])
#
# # 4. Find the length of a tuple.
# t = (10, 20, 30, 40, 50)
# print(len(t))
#
# # 5. Check if a value exists in tuple t = (1, 2, 3, 4).
# t = (1, 2, 3, 4)
# value = 2
#
# #with for loop
# for i in t:
#     if value == i:
#         print(value, "value is present in tuple")
#
# #without for loop
# if value in t:
#     print(value, "value is present in tuple")
#
# # INTERMEDIATE LEVEL
#
# # 6. Concatenate two tuples.
# t1 = (1, 2, 3, 4)
# t2 = (1, 2, 3, 4)
# print((*t1,*t2))
#
# # 7. Repeat a tuple 3 times using * operator.
# t1 = (1, 2, 3, 4)
# print(t1*3)
#
# # 8. Count occurrences of element in t = (1, 2, 2, 3, 2).
# t = (1, 2, 2, 3, 2)
# s={*t}
# for i in s:
#     print(i, t.count(i), "times")
#
# # 9. Find index of an element in tuple.
# t = (1, 2, 2, 3, 2)
# print(t.index(2))
#
# # 10. Loop through tuple and print elements.
# t = (1, 2, 2, 3, 2)
# for i in t:
#     print(i)
#
# # 11. Convert list to tuple.
# t = [1, 2, 2, 3, 2]
# print(tuple(t))
#
# # 12. Convert tuple to list.
# t = (1, 2, 2, 3, 2)
# print(list(t))
#
# # ADVANCED LEVEL
#
# # 13. Swap two elements in a tuple.
# t = (10, 20, 30, 40)    #output ==>>   t = (40, 20, 30, 10)
# l=list(t)
# l[0]   =  l[0] + l[-1]
# l[-1]  =  l[0] - l[-1]
# l[0]   =  l[0] - l[-1]
# print(tuple(l))
#
# # 14. Remove duplicates from a tuple.
# t = (1, 2, 2, 3, 2)
# s=set(t)
# print(tuple(s))
#
# # 15. Find max and min element in tuple.
# t = (1, 2, 2, 3, 2)
# print (max(t))
# print (min(t))
#
# # 16. Given t = (1, 2, 3, 4), create new tuple with squares.
# #######################################First logic######################################
# t = (1, 2, 2, 3, 2)
# l = list(t)
# l1 = []
# for i in l:
#     l1.append(i*i)   # or   l1.append(i**2)
# print(tuple(l1))
# #######################################Second Logic######################################
# t = (1, 2, 2, 3, 2)
# print(tuple(i**2 for i in t ))
#
# # 17. Merge two tuples and sort the result.
# t = (1, 2, 2, 3, 2)
# t1 = (1, 2, 2, 3, 2)
# l= ([*t,*t1])
# l.sort()
# print(tuple(l))
#
# # 18. Unpack tuple into variables.
# t=(1,2,3)
# a,b,c = t
# print(a,b,c)
# ############################## If values are more and variables are less ###########################
# t=(1,2,3,4,5)
# a, *b, c = t
# print(a)    #1
# print(b)    #[2,3,4]
# print(c)    #5
#
# # #If middle values needs to be ignor please use _ as variable is will show other people these values are
# # not used anywhere but still _ will store values
# t=(1,2,3,4,5)
# a, *_, c = t
# print(a)    #1
# print(_)    #
# print(c)    #5
#
# # 19. Access element from nested tuple:
# t = (1, (2, 3), (4, (5, 6)))
# print(t[2][1][0])  #Output  ==>>  5
#
# # 20. Count total elements in nested tuple.
# # 21. Flatten a nested tuple.
#
# # # INTERVIEW / LOGIC BASED
# #
# # 22. Write program to return multiple values using tuple.
# def cal(a,b):
#     return (a+b), (a*b)   #Output ==>>  (sum,product) in form of tuple
#     # basically if return statement is returning more then one values then it will return in the form of tuple
#
# # 23. Check if tuple can be used as dictionary key.
# #Yes, we can use tuple as dictionary key because keys should always immutable and tuple is immutable
#
# # 24. Find common elements between two tuples.
# t1 = (1, 2, 3, 4, 5)
# t2 = (4, 5, 6, 7, 8)
# print(tuple(set(t1).intersection(set(t2))))
#
# # 25. Extract even numbers from tuple:
# t = (1, 2, 3, 4, 5)
# print(tuple(i for i in t if i%2==0))
