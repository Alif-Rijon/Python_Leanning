# walrus operator :=
numbers= [1,2.3,4,5]
if (count := len(numbers)) >2:
    print(f"List has {count} element")

#logical operator and ,or ,not

x=5
print(not(x>3 and x<22))


#identity operator

x="rijon"
y= "rijon"
z=x
#checks value
print(x==z) #== - Checks if the values of both variables are equal
print(x==y)
print("---")
#checks objects
print(x is y) # is - Checks if both variables point to the same object in memory
print(z is x)

#Membership operator
print("nh" in x)

age = int(input("give a random number"))
print(age)