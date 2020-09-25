#Daniel Walker
#learning functions
def testing_Functions(): # define the function and expects no peramiters
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
        print

def loops_rows_col(row, col):
    for rows in range (row):
        for cols in range (col):
            print('*', end ='')
        print()

loops_rows_col(5,7)


# x = 4
# print (x)
# for y in range (3):
#     testing_Functions()
