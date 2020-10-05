# 1
n1=(4,3,2,1)
#2
n2=(1, 2,'burger', 'Pizza')
#3
print('3.', end ='')
n3=(1,2,3,4,5)
print(n3[4])
print()
#4
print('4.', end ='')
n4=(1,2,3,4,5)
print(n4[1:4])
print()
#5
n5 = [1,2,3,4]
n5.append(5)
#6
n6 = (1,2,3,4,5)
x=[]
x.append(n6)
#7
n7 = (0,1,2,3,4,5,6,7,8,9)
print(n7[3])
print(n7[-4])
print()
#8
n8 = (1,2,3,4)
x= len(n8)
for line in range (0,x):
    print(n8[line])
print()
#9
n9 = (1,2,3,4,1,4,2,3,4,1,2,3,4)
for line in range (1,5):
    count = n9.count(line)
    print(line,end = ' ')
    print('is repeted',end = ' ')
    print(count, end = ' ')
    print('times')
print()
#10
tuplex = ("r",'e','s','o','u','r','c','e',8,6,7,5)
print("r" in tuplex)
print(9 in tuplex)
