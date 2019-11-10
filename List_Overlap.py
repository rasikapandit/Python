import random
a = []
b = []
#Generating random number.
for z in range(1,6):
    x = random.randint(1,20)
    y = random.randint(1,20)
    a.append(x)
    b.append(y)
print(a)
print(b)
mylist = []
#Finding Common Number
for i in a:
    for j in b:
        if i==j:
            mylist.append(j)
print(mylist)
# Print in one line.
print( [(j) for i in a for j in b if i==j] )