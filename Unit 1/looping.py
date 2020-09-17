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

for line in range(1,10):
    print()
#both loops uses line to control flow
    for space in range (9-line):
        print(" ",end='')
    for number in range (line):
        print (line,end ='')
    for number in range(line):
        print (line, end = '')
