# List is having 11 methods append(), extend(), insert(), remove(), pop(), clear(), index(), count() ,sort(), reverse() and copy() check below how these methods are used

# List without element
t=[]

# List with one element
# t=[1] or t=["Shashank"] or t=[a] or t=[3.5]

# List with one element using constructor
t=list("10")

# List with brackets
t=[1, 2, 3, 4, 5, 2]

L=[1, 2, 3, 4, 5, 6, 7, 8]
print(L.append(9))
print(L.extend([10, 11]))
print(L.insert(12, 12))
print(L.remove(12))
print(L.pop())
print(L.clear())
print(L.extend([1, 2, 3, 4, 5, 6, 7, 8]))
print(L.count(2))
print(L.index(3))
print(L.sort())
print(L.reverse())
print(L.sort(reverse=False))
L1 = L.copy()
L1.append(9)
print(L)
print(L1)


# This way we can short list on the bases of alphabetical order but it will first convert the
# all list arguments as lowercase and short it according to alphabetical order
L2 = ["Shashank", "gaurav", "Dhinakaran", "Andy"]
L2.sort(key=str.lower)
print(L2)

L1 = [(4,1), (2,3), (1,2)]
L1.sort(key=lambda x: x[1])
print(L1)

####################################### List Practice ######################################################

# Reverse a list
s=[1,2,3,4,5]
print(s[::-1])

# Find largest and smallest element
s=[1,2,3,4,5]
print(max(s), min(s))

# Remove duplicates
s=[1,2,3,4,5,2,3]
print(list(set(s)))

# Sort a list without using sort()
s=[1,4,3,5,2,3]
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]>s[j]:
            s[i], s[j] = s[j], s[i]
print(s)

# Merge two lists
l1=[1,2,3,4]
l2=[5,6,7,8]
print([*l1,*l2])

# Find second largest number
s=[1,4,3,5,2,3]
print(s.sort())
print(s[-2])

# Count even and odd numbers
s=[1,4,3,5,2,3]
even=0
odd=0
for i in s:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even, odd)

# Find common elements between two lists
#First Method
l1=[1,4,3,5,2]
l2=[8,2,3,6,7]
print(list(set(l1).intersection(set(l2))))

#Second Method
l1=[1,4,3,5,2]
l2=[8,2,3,6,7]
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)

# Rotate a list
#left rotation output should be like [3,4,5,1,2]
l=[1,2,3,4,5]
rotation = 2
for i in range(rotation):
    first = l.pop(0)
    l.append(first)
print(l)

#left rotation using slicing
l=[1,2,3,4,5]
r = 2
r = r%len(l)
print(l[r:]+l[:r])

# Flatten a nested list single level and multi level
