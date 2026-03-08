thistouple=('h',5,3)
print(thistouple)

this=("hello",)
print(type(this))

x=tuple((3,5))
print(x)
y=list(x)
y[1]='h'
x=tuple(y)
print(x)

for i in range(len(x)):
    print("tuple ",i,":",x[i])

i=0
while(i<len(x)):
    print("While loop ",i,x[i])
    i=i+1