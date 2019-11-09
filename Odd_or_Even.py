number = int(input("Enter a Number "))
if number % 2 == 0:
    print("Number is Even")
    if number % 4 == 0:
        print("AND Number is Multiplied by 4")
else:
    print("Number is odd")