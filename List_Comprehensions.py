import random
# For initialized list
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [(num) for num in a if num %2 == 0]
print(b)
# By taking Random Inputs
list = []
length = random.randint(1, 15)

for x in range(0,length):
    list.append(random.randint(1, 100))

evenlist = [(i)for i in list if i % 2 == 0]

print(list)
print(evenlist)
