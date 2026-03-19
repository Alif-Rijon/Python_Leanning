import os #os use wheb python itself should work with files,folders and os-level information.

#Firstly we learn about system which is older version of sub-process

os.system("pwd")
os.system("whoami")

#subprocess is modern way 

# import subprocess

# subprocess.run(["ls","-l"])   #here under list first item is command and second item is arguement.
# subprocess.run(["whoami"])

# result = subprocess.run(["pwd"],capture_output=True,text=True)
# print(result.stdout) #output is capture in result variable
# print(result.returncode) #return value
# print(result.stderr)

#complete example:
import subprocess  #subprocess use when run external command 

print("Listing files:")
subprocess.run(["ls"])

print("\nCurrent directory:")
subprocess.run(["pwd"])

print("\nCurrent user:")
subprocess.run(["whoami"])

print("\nDeatailed file list:")
subprocess.run(["ls","-l"])

#os = python handles directly the system 
#subprocess = python asks another command/program to run
