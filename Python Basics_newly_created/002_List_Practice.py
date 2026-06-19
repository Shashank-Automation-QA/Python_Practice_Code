#List is having 11 methods append(), extend(), insert(), remove(), pop(), clear(), index(), count() ,sort(), reverse() and copy() check below how these methods are used

#List without element
# t=[]

#List with one element
# t=[1] or t=["Shashank"] or t=[a] or t=[3.5]

#List with one element using constructor
# t=list["10"]

#List with brackets
# t=[1, 2, 3, 4, 5, 2]

# L=[1, 2, 3, 4, 5, 6, 7, 8]
# print(L.append(9))
# print(L.extend([10, 11]))
# print(L.insert(12, 12))
# print(L.remove(12))
# print(L.pop())
# print(L.clear())
# print(L.extend([1, 2, 3, 4, 5, 6, 7, 8]))
# print(L.count(2))
# print(L.index(3))
# print(L.sort())
# print(L.reverse())
# print(L.sort(reverse=False))
# L1 = L.copy()
# L1.append(9)
# print(L)
# print(L1)


# # This way we can short list on the bases of alphabetical order but it will first convert the
# # all list arguments as lowercase and short it according to alphabetical order
# L2 = ["Shashank", "gaurav", "Dhinakaran", "Andy"]
# L2.sort(key=str.lower)
# print(L2)

# L1 = [(4,1), (2,3), (1,2)]
# L1.sort(key=lambda x: x[1])
# print(L1)
