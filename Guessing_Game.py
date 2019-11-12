import random
print(' Welcome to number guessing game !!!!')
number = random.randint(1,9)
#To check the number
#print(number)
guess = 0
count = 0
inp = ''
while inp != 'exit':
    inp = input("Type 'exit' to exit the game or 'c' to continue: ")
    if inp == 'exit':
        print("You Exited.")
        break
    elif inp == 'c':
        guess = input("Guess the correct number between 1 to 9, type here: ")
        guess = int(guess)
        count += 1
        if  guess == number:
            print("You Won! You gussed in ", count, "chances.")
            break
        elif guess< number:
            print("Number is greater than your guess")
        elif guess > number:
            print("Number is less than your guess")
    else:
        print("Please enter valid choice")


