import os

questions = ("1 + 1 = ?",
             "What is the first letter in alphabet ? ",
             "What is the color of apple ? ",
             "How many legs dog have? ",
             "It is the 3rd planet in solar system")

options = (("A. 1", "B. 2", "C. 3", "D. 4"),
           ("A. A", "B. B", "C. C", "D. D"),
           ("A. Red", "B. Blue", "C. Green", "D. Orange"),
           ("A. 1", "B. 2", "C. 3", "D. 4"),
           ("A. venus", "B. mercury", "C. mars", "D. earth"))


answer = ("B", "A", "A", "D", "D")
guesses = []
score = 0
questionsNumber = 0

for question in questions:
    os.system('cls')
    print(question)
    for option in options[questionsNumber]:
        print(option)
    print("-----------------------")
    guess = input("TYPE YOU ANSWER: ").upper()
    print("-----------------------")
    guesses.append(guess)
    if guess == answer[questionsNumber]:
        score = score + 1
        print("YOU GOT IT RIGHT!!!")
        print("-----------------------")
    else:
        print(f"THE RIGHT ANSWER WAS: {answer[questionsNumber]}")
        print("-----------------------")

    questionsNumber = questionsNumber + 1
    os.system('pause')

os.system('cls')
score = (score / len(questions) * 100)
print("---------------")
print("RIGHT ANSWER")
print("---------------")
for answer in answer:
    print(answer, end = " ")
print()
print("---------------")
print("YOUR ANSWER")
print("---------------")
for guess in guesses:
    print(guess, end = " ")
print()
print("---------------")
print(f"RESULT: {score} / {len(questions) * 20}")
print("---------------")