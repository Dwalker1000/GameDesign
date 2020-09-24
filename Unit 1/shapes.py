size = 8
for line in range (size):
    print()
    #print first set
    for numebr in range (line+1):
        print('*', end = '')
    #print spaces after first set
    for space in range (size-line-1):
        print(' ', end = '')
    #prints second set
    for number in range (size-line):
        print('*', end ='')
    #prints second set of spaces
    for space in range (line):
        print(' ', end = ' ')
    #prints third set
    for number in range (size-line):
        print('*', end ='')
    #print third set of spaces
    for space in range (size-line-1):
        print (' ',end = '')
    #prints last set
    for numebr in range (line+1):
        print('*', end = '')
