#While loop

#when we don't know about length then we actually use while loop

i =1
while i<8:
    print(i)
    i=i+1

i=1
while i<10:
    print(i)
    if(i==3):
        break 
    i +=1

i=0
while i<9:
    i+=1
    if(i==5):
        continue
    print(i)
    
j=0
while j<4:
    print(j)
    j+=1
else:
    print("no longer available after that 3")
print("-----------")
#for loop
list=[3,3,5,"h",62,2]
for i in list:
    if type(i)==type("a"):
        break
    print(i)

for i in list:
    if type(i)==type("a"):
        continue
    print(i)

for i in range(10):
    print("I love you 'TRIPTY'")



