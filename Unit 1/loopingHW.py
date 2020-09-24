#three loops
#first umber that gets printed and how it gets controlled
top= 5
for i in range (0,top + 1):
    for x in range (top-i, 0,-1):
        #prints the number
        print(x, end = ' ')
        #printe the space between the lines
    print()

#prime number problem
#sets start and finish
start = 25
end = 50
#controlls hw long to run the lines
for i in range(start,end):
    if i>1:
        for j in range (2,i):
            if(i % j==0):
                break
        else:
            print(i,end = ' ')
print()
print()

#sets start varuable
x=0
y=1
#how long you want the program to repete
for number in range(5):
    #prints both varuables
    print (x, end = ' ')
    print (y, end = ' ')
    #adds varuables so they can increse but the last number
    x=x+y
    y=x+y
