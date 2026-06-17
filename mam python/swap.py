s = "hAi goOd morning"
res=" "
for var_name in s:
    if var_name in "aeiouAEIOU":
        print (var_name,"character is vowel")
        if ord('a')<=ord(var_name)<=ord('z'):
            res=res+ chr(ord(var_name)-32)

        elif ord('A')<=ord(var_name)<=ord('Z'):
            res=res+ chr(ord(var_name)+32)
    else:
        res=res+var_name
print(res)         

