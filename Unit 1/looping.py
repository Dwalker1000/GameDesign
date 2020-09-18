for x in range(1,10):
    print (x,end =" ")
print("")

for x in range(1,5):
    print (x)
print("")

#nested loops
for line in range(1,10):
    for x in range(line):
        print (line, end = ' ')
    print("")
#controls where the pryrimid will start at
x=0
#controls where it wil finish
#will break if number is over 10
y=10
for line in range(x,y):
    #mkae sure each number is on a diffrent line
    print()
#both loops uses line to control flow
    for space in range (9-line):
        #prints spaces on first side
        print(" ",end='')
    for number in range (line):
        #prints the first side numbers
        print (line,end ='')
    #prints space in between both sides
    print (' ',end ='')
    for number in range(line):
        #prints the second set of numbers
        print (line, end = '')
print()
print()

top= 5
for i in range (0,top + 1):
    for x in range (top-i, 0,-1):
        print(x, end = ' ')
    print()

start = 25
end = 50
for i in range(start,end):
    if i>1:
        for j in range (2,i):
            if(i % j==0):
                break
        else:
            print(i,end = ' ')
print()
print()

x=0
y=1
for number in range(5):
    print (x, end = ' ')
    print (y, end = ' ')
    x=x+y
    y=x+y
