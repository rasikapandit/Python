name = input("Enter Your Name ")
age = int(input("Enter Your Age "))
n = int(input("Enter Number of Copies "))
num = 100-age
year = num + 2019
for i in range(0,n):
    print("\n"+ name + " you will turn 100 in year " + str(year))
