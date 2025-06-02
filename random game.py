import random
import os

lowestNumber = 1
highestNumber = 100
guesses = 0

isRunning = True

answer = random.randint(lowestNumber, highestNumber)

while isRunning:
    os.system('cls')
    print(f"Select a number between {lowestNumber} and {highestNumber}")
    
    guess = input("\nEnter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses = guesses + 1
        if guess < lowestNumber or guess > highestNumber:
            print(f"\n{guess} is an invalid input\n")
        elif guess < answer:
            print(f"\n{guess} is too low!\n")
        elif guess > answer:
            print(f"\n{guess} is too high!\n")
        else:
            print(f"\nThe asnwer is {answer} and you choose {guess} the correct answer!\n")
            print(f"Number of guesses: {guesses}\n")
            isRunning = False
    else:
        print(f"\n{guess} is an invalid input\n")
    os.system('pause')
