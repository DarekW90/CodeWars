def feast(beast, dish):
    return beast[0]==dish[0] and dish[-1]==beast[-1]


test1 = feast("great blue heron", "garlic naan")
test2 = feast("chickadee", "chocolate cake")
test3 = feast("brown bear", "bear claw")

print(f"{test1} # True")
print(f"{test2} # True")
print(f"{test3} # False")
