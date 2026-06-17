                                                        #*****************sorted()************************

#WAP to sort a list in reversed order....


name=["shashank","nitin","gaurav","neha","rishav"]
sorted_name=sorted(name,reverse=True)



#WAP to sort a list in reversed order based on length....

#Note:--custom sorting because we are chsanging the value of key

name=["shashank","nitin","gaurav","neha","rishav"]
sorted_name=sorted(name,key=len)


#WAP to sort on the base of last character of the elements given in list........ 

name=["shashank","nitin","gaurav","neha","rishav"]

#using normal function
def reverse_string(names):
    return names[-1]
sorted_name1=sorted(name,key=reverse_string)

#using lambda function
f_char=lambda string: string[-1]
sorted_name=sorted(name,key=f_char)
print()

#WAP to sort the list based on the first element of each touple.....

names=[("facebook",8),("apple",5),("instagaram",9),("google",6),("yahoo",5)]
s1=sorted(names)
s= sorted(names,key=lambda element:element[0])
print()

#WAP to sort the dictonary based on key .....

prices={"ACME":45.23,"AAPL":612.78,"IBM":205.55,"HQP":37.20,"FB":10.75}

print(sorted(prices))
print(sorted(prices.items()))
print(sorted(prices.items(),key=lambda item: item[0]))
print()

#WAP to sort the dictonary based on value .....

prices={"ACME":45.23,"AAPL":612.78,"IBM":205.55,"HQP":37.20,"FB":10.75}

print(sorted(prices.items(),key=lambda item: item[1]))
print()

#WAP to sort the dictonary based on length of the key .....

prices={"ACME":45.23,"AAPL":612.78,"IBM":205.55,"HQP":37.20,"FB":10.75}

print(sorted(prices.items(),key=lambda item: len(item[0])))
print()

#WAP to sort the dictonary based on length of the value .....

dail_codes={86:"china",91:"india",1:"united states",62:"indonesia",55:"brazil"}
print(sorted(dail_codes.items(),key=lambda item: len(item[1])))
print()

#WAP to sort the dictonary based on last character of each value .....

dail_codes={86:"china",91:"india",1:"united states",62:"indonesia",55:"brazil"}
print(sorted(dail_codes.items(),key=lambda item:item[1][-1]))
print()

#WAP to find the longest word in the given sentence.........

s="python is a programming  language and programming is fun"
l=s.split()
s_words=sorted(l,key=len)
shortest,*rest,longest=s_words
print(shortest)
print(rest)
print(longest)
print()

#WAP to print the pair of longest non repeated word and its length pair .......

s="python is a programming  language and programming is fun"
words=s.split()
d={word: len(word) for word in words if words.count(word)==1}
s_words=sorted(d.items(),key=lambda item: item[-1])
shortest,*rest,longest=s_words
print(longest)
print()

#WAP to print all the maximum values present in the list......


numbers=[7,4,9,2,8,9,6,4,5,9]
max_nums=[]
largest=max(numbers)
for num in numbers:
    if largest ==num:
        max_nums.append(num)
print(max_nums)


#WAP to print all the shortes words in the sentence ..........

s="python is a programming  language and programming is a  fun"
min_,*rest,_max=sorted(s.split(),key=len)

for word in s.split():
    if len(min_)==len(word):
        print(word)

#************************************************************************grouping anagaram*********************************************************

words=["eat","silent","ate","hello","tea"]
d={}
for word in words:
    key="".join(sorted(word))
    if key not in d:
        d[key]=[word]
    else:
        d[key]+=[word]
print(d)        
