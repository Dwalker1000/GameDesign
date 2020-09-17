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
