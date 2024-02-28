def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]


test1 = rps('rock', 'scissors')
test2 = rps('scissors', 'rock')
test3 = rps('rock', 'rock')

print(f"{test1} # Player 1 won!")
print(f"{test2} # Player 2 won!")
print(f"{test3} # Draw!")