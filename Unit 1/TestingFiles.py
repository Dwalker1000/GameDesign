#Daniel Walker
#10/28/2020
#learning about files
# open
# cloes
# write   "w"
# append  "a"
# read    "r"
# create a fileVariableName = open("fileName.txt", function)
# to remove a file you need to use the OS module
import os
import time
myFile = open("newFile.txt", "w") # open file if it exist, if not it will create file
myFile.write("i am adding some stuff")
myFile.close()
myFile = open("newFile.txt", "r")
print(myFile.read())
myFile.close()
# when you use w it will overwrite
myFile = open("newFile.txt", "w") # open file if it exist, if not it will create file
myFile.write("Opps, I deleted my stuff\n")
myFile.close()
myFile = open("newFile.txt", "r")
print(myFile.read())
myFile.close()
#i am going to add more info to myFile
myFile = open("newFile.txt", "a") # open file if it exist, if not it will create file
myFile.write("I add more stuff\n")
myFile.close()
myFile = open("newFile.txt", "r")
print(myFile.read())
myFile.close()
time.sleep(2)
if os.path.exists("Game1.py"):
    print("yes")
else:
    print("no")
myFile = open("lineFile.txt", "w")
for i in range(10):
    word = "this is line number " + str(i+1)+ "\r"
    myFile.write(word)
myFile.close()
myFile = open("lineFile.txt", "r")
print(myFile.read())
myFile.close()
