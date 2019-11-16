import random
def cowbull():
    print(' Welcome to Cows And Bulls !!!!')
    number = str(random.randint(1000, 9999))
    guess = 0
    cows = 0
    bulls = 0
    count = 0
    inp = ''
    while inp != 'exit' or guess != number :
        inp = input("Type 'exit' to exit the game or 'c' to continue: ")
        if inp == 'exit':
            print("You Exited.")
            break
        elif inp == 'c':
            guess = input("Guess the correct number between 1000 to 9999, type here: ")
            count += 1
            if  guess == number:
                bulls = 4
                print(bulls,"bulls. You Won! You gussed in ", count, "chances.")
                break
            else:
                for i in range(len(number)):
                        if number[i] == guess[i]:
                            bulls += 1
                        else:
                            cows += 1
                print(bulls,"bulls, ",cows,"cows")
                cows = 0
                bulls = 0
        else:
            print("Please enter valid choice")

cowbull()


