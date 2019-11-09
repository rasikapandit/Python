number = int(input("Enter a Number "))
mylist = []
for x in range(1,number+1):
    if number % x == 0:
        mylist.append(x)
print(mylist)