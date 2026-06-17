import os
print(os.getcwd())
os.chdir(r"C:\Users\singh\OneDrive\Desktop\python'")


#wap to read the nth line of file...

n=15
with open ("../sample.txt") as file:
    for line_no, line in enumerate(file,start=1):
        if line_no==n:
            print(line)
print()

#WAP to read first n lines...

n=6
with open("../sample.txt")as file:
    for line_no, line in enumerate(file,start=1):
        if line_no<=n:
            print(line)
print()


                                                          #**********************islice ********************       use for indexing for file lines

#wap to read the nth line of file using islicing...
from itertools import islice
n=2
with open ("../sample.txt") as file:
    lines=islice(file,n-1,n)
    print(list(lines))

#WAP to read first n lines...
n=2
with open("../sample.txt")as file:
    lines=islice(file,n)
    print(list(lines))

#WAP to read 10th to 15th line from a file......
start=10
end=15
with open("../sample.txt")as file:
    lines=islice(file,start-1,end)
    print(list(lines))

#enumerate

with open("../sample.txt")as file:
    for line_no,line in enumerate(file,start=1):
        if 10<=line_no<=15:
            print(line)

#WAP to read last n lines......

n=4
with open("../sample.txt")as file:
    lines_count=0
    for _ in file:
        lines_count+=1
    file.seek(0) #it will take the courser to the number(character) we enter inside    
    lines=islice(file,lines_count-n,lines_count)
    print(list(lines))
print()
                                                                                #or      we can use deque

#deque


from collections import deque
n=2
with open("../sample.txt")as file:
    lines=deque(file,n)
    print(list(lines))


#(((((((#default dict,#counter,#deque))))))))) all present inside the collection so you have to import all of them from collection


#((((((#ziplong,#islice)))))))))))))all present in  the itertool so we have to import it from  that 



    





















