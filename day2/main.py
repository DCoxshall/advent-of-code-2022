# This is some of the worst code I've ever written.

inp = open("input.txt", "r")

total_score = 0
beats = {"A": "B", "B": "C", "C": "A"}        # value beats key
beaten_by = {v: k for k, v in beats.items()}  # key beats value
equals = {"X": "A", "Y": "B", "Z": "C"}
score = {"A": 1, "B": 2, "C": 3}

# Question 1 and question 2, merged into one.

q1_score = 0
q2_score = 0

for line in inp.readlines():
    player1 = line.split(" ")[0][0]
    outcome = line.split(" ")[1][0]
    player2 = equals[outcome]

    # We win
    if beats[player1] == player2:
        q1_score += 6 + score[player2]

    # Elf wins
    elif beats[player2] == player1:
        q1_score += 0 + score[player2]

    # Draw
    else:
        q1_score += 3 + score[player2]

    if outcome == "X":
        player2 = beaten_by[player1]

    elif outcome == "Y":
        player2 = player1

    elif outcome == "Z":
        player2 = beats[player1]

    # We win
    if beats[player1] == player2:
        q2_score += 6 + score[player2]

    # Elf wins
    elif beats[player2] == player1:
        q2_score += 0 + score[player2]

    # Draw
    else:
        q2_score += 3 + score[player2]

print(q1_score)
print(q2_score)

inp.close()
