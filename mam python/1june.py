                                                                    #serilization


import json
##############################    serialization -  dump(), dumps()
# loads and dumps ---> variable/object
# load and dump ---> file

#1
data = {"username": "user1", "password": "pwd"}
json_obj = json.dumps(data)
print(json_obj)
print(type(json_obj))

#2
data = None
json_obj = json.dumps(data)
print(json_obj)
print(type(json_obj))

#3
data = {"username": "user1", "password": "pwd"}
data2 = None
with open("sample.json", "w") as file:
    json.dump(data, file)
    json.dump(data2, file)
    print("data dumped successflly")

'''    
################################   de-serialization - load(), loads()
#1
data = {"username": "user1", "password": "pwd"}
json_obj = json.dumps(data)
print(json_obj)
print(type(json_obj))

#2
python_obj = json.loads(json_obj)
print(python_obj)
print(type(python_obj))

#3
data = {"username": "user1", "password": "pwd"}
with open("sample.json") as file:
    data = json.load(file)
    print(data)
    print(type(data))
'''

import pickle
#################################   serialize - dump, dumps
data = "hello"
pck_obj = pickle.dumps(data)
print(pck_obj)
print(type(pck_obj))


data = "hello"
with open("../demo.pkl", "wb") as file:
    pickle.dump(data, file)

#################################   de-serialize - load, loads
python_obj = pickle.loads(pck_obj)
print(python_obj)
print(type(python_obj))


with open("../demo.pkl", "rb") as file:
    data = pickle.load(file)
    print(data)









    
















    
