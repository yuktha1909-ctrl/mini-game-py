import random

def roll():
    min_value = 1
    max_value = 6
    value = random.randint(min_value, max_value)
    return value


while True:
    players = input("Enter the number of players (2-6): ")

    if players.isdigit():
        players = int(players)

        if 2 <= players <= 6:
            break
        else:
            print("Must be between 2-6")
    else:
        print("Invalid, try again")


max_score = 50
player_scores = [0 for _ in range(players)]


while max(player_scores) < max_score:

    for player_idx in range(players):

        print("\nPlayer number", player_idx + 1, "turn has just started!\n")

        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")

            if should_roll.lower() != "y":
                break

            value = roll()

            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled:", value)

        print("Your score is:", current_score)

        player_scores[player_idx] += current_score

        print("Your total score is:", player_scores[player_idx])


print("Game Over!")

winner = player_scores.index(max(player_scores)) + 1
print("Player", winner, "wins with", max(player_scores), "points!")