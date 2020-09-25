#Daniel Walker
#having fun with loops
#learn how to resize our programs
#asking the usr for values
#is requesting values via consle input
#type casting
begin = 10
lines = int(begin)
for line in range(lines):
    for number in range(begin-line,0,-1):
        print(number, end = ' ')
    print()
