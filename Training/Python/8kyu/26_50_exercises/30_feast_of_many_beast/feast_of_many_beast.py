def feast(beast, dish):
    if [beast[0], beast[-1]] == [dish[0], dish[-1]]:
        return True
    else:
        return False


test1 = feast("great blue heron", "garlic naan")
test2 = feast("chickadee", "chocolate cake")
test3 = feast("brown bear", "bear claw")

print(f"{test1} # True")
print(f"{test2} # True")
print(f"{test3} # False")
