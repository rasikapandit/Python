num = int(input("Enter Number to check whether it is prime or not "))
def prime_function(x):
    if num == 1:
        print(num,"is not prime")
    elif num == 2:
        print(num,"is prime")
    elif num > 2:
        for i in range(2,num):
             if num % i == 0:
                 print(num,"is not a Prime number")
                 break
        else:
             print(num,"is a prime number")


prime_function(num)
