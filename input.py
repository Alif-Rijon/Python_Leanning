print("what is your name?")
name= input()  #this is use for when we want to user give input in new line 
print (f"My name is {name}")

#Another way ,input() function has prompt parameter that's why we can take input at same line

age=input("How old are you?")
print(f"My age is {float(age)}")
print(4+int(age)) #All input take as string so if we want to use for cal. then must do typecasting
print(type(age))

#validate input
y= True
while y== True:
    x =input("Enter a number:")
    try:
        x= float(x)
        y=False
    except:
        print("Wrong input, please try again")
print("Thank you!")
        