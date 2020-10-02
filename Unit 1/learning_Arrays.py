names = ['Ali', 'justin', 'Daniel', 'Jake', 'Rohan', 'Sarah', 'Augest', 'Aarian', 'Kunal', 'Safin']
#          0       1         2         3       4        5        6          7        8        9
print('list of names in class')
for i in range (len(names)):
    print(names[i], end = ' ')
print()
print()
print('list of diffrent foods')
food = ['pizza', 'burger', 'pasta', 'fries']
#copys array
newfood = food.copy()
#removes fries from list
food.remove('fries')
#removes second  word
food.pop(1)
#will delete second word completly
#del food will delete array completly
del food[1]
print(food)
#adds to end of array
food.append('burger')
#adds to specific spot
food.insert(2, 'pasta')
print(food)
print(newfood)
#takes everthing out of array
#empties array
newfood.clear()
print(newfood)
newfood.append('milkshake')
print(newfood)
for i in range(len(food)):
    print(food [i], end = ' ')
#checks if fries is in food
if 'pizza' in food:
    print('eat pizza')
else:
    print('get pizza')
print(len(food))
print()


mylist = [2,4,5,7,8,9]
yourlist = [1,2,3,4,5,6,7]
otherlist = [2,4,6,8]
#tuple cannot be changed
numbers=(4,3,2,1)
print(numbers)
#prints first number
print(mylist[1])
print()
#prints 2 numbers back from 2 so 8
print(mylist[-2])
print()
#prints from the first number to the 3rd number
print(mylist[1:4])
#chesck if 4 is in mylist
if 4 in mylist:
    print('yes')
print()
for x in mylist:
    print(x)
#easiest way to compine list
ourlist= mylist+yourlist

#changes original list
for i in newfood:
    otherlist.append(i)
print(otherlist)
print(ourlist)
#joins list
otherlist.extend(food)
print(otherlist)
#sorts list aphabetcly
food.sort()
print(food)
