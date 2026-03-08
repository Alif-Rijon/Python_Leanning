myset={"hello","world",4,5,7,6,7,7} #set doesn't take dublicate value
print(myset)
print(len(myset))
print(type(myset))

#Only can access set using for loop and can not access it indexing because set is unindexed
for i in myset:
    print(i)

#but we can add item in set
myset.add("Rijon")
myset.add("Alif")
print(myset)
myset.remove("Rijon") #if doesn't match value then it give an error 
myset.discard("Alf") #but it doesn't give error
print(myset)