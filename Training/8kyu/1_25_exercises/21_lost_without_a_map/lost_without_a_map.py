def maps(a):
    return [i * 2 for i in a]



test1 = maps([1, 2, 3])
test2 = maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
test3 = maps([])

print(f"{test1} # [2, 4, 6]")
print(f"{test2} # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]")
print(f"{test3} #  []")