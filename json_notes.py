#need to remember these 4 names clearly:
# 1.json.dumps()
# ->convert python object --> json string

# 2.json.loads()
# ->convert json string --> python object

# 3.json.dump()
# ->write python object --> json file

# 4.json.load()
# ->read json file --> python object

# ---> s in dumps and loads means string
# ---> no s means file

import json

# Ex:

data ={"name": "Rijon", "age": 22} #normal dictionary
json_data = json.dumps(data,indent=4) # truns to json where data keep as string

print(json_data)
print(type(json_data))
print(type(data))

# Ex: 
print("---------")

json_text = '{"name":"Rijon","age":22}' #-->this is string ,for converting it must need to be string
data = json.loads(json_text) #onverted to dictionary

print(data)
print(type(data))
print(data["name"])

print("----------")

import json

data ={
    "name":"Rijon",
    "skills":["linux","python","git"]
}

with open("data.json","w") as file:
    json.dump(data,file)


print("----------")

with open("data.json","r") as file:
    data = json.load(file)

print(data)
print(data["skills"])

#or another way to open file

file1= open("data.json","r")
load = json.load(file1) #here json.load --> convert json data into python data .that's why we can access --> load["skills"] otherwise we can't access this because we know that json only take as string so i can't call them as dict
print(load)
print(load["skills"])
file.close()

print("---------")

# we can make json pretty

data2 ={
    "info":"making json pretty",
    "need":["indent","=","4"]
}

pretty = json.dumps(data2,indent =4)
print(pretty)
print(type(data2))
print(type(pretty))

print("---------")

# Demo real-life example
import json

server_config = {
    "server":"nginx",
    "port":80,
    "ssl":False,
    "allowed_ips":["192.168.1.10","192.168.1.20"]
}

with open ("server_config.json","w") as file:
    json.dump(server_config,file,indent=4)

#--->later we need to access that
with open("server_config.json","r") as file:
    config = json.load(file)

print("Server:",config["server"])
print("Port:",config["port"])