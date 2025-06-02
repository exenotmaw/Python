import random
import os

def get_user_guess():
    os.system('cls')
    guess = []
    print("\nGuess the arrangement of the cards from 1 to 10.")
    print("Each number must be unique and between 1 and 10.\n")
    
    for i in range(1, 11):
        while True:
            try:
                temp = int(input(f"Enter your guess #{i}: "))
                if temp < 1 or temp > 10:
                    print("Please enter a number between 1 and 10.")
                elif temp in guess:
                    print("You already guessed that number.")
                else:
                    guess.append(temp)
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return guess

def calculate_score_and_feedback(guess, answer):
    correct = 0
    correct_positions = []
    
    for i, (g, a) in enumerate(zip(guess, answer)):
        if g == a:
            correct += 1
            correct_positions.append(i + 1)
    return correct, correct_positions

cards = list(range(1, 11))
random.shuffle(cards)

attempts = 0

while True:
    attempts += 1
    guess = get_user_guess()
    score, correct_positions = calculate_score_and_feedback(guess, cards)

    print(f"\nYou got {score} cards in the correct position.")

    if correct_positions:
        print("Correct positions:", ", ".join(str(pos) for pos in correct_positions))
    else:
        print("No cards in the correct position.")

    if score == 10:
        print(f"\nCongratulations! You guessed all cards correctly in {attempts} attempt(s).")
        print("Final answer:", cards)
        break
    else:
        print("Try again!\n")
    os.system('pause')
