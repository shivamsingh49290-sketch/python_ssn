from random import *
n=randint(1,10000)
for i in range(4):
    guess = int(input("Enter your guess (1-10000): "))

    if guess == n:
        print(" You Win! You guessed the correct number.")
        break
    else:
        print(" Wrong guess.")

        if i < 3:
            print("Try again!")
        else:
            print("Game Over!")
            print("The correct number was:", n)
