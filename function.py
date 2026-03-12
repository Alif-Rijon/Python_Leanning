#function can be two type -->built in function and user difined function 
#if any function return type then it must use print for showing

#now we show 4 types of function
#1 no input , no return

def function_1():
    a=4
    b=20
    c=a+b
    print(c)

function_1()

#2 take input ,no return

def function_2(a,b,c):
    d=a+b*c
    print(d)

function_2(2,5,6)

#3 no input, return

def function_3():
    c="hello function"
    return c

greetings = function_3()
print(greetings)

#4 take input, return

def function_4(a,b,c): #a,b,c are parameter
    d=a*b%c
    return d

result=function_4(4,5,6) #4,5,6 are arguement and it also called positional arguement

print(result)

#default value

def function_5(country = "Bangladesh"):
    print(f"My country name {country}")

function_5()

#we can also take key value arguement ,in this way maintain order does't matter

def function_6(name,age,country="Bangladesh"):
    return (f"My name is {name}.My age is {age}.My country name is {country}")

info=function_6(age=23,name="MD RIJON SIKDER ALIF") #It's called keyword arguement
print(info)

#Example
number =[3,5,2,7]
multiply_number=[]
print("Normal list:", number)
def function_7(lis):
    for i in range(len(lis)):
        multiply=lis[i]*3
        multiply_number.append(multiply)
    return multiply_number
function_7(number)
print("Updated List:", multiply_number)
print(number)

#if we don't know how many positional arguement passed in my function then we can use --> *args ---> it takes value in tuple
#if we don't know how many keyword arguement passed in mu function then we can use --> **kwargs ---> it takes values as dictionary
def function_8(*name):
    print(type(name)) 
    print(name)
    print(name[2])
function_8("rijon;",23,'f')

#it's actually use when we want to create flexible functions:

#ex: a function that calculate the sum of any number of values
def function_9(*number):
    total=0
    for i in number:
        total +=i
    print(total) 

function_9(1,1,1,1,1)


""" Lambda functions --->anonymous function-->Unnamed

--> it can take any number of arguement but can only have one expression
-->it can not take print function ,it only return

syntax--> lambda arguements:expression
        """     
x=lambda a: a+20
print(x(5))

x=lambda a,b,c,d: a-b+c*d
print(x(2,3,4,5))

# lambda function use in another function
def function_10(n):
    return lambda a:a*n
doubler = function_10(2)
print(doubler(9))

# Lambda with build in function
#-->map(func,*iterables(ker oper apply korte chacchi)) function --->map object
number =[8,3,2,5,6]
doubled = list(map(lambda x:x*2,number))
print(doubled)

#filter(func,*iterables)
# even= list(map(lambda x:x%2==0,number))
even = list(filter(lambda x:x%2==0,number))
print(even)

# sorted(*iterables,key=(which order --> defined by lambda function))
student=[("rijon",20),("alif",33),("tripty",21)]
sort= sorted(student,key= lambda x:x[1])
print(sort)


#Scope
# python follows LEGB rule when looking up varible name,and searches for them in this order
""" 
L=local
E=enclosing(inside enclosing function froom inner to outer)
G=Global
B=Built in 

//
if i want change global varible inside a function i will use global keyword  --->global  only can change global varible not enclosing
 -->nolocal only can change enclosing not global
 """

x="Global"
def outer():
    #global x
    x="enclosing" #we can use global for enclosing varible truns into  global
    def inner():
        nonlocal x #we can not use nonlocal if this function is not have outer function  also if we previously use global then we can not use nonlocal in this scope 
        x="local"
        print(x)

    inner()

    print(x)
outer()
print(x)