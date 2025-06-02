steal = 0
share = 1

scoreOne = 0
scoreTwo = 0

decision = 1
enemy = True
player = True

count = 0
total = 0

while(total != 100):

    if enemy == True and decision == share:
        scoreOne = scoreOne + 3
        scoreTwo = scoreTwo + 3
    elif enemy == False and decision == share:
        scoreTwo = scoreTwo + 5
    elif enemy == True and decision == steal:
        scoreOne = scoreOne + 5
    elif enemy == False and decision == steal:
        scoreOne = scoreOne + 1
        scoreTwo = scoreTwo + 1

    if decision == share:
        enemy = True
    elif decision == steal:
        enemy = False

    if count == 2:
        player = False
        decision = 0
        count = 0
    else:
        player = True
        decision = 1
        count += 1

    total += 1

print(f"Player 1 Score: {scoreOne} Player 2 Score: {scoreTwo}")