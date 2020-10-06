#1 Write a Python program to create a tuple
n1=(4,3,2,1)
#2 Write a Python program to create a tuple with different data types3
n2=(1, 2,'burger', 'Pizza')
#3 Write a Python program to create a tuple with numbers and print one item
print('3.', end ='')
n3=(1,2,3,4,5)
print(n3[4])
print()
#4 Write a Python program to unpack a tuple in several variables
print('4.', end ='')
tuplex=(1,2,3)
n1, n2, n3 = tuplex
print(n1)
print(n2)
print(n3)
print()
#5 Write a Python program to add an item in a tuple
#cant add items to a tupple
#6 Write a Python program to convert a tuple to a string
n6 = (1,2,3,4,5)
x=[]
x.append(n6)
#7 Write a Python program to get the 4th element and 4th element from the last of a tuple
n7 = (0,1,2,3,4,5,6,7,8,9)
print(n7[3])
print(n7[-4])
print()
#8 Write a Python program to create the colon of a tuple
from copy import deepcopy
n8 = ('Hello', 5, [], True)
print(n8)
tuplex_colon = deepcopy(n8)
tuplex_colon [2].append (50)
print(tuplex_colon)
print(n8)
print()
#9 Write a Python program to find the repeated items of a tuple
n9 = (1,2,3,4,1,4,2,3,4,1,2,3,4)
for line in range (1,5):
    count = n9.count(line)
    print(line,end = ' ')
    print('is repeated',end = ' ')
    print(count, end = ' ')
    print('times')
print()
#10 Write a Python program to check whether an element exists within a tuple
n10 = ("r",'e','s','o','u','r','c','e',8,6,7,5)
print("r" in n10)
print(9 in n10)
print()
#11 Write a Python program to convert a list to a tuple
n11 = ["mon", "Tue", "wed", 1,2,3]
x = tuple(n11)
#12 Write a Python program to remove an item from a tuple
n12 = (1,2,3,4,5,6,7,8,9)
#cannot remove items from a tuple
#13 Write a Python program to slice a tuple
n13 = (0,1,2,3,4,5,6,7,8,9)
x = (len(n13))
y = int(x/2)
print(n13[:y])
print(n13[y:])
print()
#14 Write a Python program to find the index of an item of a tuple
n14 = (1,4,2,5,3,7,6,8,0,9)
print(n14.index(5))
print()
#15 Write a Python program to find the length of a tuple
n15= (0,1,2,3,4,5,6,7,8,9)
print(len(n15))
print()
#16 Write a Python program to convert a tuple to a dictionary
# n16 = (0,1,2,3,4,5,6,7,8,9)
# print (dict[n16])
# skip
# 17.Write a Python program to unzip a list of tuples into individual lists
n17 = [(1,2,3), (4,5,6), (7,8,9)]
print(list(zip(*n17)))
# 18.Write a Python program to reverse a tuple
n18 = (0,1,2,3,4,5,6,7,8,9)
y = list(n18)
y.reverse()
print (y)
# 19.Write a Python program to convert a list of tuples into a dictionary
# skip
# 20.Write a Python program to print a tuple with string formatting.Sample tuple : (100, 200, 300)Output :This is a tuple (100, 200, 300)
# 21.Write a Python program to replace last value of tuples in a list.Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
# 22.Write a Python program to remove an empty tuple(s) from a list of tuples.Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
# 23.Write a Python program to sort a tuple by its float element.Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
# 24.Write a Python program to count the elements in a list until an element is a tuple.
