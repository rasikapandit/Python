a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input("Enter a number "))
mylist = []
for element in a:
    if element < num:
        mylist.append(element)
print(mylist)
# To print in one line
print([x for x in a if x < num])
