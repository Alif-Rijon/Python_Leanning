import os
import subprocess

folders_name=["data","logs","scripts"]

for i in folders_name:
    if not os.path.exists(i):
        os.mkdir(i)
        print("Created:",i)

    else:
        print("Already exists:",i)

for i in folders_name:
     if i== "logs":
            if not os.path.exists("logs/app"):
                os.mkdir("logs/app")
                print("app folder is created.")
            else:
                print("app folder is already exists under logs")  
            if not os.path.exists("logs/app/app.log"):
               file =open("logs/app/app.log","x")
               file.close()
               print("File is created")
            else:
               print("File already exists.")  

                    
print("Setup complete.\nCurrent directory lists: \n",os.listdir())
print("\nCurrent directory lists from linux command shell:\n")
subprocess.run(["ls","-l"])
