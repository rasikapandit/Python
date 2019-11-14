#In this function one drwaback is there what if all the elements are same.
def rvm_duplicates():
    num = int(input("Enter how many numbers you want to insert in a list: "))
    list = []
    for i in range(num):
        nums = int(input("Enter the numbers to insert in a list: "))
        list.append(nums)
    print(list)
    mylist = list
    for j in mylist:
        if mylist.count(j) > 1:
            mylist.remove(j)
    print(mylist)

#Another method
def rvms_duplicate(listp):
    num = int(input("Enter how many numbers you want to insert in a list: "))
    list = []
    mylist = []
    for i in range(num):
        nums = int(input("Enter the numbers to insert in a list: "))
        list.append(nums)
    for i in list:
        if i not in mylist:
            mylist.append(i)
    print(list)
    print(mylist)

rvm_duplicates()
rvms_duplicate(list)