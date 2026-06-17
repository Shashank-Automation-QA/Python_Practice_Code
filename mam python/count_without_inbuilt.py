s= "shashank"
d={}
for var_name in s:
    if var_name not in d:
        d[var_name]=1
    else:
        d[var_name]+=1
print(d)
        
