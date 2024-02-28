def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif p1 == "rock" and p2 == "scissors" or p1 == "scissors" and p2 == "paper" or p1 == "paper" and p2 == "rock":
        return "Player 1 won!"

    else:
        return "Player 2 won!"


test1 = rps('rock', 'scissors')
test2 = rps('scissors', 'rock')
test3 = rps('rock', 'rock')

print(f"{test1} # Player 1 won!")
print(f"{test2} # Player 2 won!")
print(f"{test3} # Draw!")