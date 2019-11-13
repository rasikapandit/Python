n = int(input("Enter number of elements in list: "))
a =[]
def list_end():
    for i in range(0, n):
        num = int(input("Enter "+ str(i+1)+"st/nd/th element in the list: "))
        a.append(num)

    #Adding and first and last element in other list.
    print([a[0],a[n-1]])

list_end()