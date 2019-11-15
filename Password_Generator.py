import random
import string
let = int(input("Enter how many letters you want in your password: "))
num = int(input("Enter how many numbers you want in your password: "))
sym = int(input("Enter how many symbols you want in your password: "))
list = []
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
for i in range(let):
    y = random.choice(letters)
    list.append(y)

for j in range(num):
    x = random.choice(numbers)
    list.append(x)

for j in range(sym):
    z = random.choice(symbols)
    list.append(z)

password = ''.join(list)
print("Your Password is: ",password)

# Second Method
print("---- SECOND METHOD -----")
str = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()?'
len = int(input("Enter length of password you want: "))
passw = ''.join(random.sample(str,len))
print("Your Password is: ",passw)