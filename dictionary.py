mydict = {
    "name":"Rijon",
    "id": "23-52671-2",
    "year":2023
}
print(type(mydict))
print(mydict)
print(mydict["id"])
print(len(mydict))

print(mydict.keys()) #using keys i can get all keys of dictionary
print(mydict.values())#using values i can get all values of dictionary
mydict["semester"]="8th" # add keys
print(mydict)
mydict["semester"]="9th" #change value
print(mydict)

print(mydict.items())

mydict.update({"session":"23-24"}) #we can also add or update values using update method
print(mydict)

for i in mydict:
    print(mydict[i])  #it shows values of dictionary
print("--------")
for i in mydict.values():
    print(i)

print("---------")
for i in mydict:
    print(i)  #returns keys

print("----")
for i,j in mydict.items():
    print(i,":",j)

#Nested dictionary

myFamily ={
    "child1":{
        "name":"Rijon",
        "age": 20
    },
    "child2":{
        "name":"Alif",
        "age":22

    }
}
print(f"this is nested dict test where keys are{myFamily.keys()} and values are {myFamily.values()}")
print(myFamily)
print(myFamily.items())
print(myFamily.keys())
print(myFamily.values())
print(len(myFamily))

for i in myFamily:
    print(myFamily[i])