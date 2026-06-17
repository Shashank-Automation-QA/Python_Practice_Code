#write a prime no using one line.........


num=[7,4,5,3,1,2,8,9]
print(list(filter((lambda value:["not prime" if value%i==0 else value for i in range(2,value)]),num)))
print()
