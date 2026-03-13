#open(filename,mode)
""" there are different mode a file:
-"r"-->read file
-"a"-->append(opens a file for appending,creates the file if does not exist )
-"w"-->write(open a file for writing ,creates the file if it does not exist)
-"x"-->create file
///
we can handle file as binary or text mode
-"t"-->Text(default)
-"b" -->binary mode
 """
# file1= open("demoFile.txt","x")
# file1.close()

file2 = open("demoFile.txt","r")
print(file2.read())
file2.close()

#We can do this same thing in shortcut using with statement

with open("demoFile.txt","r") as f: #if i use with statement i don't need to worry about closing that files
    print(f.read())

#We can specify how many characters i want to read 
file3= open("demoFile.txt","r")
print(file3.read(5))
file3.close()

#we can read a one line using readline()
with open("demoFile.txt","r") as f1:
    print(f1.readline())
    #//////
    print(f1.readline())  #now we can see 2nd line

print("----------")
# we can do this thing using loop
file4=open("demoFile.txt","r")
for x in file4:
    print (x,"\n") #we can do the same thing read()
file4.close()

""" to write in existing file :
-"a" -->will append to the end of the file
-"w"---> will overwrite any existing content
 """
with open("demoFile.txt","w") as f3:
    f3.write("hey this is overrite testing!")

file6= open("demoFile.txt","a")
file6.write("\nthis is appending test")
file6.close()

file7=open("demoFile.txt","r")
print(file7.read())
file7.close()



#we can take a list where contain line that we append in demoFile.txt ---->using writelines
line=["\n line add-1 \n","line add-2\n"]
with open("demoFile.txt","a") as f8:
    f8.writelines(line)



#/////  Dekete file
#file9= open("demo2.txt","x")
import os  #------------------->for delete a file must import os module

#os.remove("demo2") -->>>os.remove("file removed")
#os.rmdir("folder remove")  --> i can only remove empty file
#os.remove("fileHandling.txt")