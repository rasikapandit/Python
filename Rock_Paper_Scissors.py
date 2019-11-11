print("Welcome to rock paper scissor Game!")
input1 = str(input("Enter First Player Choice "))
input2 = str(input("Enter Second Player Choice "))

if input1 == input2:
        print(" Draw!!")

elif input1 == 'rock' and input2 =='scissors':
        print("Player 1 Won!!!")
elif input1 == 'scissors' and input2 =='paper':
        print("Player 1 Won!!!")

elif input1 == 'paper' and input2 == 'rock':
        print("Player 1 Won!!!")
elif input2 == 'rock'and input1 =='scissors':
        print("Player 2 Won!!!")

elif input1 == 'paper' and input2 == 'scissors':
        print("Player 2 Won!!!")

elif input2 == 'paper' and input1 == 'rock':
        print("Player 2 Won!!!")

else:
        print("Enter Valid Option")
