#Daniel Walker
#having fun with loops
#learn how to resize our programs
#asking the usr for values
#is requesting values via consle input
#type casting
input = int(input('program number (1,2)\n'))
begin = int(input('number input\n'))
lines = begin
if input == 1:
    for line in range(lines):
        print(line-1, end = ' ')
elif input == 2:
    for number in range(begin-line,0,-1):
        print(number, end = ' ')
print()
