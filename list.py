number = [1,4,4,5,"Rjoj",'r']
number.append(5)
number.copy()

print(number)
a=number.count(4)
print(a)

b = number.index(4)
print(b)

number1=["rijon",5,3,9,44]
c=number1.insert(2,"tijo")
print(c) # it returns none because insert() function return none 

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

fruits.pop(0)
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.reverse()
print(fruits)

number3=[1,2,5,2,4,7,4,66,45]
number3.sort()
print(number3)

print(number3[-3])  #-3 means last 3 number item  and count start with 1
print(number3[3:5]) #count start with 0
print(number3[2:])
print(number3[-4:-1])  #-1 excluded

if 66 in number3:
    print("Yes present")

# We can change item value

new = ['hello','now',5,87]
new[1:3]=['changed',44]  #there also be 3 excluded
print(new)

for x in new:
    print(x)

for i in range(len(new)):
    print(i)
