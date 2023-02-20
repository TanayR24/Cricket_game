import random
dice = [1, 2, 3, 4, 6, 7, 0]

tm1 = input("Enter the name of the team: ")
team1 = tm1.upper()
tm2 = input("Enter the name of the opposition: ")
team2 = tm2.upper()

score1 = 0
wickets1 = 0
score2 = 0
wickets2 = 0
run = 0

match_choice=input("Would you like to Bat or Bowl first: ")
if match_choice.lower() == "bat":
    while wickets1 < 10:
        run = random.choice(dice)
        if run != 0:
            score1 = score1+run
        elif run == 0:
            wickets1 += 1
    print(f"{team1}:{score1}-{wickets1}")

    while wickets2 < 10 and score2 <= score1:
        run = random.choice(dice)
        if run != 0:
            score2 = score2+run
        elif run == 0:
            wickets2 += 1

    print(f"{team2}:{score2}-{wickets2}")
    if score2 > score1:
        print(f"{team2} won the game by {10-wickets2} wickets")
    elif score2 == score1:
        print("The game is tied.")
    else:
        print(f"{team1} won the game by {score1-score2} runs.")

elif match_choice.lower() == "bowl":
    while wickets2 < 10:
        run = random.choice(dice)
        if run != 0:
            score2 = score2+run
        elif run == 0:
            wickets2 += 1
    print(f"{team2}:{score2}-{wickets2}")

    while wickets1 < 10 and score1 <= score2:
        run = random.choice(dice)
        if run != 0:
            score1 = score1+run
        elif run == 0:
            wickets1 += 1

    print(f"{team1}:{score1}-{wickets1}")
    if score1 > score2:
        print(f"{team1} won the game by {10-wickets1} wickets")
    elif score2 == score1:
        print("The game is tied.")
    else:
        print(f"{team2} won the game by {score2-score1} runs.")