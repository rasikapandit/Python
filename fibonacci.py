def fibonacci():
    num = int(input("Enter how many fibonnaci numbers to generate "))
    a = 0
    b = 1
    if num == 0:
        print("Please enter the number which is greater than 0")
    elif num == 1:
        list = [0,1]
        print(list)
    elif num > 1:
        list = [0, 1]
        for i in range(num):
            c = a+b
            list.append(c)
            a = b
            b = c
    print(list)

fibonacci()
