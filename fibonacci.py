def fib():                  
    a=0
    b=1
    c = int(input('Enter the endpoint till where you want your fibonacci sequence ... '))
    print(a)
    print(b)
    for i in range(2,c):
        c=a+b
        a=b
        b=c
        print(c)
fib()
