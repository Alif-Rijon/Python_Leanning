print("Hello")
print('Tripty')
print("It's alright")
print('Hey, I am "rijon"')
print("Hey,I'm \"Tripty\"")
a=""" how to write lorem code in,
now i will try this.From help's of "AI\""""
print(a[4])
for r in a:
    print(r)
print(len(a))

#for in loop
for t in "banana":
    print(t)
print(len(t))
 
 #len method
b="hello rijon"
print(len(b))

#check string using in
txt= "the best things in life are free"
check = "freee" in txt
print(check)

txt2= "My name is Rijon"
if "Rijon" in txt2:
    print("Yes,'Rijon' is here.")

#check if not
txt3= "My another name is Alif"
print("Alif" not in txt3)

#slicing

b = "Hello world!"
print(b[2:5]) #last index excluded
print(b[:5])
print(b[2:])
print(b[-5:-2]) #start from last and count start with 1 and last index will be excluded
print("----")
print(b[-5:])  
print(b[:-2])
print(b[:-5])
print(b[-2:])

#strip() method removed any whitespace from beginning or the end

a= " Alif Rijon "
print (a.strip())

# replace and split returns a list 

a= "Alif Rijon"
print(a.replace("A" ,"a"))
print(a.split(","))

#F-string

age=22
txt= f"My age is {age}"
print(txt)

txt1 = f"It can take decimal point like {age:.3f}"
print(txt1)

txt2 = f"i can calculate math in placeholder {5*6}"
print(txt2)
print(txt.count("i"))