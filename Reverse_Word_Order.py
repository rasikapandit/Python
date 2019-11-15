def reverse():
    str = input("Enter a string: ")
    print(str)
    strlist = str.split( )
    x = strlist[::-1]
    res = " ".join(x)
    print(res)

reverse()


