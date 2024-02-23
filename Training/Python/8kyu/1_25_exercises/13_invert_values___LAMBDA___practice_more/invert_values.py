def invert(lst):
    elements = list(map(lambda v: v * -1, lst))
    return elements


test1 = invert([1, 2, 3, 4, 5])
test2 = invert([1, -2, 3, -4, 5])
test3 = invert([])

print(f"{test1} # [-1, -2, -3, -4, -5]")
print(f"{test2} # [-1, 2, -3, 4, -5]")
print(f"{test3} # []")
