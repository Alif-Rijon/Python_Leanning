name ="tripty"
age = 20
cgpa =3.99

print ("my name is " + name + ". my age is" , age ,"\n my cgpa is" ,cgpa)

#note + only use for string and "," is use for other data type

#Identation
if 5>2:
    print("Five is greater than two!", end = " ")
    print ('hello testing statement')
print(3+4)
print("I am", 22 , "Years old.")

#Type casting 
x= 10
y = str(x)
print(type(y))
print(y)
print("------------")
a= 5.4
b= int(a)
print(a)
print(b)
print(type(a))
print(type(b))
print("------------")

x,y,z = "orange",11,"Cherry"
print(x)
print(y)
print(z)
print("------------")

x=y=z= "hello"
print(x)
print(y)
print(z)
print("------------")

#Unpacking

number =[1,5,6,7]
x,y,k,z=number
"""print(x)
print(y)
print(k)
print(z)
"""
print(x,y,k,z)

a= 1j+2
print(type(a))
b=22
c= complex(b)
print(c)

b= 2e2 #e means 10 to the power
print(b)
print(type(b))

#Random numbers

import random
print(random.randrange(3,50))