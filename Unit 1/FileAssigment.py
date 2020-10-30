import os
import time
fileName=input("what do you want to name your file? ")
name= input("what is your name? ")
age = input("how old are you? ")
myFile = open(fileName+".txt", "w")
myFile.write(name + "\n")
myFile.write(age + "\n")
myFile.close()

def menu ():
    print("******************************************************************")
    print("*                              Menu                              *")
    print("*                                                                *")
    print("* 1. create new file                                             *")
    print("* 2. see whats in your file                                      *")
    print("* 3. add to file (inclue file name)                              *")
    print("* 4. write to file (will delete everything in the file you name) *")
    print("* 5. delete file (include file name)                             *")
    print("* 6. stop program                                                *")
    print("******************************************************************")

def start ():
    start = input("(1,2,3,4,5,6) ")
    return start

def newFile ():
    File2name = input("what do you want to name your file? ")
    File2 = open(File2name + ".txt", "w")
    File2.close()

def read ():
    print()
    filename = input("whats your files name? ")
    print()
    print("Whats in your file currently")
    myFile = open(fileName+".txt", "r")
    print(myFile.read())
    myFile.close()

def add():
    filename = input("what file do you want to acsses? ")
    addin = input("what do you want to add to your file? ")
    myFile = open(fileName+ ".txt", "a")
    myFile.write(addin + "\n")
    myFile.close()

def write():
    InPut = input("are you sure that you want to write to the file it will delete all previous informatin in the file (yes or no) ")
    if InPut == 'yes':
        information = input("what do you want to write to the file ")
        myFile = open(fileName+".txt", "w")
        myFile.write(information + "\n")
    elif InPut == 'no':
        print()

def delete():
    name = input("whats yor files name? ")
    if os.path.isfile(name+".txt"):
        os.remove(name+".txt")
        print("success")
    else:
        print("File doesn't exists!")

xyz = 0
while xyz == 0:
    menu()
    x = start()
    while x == '1':
        newFile()
        break
    while x == '2':
        read()
        break
    while x == '3':
        add()
        break
    while x == '4':
        write()
        break
    while x == '5':
        delete()
        break
    while x == '6':
        exit()
