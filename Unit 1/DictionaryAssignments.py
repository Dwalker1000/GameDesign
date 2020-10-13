# 1 Write a Python script to sort (ascending and descending) a dictionary by value.
import operator
d1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_d1 = sorted(d1.items(), key=operator.itemgetter(1))
print(sorted_d1)
sorted_d1 = dict( sorted(d1.items(), key=operator.itemgetter(1),reverse=True))
print(sorted_d1)
print()

# 2 Write a Python script to add a key to a dictionary.
d2 = {0:10, 1:20}
print(d2)
d2.update({2:30})
print(d2)
print()

# 3 Write a Python script to concatenate the following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

dic1.update(dic2)
dic1.update(dic3)
print(dic1)
print()

# 4 Write a Python script to check whether a given key already exists in a dictionary.
d4 = {'z': 10, 'l': 50, 'c': 74, 'm': 12, 'f': 44, 'g': 19}
print(d4)
if 'z' in d4.keys():
    print("True")
else:
    print("False")
print()

# 5 Write a Python program to iterate over dictionaries using for loops.
d5 = {2: 1, 4: 2, 9: 3}
for value_key, value in d5.items():
    print(value_key, 'is to as', d5[value_key])
print()

# 6 Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
x=8
n=int(x)
d6 = dict()
for x in range(1,n+1):
    d6[x]=x*x
print(d6)
print()

# 7 Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
d7=dict()
for x in range(1,16):
    d7[x]=x**2
print(d7)
print()

# 8 Write a Python script to merge two Python dictionaries.
d81 = {'a': 100, 'b': 200}
d82 = {'x': 300, 'y': 200}
d = d81.copy()
d.update(d82)
print(d)
print()

# 9 Write a Python program to iterate over dictionaries using for loops.
d9 = {'g': 1, 'go': 2, 'goo': 3}
for d91, value in d9.items():
    print(d2, 'corresponds to ', d9[d91])
print()

# 10 Write a Python program to sum all the items in a dictionary.
d10 = {'num1':100,'num2':-123,'num3':246}
print(sum(d10.values()))
