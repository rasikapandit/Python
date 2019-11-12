import random
a = []
b = []
#Generating random number.
for z in range(1,13):
    x = random.randint(1,30)
    y = random.randint(1,30)
    a.append(x)
    b.append(y)
print(a)
print(b)
mylist = []
#Finding Common Number
for i in a:
    for j in b:
        if i==j:
            if i not in mylist:
                mylist.append(i)
print("Repeat number's list: ",mylist)
# Print in one line.
print("Print in one line answer: ",[(i) for i in set(a) for j in set(b) if i==j])