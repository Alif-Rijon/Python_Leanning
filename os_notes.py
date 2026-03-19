#Current working dictory (getcwd())
import os 
print(os.getcwd())

#Listing files and folders (listdir()) --by default
print(os.listdir())

#Creating a folder (mkdir())
#print(os.mkdir("testos"))

print("-------")

#check listing
print(os.listdir("testos"))

#check first is folder/file exist or not . --->for this purpose we use os.path.exists("")
#Ex-1:
if not os.path.exists("testos"):
    os.mkdir("testos")
    print("TestOs folder is created")
else:
    print("TestOs folder is already exists")

# Ex-2: ------->Always check current folder if we want to check another folder then must be specified path like(testos/testFile.txt)
if os.path.exists("testos/testFile.txt"):
    print("This is current working dictory for this file:",os.getcwd())
    print(os.listdir())
    print(os.listdir("testos"))
else:
    print("file doesn't exists")

# ex-3 ---->File creating under a folder and check is file exist under that folder?
if not os.path.exists("testos/demoFile.txt"):
    f= open("testos/demoFile.txt","x")
    print("File is created!")
else:
    print("File is exists")

print("---------")

#### Complete Example:
import os 

print("Current directory:")
print(os.getcwd())

print("\n Files and folders before:")
print(os.listdir())

folder_name="testos"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("\n Folder created:",folder_name)
else:
    print("\n Folder already exists:",folder_name)

print("Files and Folders after:")
print(os.listdir())